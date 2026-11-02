# Multiprocessing

**NOTE**: Because this client uses [`grpc`](https://grpc.github.io/grpc/python/grpc.html#module-grpc) library, it is safe to
share instances across threads. In multiprocessing scenarios, the best
practice is to create client instances *after* the invocation of
[`os.fork()`](https://python.readthedocs.io/en/latest/library/os.html#os.fork) by [`multiprocessing.pool.Pool`](https://python.readthedocs.io/en/latest/library/multiprocessing.html#multiprocessing.pool.Pool) or
[`multiprocessing.Process`](https://python.readthedocs.io/en/latest/library/multiprocessing.html#multiprocessing.Process).
