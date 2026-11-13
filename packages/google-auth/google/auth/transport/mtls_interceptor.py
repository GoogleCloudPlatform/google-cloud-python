"""mTLS Interceptor and Channel Wrapper for certificate rotation."""

import collections
import threading
import time

import grpc
from google.auth import transport

class CertRotationInterceptor(
    grpc.UnaryUnaryClientInterceptor,
    grpc.UnaryStreamClientInterceptor,
    grpc.StreamUnaryClientInterceptor,
    grpc.StreamStreamClientInterceptor,
):
    """A gRPC client interceptor that provides automatic retry logic for mTLS certificate rotation.

    This interceptor wraps all gRPC client calls (unary and streaming) with retryable
    futures or iterators. Its primary role is to monitor responses for `UNAUTHENTICATED`
    errors. When an authentication failure occurs, it uses `_should_retry()` to check
    if a new mTLS certificate is available. If a new certificate is found, it signals
    its associated `MTLSRefreshingChannel` wrapper to refresh the underlying gRPC
    channel's credentials and automatically replays the failed RPC.
    """

    def __init__(self, wrapper=None):
        self._wrapper = wrapper
        self._max_retries = transport.DEFAULT_MAX_REFRESH_ATTEMPTS

    def _should_retry(self, code, retry_count, attempt_cert):
        """Determines if the RPC should be retried due to a certificate rotation.

        Returns a tuple: (should_retry, call_cert_bytes, call_key_bytes, passphrase).
        """
        if code != grpc.StatusCode.UNAUTHENTICATED or not self._wrapper:
            return False, None, None, None

        if retry_count >= self._max_retries:
            _LOGGER.debug(
                "Max retries reached (%d/%d) for channel recreation.",
                retry_count,
                self._max_retries,
            )
            return False, None, None, None

        # If another thread already refreshed the channel with an updated cert, retry immediately
        if attempt_cert != self._wrapper._cached_cert:
            return True, None, None, None

        # Check if the certificate on disk or callback has changed since this request was attempted
        (
            call_cert_bytes,
            call_key_bytes,
            passphrase,
            cached_fingerprint,
            current_cert_fingerprint,
        ) = _mtls_helper.check_parameters_for_unauthorized_response(attempt_cert)
        should_retry = cached_fingerprint != current_cert_fingerprint
        return should_retry, call_cert_bytes, call_key_bytes, passphrase

    def intercept_unary_unary(self, continuation, client_call_details, request):
        return _RetryableUnaryResponseFuture(
            continuation, client_call_details, request, self, is_client_stream=False
        )

    def intercept_stream_unary(
        self, continuation, client_call_details, request_iterator
    ):
        return _RetryableUnaryResponseFuture(
            continuation,
            client_call_details,
            request_iterator,
            self,
            is_client_stream=True,
        )

    def intercept_unary_stream(self, continuation, client_call_details, request):
        return _RetryableStreamResponseIterator(
            continuation, client_call_details, request, self, is_client_stream=False
        )

    def intercept_stream_stream(
        self, continuation, client_call_details, request_iterator
    ):
        return _RetryableStreamResponseIterator(
            continuation,
            client_call_details,
            request_iterator,
            self,
            is_client_stream=True,
        )


class MTLSRefreshingChannel(grpc.Channel):
    def __init__(self, target, factory_args, initial_channel, initial_cert, create_channel_fn):
        self._target = target
        self._create_channel_fn = create_channel_fn
        self._channel = initial_channel
        self._cached_cert = initial_cert
        self._lock = threading.Lock()
        self._subscribers = set()

    def refresh_logic(
        self, count, call_cert_bytes=None, call_key_bytes=None, passphrase=None
    ):
        with self._lock:
            if not call_cert_bytes or self._cached_cert == call_cert_bytes:
                return

            _LOGGER.debug("Wrapper: Refreshing mTLS channel. Retry count: %d", count)
            old_channel = self._channel

            if passphrase is not None:
                call_key_bytes = _mtls_helper.decrypt_private_key(
                    call_key_bytes, passphrase
                )

            # Call the partial, overriding only the cert-related arguments
            new_ssl_credentials = grpc.ssl_channel_credentials(
                certificate_chain=call_cert_bytes,
                private_key=call_key_bytes,
            )

            self._channel = self._create_channel_fn(
                ssl_credentials=new_ssl_credentials,
                client_cert_callback=None
            )


            self._channel = secure_authorized_channel(**factory_args)
            self._cached_cert = call_cert_bytes
            for callback in self._subscribers:
                try:
                    old_channel.unsubscribe(callback)
                except Exception:
                    pass
                self._channel.subscribe(callback)

    def unary_unary(self, method, *args, **kwargs):
        # Always return a callable from the CURRENT channel
        return self._channel.unary_unary(method, *args, **kwargs)

    # Mandatory passthroughs
    def unary_stream(self, method, *args, **kwargs):
        return self._channel.unary_stream(method, *args, **kwargs)

    def stream_unary(self, method, *args, **kwargs):
        return self._channel.stream_unary(method, *args, **kwargs)

    def stream_stream(self, method, *args, **kwargs):
        return self._channel.stream_stream(method, *args, **kwargs)

    def subscribe(self, callback, try_to_connect=False):
        with self._lock:
            self._subscribers.add(callback)
            return self._channel.subscribe(callback, try_to_connect=try_to_connect)

    def unsubscribe(self, callback):
        with self._lock:
            self._subscribers.discard(callback)
            return self._channel.unsubscribe(callback)

    def close(self):
        self._channel.close()


class _ReplayableIterator(object):
    def __init__(self, target_iterator, max_items=1000):
        self._target_iterator = iter(target_iterator)
        self._max_items = max_items
        self._buffer = []
        self._exhausted = False
        self._can_replay = True

        self._lock = threading.Lock()
        self._consumer_lock = threading.Lock()
        self._active_reader = None

    def __iter__(self):
        reader = _ReplayableIteratorReader(self)
        with self._lock:
            self._active_reader = reader
        return reader

    def can_replay(self):
        with self._lock:
            return self._can_replay


class _ReplayableIteratorReader(object):
    def __init__(self, parent):
        self._parent = parent
        self._read_index = 0

    def __next__(self):
        while True:
            with self._parent._lock:
                if self._read_index < len(self._parent._buffer):
                    val = self._parent._buffer[self._read_index]
                    self._read_index += 1
                    return val

                if self._parent._exhausted:
                    raise StopIteration()

                if self._parent._active_reader is not self:
                    raise StopIteration()

            with self._parent._consumer_lock:
                with self._parent._lock:
                    if self._read_index < len(self._parent._buffer):
                        continue
                    if self._parent._active_reader is not self:
                        raise StopIteration()

                try:
                    val = next(self._parent._target_iterator)
                except StopIteration:
                    with self._parent._lock:
                        if self._parent._active_reader is self:
                            self._parent._exhausted = True
                    raise

            with self._parent._lock:
                if self._parent._active_reader is not self:
                    if self._parent._can_replay:
                        self._parent._buffer.append(val)
                    raise StopIteration()

                if self._parent._can_replay:
                    self._parent._buffer.append(val)
                    if len(self._parent._buffer) > self._parent._max_items:
                        self._parent._buffer.clear()
                        self._parent._can_replay = False

                self._read_index += 1
                return val


_ClientCallDetails = collections.namedtuple(
    "_ClientCallDetails",
    ("method", "timeout", "metadata", "credentials", "wait_for_ready"),
)


class _DeadlineExceededError(grpc.RpcError, grpc.Call):
    def __init__(self, details):
        super().__init__()
        self._details = details

    def code(self):
        return grpc.StatusCode.DEADLINE_EXCEEDED

    def details(self):
        return self._details


class _RetryableUnaryResponseFuture(_BaseCallWrapper):
    def __init__(
        self,
        continuation,
        client_call_details,
        request_or_iterator,
        interceptor,
        is_client_stream=False,
    ):
        self._continuation = continuation
        self._client_call_details = client_call_details
        self._is_client_stream = is_client_stream
        self._source_request = request_or_iterator
        self._interceptor = interceptor

        self._uses_factory = is_client_stream and callable(request_or_iterator)
        self._payload = (
            None
            if self._uses_factory
            else (
                _ReplayableIterator(request_or_iterator)
                if is_client_stream
                else request_or_iterator
            )
        )

        self._retry_count = 0
        self._call = None
        self._lock = threading.RLock()

        timeout = getattr(self._client_call_details, "timeout", None)
        self._initial_timeout = timeout if isinstance(timeout, (int, float)) else None
        self._start_time = time.monotonic() if self._initial_timeout else None

        self._completion_event = threading.Event()
        self._done_callbacks = []
        self._terminal_exception = None

        self._start_call()

    def _start_call(self):
        self._attempt_cert = (
            self._interceptor._wrapper._cached_cert
            if self._interceptor._wrapper
            else None
        )

        with self._lock:
            if self._uses_factory:
                payload = self._source_request()
            else:
                payload = (
                    iter(self._payload) if self._is_client_stream else self._payload
                )

            call_details = self._client_call_details
            if self._start_time and self._initial_timeout:
                elapsed = time.monotonic() - self._start_time
                remaining = self._initial_timeout - elapsed
                if remaining <= 0:
                    raise _DeadlineExceededError(
                        "Deadline Exceeded during retry resolution."
                    )
                call_details = _ClientCallDetails(
                    method=call_details.method,
                    timeout=remaining,
                    metadata=call_details.metadata,
                    credentials=call_details.credentials,
                    wait_for_ready=call_details.wait_for_ready,
                )

            self._call = self._continuation(call_details, payload)
            self._call.add_done_callback(self._on_inner_future_done)

    def _on_inner_future_done(self, inner_future):
        with self._lock:
            if self._call is not inner_future:
                return

        if inner_future.cancelled():
            with self._lock:
                self._completion_event.set()
                callbacks_to_fire = list(self._done_callbacks)
            for fn in callbacks_to_fire:
                try:
                    fn(self)
                except Exception as e:
                    _LOGGER.warning("Callback failed: %s", e)
            return

        exc = inner_future.exception()
        if isinstance(exc, grpc.RpcError):
            status_code = exc.code()

            can_replay = (
                True
                if self._uses_factory
                else (self._payload.can_replay() if self._is_client_stream else True)
            )

            should_retry, call_cert, call_key, pwd = self._interceptor._should_retry(
                status_code, self._retry_count, getattr(self, "_attempt_cert", None)
            )
            if can_replay and should_retry:
                if getattr(self._interceptor, "_wrapper", None):
                    try:
                        self._interceptor._wrapper.refresh_logic(
                            1, call_cert, call_key, pwd
                        )
                    except Exception as e:
                        with self._lock:
                            self._terminal_exception = e
                        self._completion_event.set()
                        return
                with self._lock:
                    self._retry_count += 1
                try:
                    self._start_call()
                    return
                except Exception as e:
                    self._terminal_exception = e

            if self._interceptor._wrapper:
                (
                    chk_should_retry,
                    chk_cert,
                    chk_key,
                    chk_pwd,
                ) = self._interceptor._should_retry(status_code, 0, self._attempt_cert)
                if chk_should_retry:
                    try:
                        self._interceptor._wrapper.refresh_logic(
                            1, chk_cert, chk_key, chk_pwd
                        )
                    except Exception:
                        pass
        with self._lock:
            self._completion_event.set()
            callbacks_to_fire = list(self._done_callbacks)

        for fn in callbacks_to_fire:
            try:
                fn(self)
            except Exception as e:
                _LOGGER.warning("Callback failed: %s", e)

    def add_done_callback(self, fn):
        with self._lock:
            if self._completion_event.is_set():
                fire_now = True
            else:
                self._done_callbacks.append(fn)
                fire_now = False

        if fire_now:
            try:
                fn(self)
            except Exception:
                pass

    def result(self, timeout=None):
        if not self._completion_event.wait(timeout):
            raise grpc.FutureTimeoutError()
        with self._lock:
            if self._terminal_exception is not None:
                raise self._terminal_exception
            current_future = self._call
        return current_future.result()

    def exception(self, timeout=None):
        if not self._completion_event.wait(timeout):
            raise grpc.FutureTimeoutError()
        with self._lock:
            if self._terminal_exception is not None:
                return self._terminal_exception
            return self._call.exception()

    def traceback(self, timeout=None):
        if not self._completion_event.wait(timeout):
            raise grpc.FutureTimeoutError()
        with self._lock:
            if self._terminal_exception is not None:
                return self._terminal_exception.__traceback__
            return self._call.traceback()

    def initial_metadata(self):
        self._completion_event.wait()
        with self._lock:
            if self._terminal_exception is not None:
                return None
            return self._call.initial_metadata()

    def trailing_metadata(self):
        self._completion_event.wait()
        with self._lock:
            if self._terminal_exception is not None:
                return None
            return self._call.trailing_metadata()

    def code(self):
        self._completion_event.wait()
        with self._lock:
            if hasattr(self._terminal_exception, "code"):
                return self._terminal_exception.code()
            return self._call.code()

    def details(self):
        self._completion_event.wait()
        with self._lock:
            if hasattr(self._terminal_exception, "details"):
                return self._terminal_exception.details()
            return self._call.details()

class _RetryableStreamResponseIterator(_BaseCallWrapper):
    def __init__(
        self,
        continuation,
        client_call_details,
        request_or_iterator,
        interceptor,
        is_client_stream=False,
    ):
        self._continuation = continuation
        self._client_call_details = client_call_details
        self._is_client_stream = is_client_stream
        self._source_request = request_or_iterator
        self._interceptor = interceptor

        self._uses_factory = is_client_stream and callable(request_or_iterator)
        self._payload = (
            None
            if self._uses_factory
            else (
                _ReplayableIterator(request_or_iterator)
                if is_client_stream
                else request_or_iterator
            )
        )
        self._call = None
        self._retry_count = 0
        self._yielded_any_response = False
        self._lock = threading.RLock()

        timeout = getattr(self._client_call_details, "timeout", None)
        self._initial_timeout = timeout if isinstance(timeout, (int, float)) else None
        self._start_time = time.monotonic() if self._initial_timeout else None

        self._is_completed = False
        self._done_callbacks = []

        self._start_call()

    def _start_call(self):
        self._attempt_cert = (
            self._interceptor._wrapper._cached_cert
            if getattr(self._interceptor, "_wrapper", None)
            else None
        )
        with self._lock:
            if self._uses_factory:
                payload = self._source_request()
            else:
                payload = (
                    iter(self._payload) if self._is_client_stream else self._payload
                )

            call_details = self._client_call_details
            if self._start_time and self._initial_timeout:
                elapsed = time.monotonic() - self._start_time
                remaining = self._initial_timeout - elapsed
                if remaining <= 0:
                    raise _DeadlineExceededError(
                        "Deadline Exceeded during retry resolution."
                    )
                call_details = _ClientCallDetails(
                    method=call_details.method,
                    timeout=remaining,
                    metadata=call_details.metadata,
                    credentials=call_details.credentials,
                    wait_for_ready=call_details.wait_for_ready,
                )

            self._call = self._continuation(call_details, payload)
            self._call.add_done_callback(self._on_inner_call_done)

    def _trigger_callbacks(self):
        with self._lock:
            if self._is_completed:
                return
            self._is_completed = True
            callbacks = list(self._done_callbacks)

        for fn in callbacks:
            try:
                fn(self)
            except Exception:
                pass

    def _on_inner_call_done(self, inner_call):
        with self._lock:
            if self._call is not inner_call:
                return
            # Intercept and suppress premature callbacks for UNAUTHENTICATED.
            # __next__ inherently handles this error and manages triggering callbacks
            # later if retriies are exhausted.
            if (
                callable(getattr(inner_call, "code", None))
                and inner_call.code() == grpc.StatusCode.UNAUTHENTICATED
            ):
                return
        self._trigger_callbacks()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            with self._lock:
                current_call = self._call

            try:
                response = next(current_call)
                self._yielded_any_response = True
                return response
            except StopIteration:
                self._trigger_callbacks()
                raise
            except grpc.RpcError as e:
                status_code = getattr(e, "code", lambda: None)()
                with self._lock:
                    if self._call is not current_call:
                        continue

                can_replay = (
                    True
                    if self._uses_factory
                    else (
                        self._payload.can_replay() if self._is_client_stream else True
                    )
                )

                (
                    should_retry,
                    call_cert,
                    call_key,
                    pwd,
                ) = self._interceptor._should_retry(
                    status_code,
                    self._retry_count,
                    getattr(self, "_attempt_cert", None),
                )

                if not self._yielded_any_response and can_replay and should_retry:
                    try:
                        if getattr(self._interceptor, "_wrapper", None):
                            self._interceptor._wrapper.refresh_logic(
                                1, call_cert, call_key, pwd
                            )

                        with self._lock:
                            self._retry_count += 1
                            self._start_call()

                    except Exception as fallback_e:
                        self._trigger_callbacks()
                        raise fallback_e

                    continue
                else:
                    # Non-retryable error, check if another rotation happened while we were finishing
                    if getattr(self._interceptor, "_wrapper", None):
                        (
                            chk_should_retry,
                            chk_cert,
                            chk_key,
                            chk_pwd,
                        ) = self._interceptor._should_retry(
                            status_code, 0, getattr(self, "_attempt_cert", None)
                        )
                        if chk_should_retry:
                            try:
                                self._interceptor._wrapper.refresh_logic(
                                    1, chk_cert, chk_key, chk_pwd
                                )
                            except Exception:
                                pass  # Terminal anyway

                    self._trigger_callbacks()
                    raise e

    def add_done_callback(self, fn):
        with self._lock:
            if getattr(self, "_is_completed", False):
                fire_now = True
            else:
                self._done_callbacks.append(fn)
                fire_now = False

        if fire_now:
            try:
                fn(self)
            except Exception:
                pass

class _BaseCallWrapper(grpc.Future, grpc.Call):
    """A generic wrapper that delegates standard grpc.Call and grpc.Future 
    methods to an underlying call object.
    """
    
    def cancel(self):
        return self._call.cancel()

    def cancelled(self):
        return self._call.cancelled()

    def running(self):
        return self._call.running()

    def done(self):
        return self._call.done()

    def result(self, timeout=None):
        return self._call.result(timeout=timeout)

    def exception(self, timeout=None):
        return self._call.exception(timeout=timeout)

    def traceback(self, timeout=None):
        return self._call.traceback(timeout=timeout)

    def add_done_callback(self, fn):
        self._call.add_done_callback(fn)

    def initial_metadata(self):
        return self._call.initial_metadata()

    def trailing_metadata(self):
        return self._call.trailing_metadata()

    def code(self):
        return self._call.code()

    def details(self):
        return self._call.details()

    def time_remaining(self):
        return self._call.time_remaining()

    def add_callback(self, callback):
        self._call.add_callback(callback)
