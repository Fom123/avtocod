from .avtocod import AvtoCod

try:
    import uvloop as _uvloop

    _uvloop.install()
except ImportError:  # pragma: no cover
    pass

__all__ = (
    "__version__",
    "types",
    "methods",
    "session",
    "AvtoCod",
)

__version__ = "0.2.1"
