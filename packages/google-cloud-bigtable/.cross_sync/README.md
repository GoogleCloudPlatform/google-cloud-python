# CrossSync

CrossSync provides a simple way to share logic between async and sync code.
It is made up of a small library that provides:
1. a set of shims that provide a shared sync/async API surface
2. annotations that are used to guide generation of a sync version from an async class

Using CrossSync, the async code is treated as the source of truth, and sync code is generated from it.

## Usage

### CrossSync Shims

Many Asyncio components have direct, 1:1 threaded counterparts for use in non-asyncio code. CrossSync
provides a compatibility layer that works with both

| CrossSync | Asyncio Version | Sync Version |
| --- | --- | --- |
| CrossSync.Queue | asyncio.Queue | queue.Queue |
| CrossSync.Condition | asyncio.Condition | threading.Condition |
| CrossSync.Future | asyncio.Future | Concurrent.futures.Future |
| CrossSync.Task | asyncio.Task | Concurrent.futures.Future |
| CrossSync.Event | asyncio.Event | threading.Event |
| CrossSync.Semaphore | asyncio.Semaphore | threading.Semaphore |
| CrossSync.Awaitable | typing.Awaitable | typing.Union (no-op type) |
| CrossSync.Iterable | typing.AsyncIterable | typing.Iterable |
| CrossSync.Iterator | typing.AsyncIterator | typing.Iterator |
| CrossSync.Generator | typing.AsyncGenerator | typing.Generator |
| CrossSync.Retry | google.api_core.retry.AsyncRetry | google.api_core.retry.Retry |
| CrossSync.StopIteration | StopAsyncIteration | StopIteration |
| CrossSync.Mock | unittest.mock.AsyncMock | unittest.mock.Mock |

Custom aliases can be added using `CrossSync.add_mapping(class, name)`

Additionally, CrossSync provides method implementations that work equivalently in async and sync code:
- `CrossSync.sleep()`
- `CrossSync.gather_partials()`
- `CrossSync.wait()`
- `CrossSync.condition_wait()`
- `CrossSync,event_wait()`
- `CrossSync.create_task()`
- `CrossSync.retry_target()`
- `CrossSync.retry_target_stream()`

### Annotations

CrossSync provides a set of annotations to mark up async classes, to guide the generation of sync code.

- `@CrossSync.convert_sync`
  - marks classes for conversion. Unmarked classes will be copied as-is
  - if add_mapping is included, the async and sync classes can be accessed using a shared CrossSync.X alias
- `@CrossSync.convert`
  - marks async functions for conversion. Unmarked methods will be copied as-is
- `@CrossSync.drop`
  - marks functions or classes that should not be included in sync output
- `@CrossSync.pytest`
  - marks test functions. Test functions automatically have all async keywords stripped (i.e., rm_aio is unneeded)
- `CrossSync.add_mapping`
  - manually registers a new CrossSync.X alias, for custom types
- `CrossSync.rm_aio`
  - Marks regions of the code that include asyncio keywords that should be stripped during generation

### Code Generation

Generation can be initiated using `nox -s generate_sync`
from the root of the project. This will find all classes with the `__CROSS_SYNC_OUTPUT__ = "path/to/output"` 
annotation, and generate a sync version of classes marked with `@CrossSync.convert_sync` at the output path.

There is a unit test at `tests/unit/data/test_sync_up_to_date.py` that verifies that the generated code is up to date

## Architecture

CrossSync is made up of two parts:
- the runtime shims and annotations live in `/google/cloud/bigtable/_cross_sync`
- the code generation logic lives in `/.cross_sync/` in the repo root
