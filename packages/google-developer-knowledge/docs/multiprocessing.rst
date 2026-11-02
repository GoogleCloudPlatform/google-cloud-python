.. note::

   Because this client uses :mod:`grpc` library, it is safe to
   share instances across threads. In multiprocessing scenarios, the best
   practice is to create client instances *after* the invocation of
   :func:`os.fork` by :class:`multiprocessing.pool.Pool` or
   :class:`multiprocessing.Process`.
