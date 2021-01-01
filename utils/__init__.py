import fcntl
from contextlib import contextmanager
from typing import IO


@contextmanager
def open_sync(path: str, mode: str = "r"):
    with open(path, mode) as f:
        with _lock_file(f):
            yield f


@contextmanager
def _lock_file(f: IO):
    try:
        # Make sure single process only allowed to access the file at a time.
        # Locking file.
        fcntl.flock(f, fcntl.LOCK_EX)
        yield

        # Releasing the file lock.
        fcntl.flock(f, fcntl.LOCK_UN)
    except:
        # Releasing the file lock in case of error
        fcntl.flock(f, fcntl.LOCK_UN)