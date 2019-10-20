import numpy as np
import numbers
from typing import List


class Segment(np.lib.mixins.NDArrayOperatorsMixin):
    def __init__(self, arr: np.ndarray):
        self._arr = arr

    @property
    def value(self) -> np.ndarray:
        return self._arr

    def __array__(self) -> np.ndarray:
        return self._arr

    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            # Only support operations with instances of _HANDLED_TYPES.
            # Use Segment instead of type(self) for isinstance to
            # allow subclasses that don't override __array_ufunc__ to
            # handle Segment objects.
            if not isinstance(x, self._HANDLED_TYPES + (Segment,)):
                return NotImplemented

        # Defer to the implementation of the ufunc on unwrapped values.
        inputs = tuple(x.value if isinstance(x, Segment) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.value if isinstance(x, Segment) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)

class SegmentCollection:
    def __init__(self, segments: List[np.ndarray]):
        self._segments = segments

    @property
    def segments(self):
        return self._segments
