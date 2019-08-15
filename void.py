# Copyright 2019 ashafer01
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


async def _async_no_op():
    raise StopAsyncIteration


class VoidType(object):
    """Behaves universally falesy, 0-like, and None-like successfully

    Anything that emits data will emit None successfully
        This includes classically numeric operators
        If the python spec requires a specific type, it will be falsey or
        otherwise appropriately pythonic in some way
    All input data is discarded successfully
    Any equality comparisons will be True if other is falsey
    Any strictly numeric comparisons will be completed using 0
    Hashes to None (sadly we cannot satisfy `is None`)
    Iterates over nothing successfully
    Closes all context managers immediately and successfully
    Works as no-op coroutine, async iterator, and async context manager as well
    """

    # save memory

    __slots__ = ('__weakref__',)

    # hash to None

    def __hash__(self):
        return hash(None)

    # be universally falsey

    def __bool__(self):
        return False

    def __len__(self):
        return 0

    def __length_hint__(self):
        return 0

    def __eq__(self, other):
        return not other

    def __ne__(self, other):
        return bool(other) is True

    # be falsey for equality, and 0 for strictly numeric comparisons

    def __le__(self, other):
        try:
            return 0 <= other
        except TypeError:
            return not other

    def __ge__(self, other):
        try:
            return 0 >= other
        except TypeError:
            return not other

    def __lt__(self, other):
        return 0 < other

    def __gt__(self, other):
        return 0 > other

    # always successfully emit none and discard input

    def __call__(self, *args, **kwds):
        pass

    def __getitem__(self, key):
        pass

    def __getattr__(self, attr):
        pass

    def __setitem__(self, key, value):
        pass

    def __setattr__(self, attr, value):
        pass

    def __delitem__(self, key):
        pass

    def __delattr__(self, attr):
        pass

    # numeric conversions are all 0 or similar

    def __complex__(self):
        return complex(0, 0)

    def __float__(self):
        return 0.0

    def __int__(self):
        return 0

    def __index__(self):
        return 0

    def __round__(self):
        return 0

    def __trunc__(self):
        return 0

    def __floor__(self):
        return 0

    def __ceil__(self):
        return 0

    # string behaviors are pythonic

    def __str__(self):
        return 'Void'

    def __repr__(self):
        return 'Void'

    def __format__(self, format_spec):
        return 'Void'

    # exit context managers immediately and successfully (see VoidContext def)

    def __enter__(self):
        return VoidContext()

    def __exit__(self, etype, e, trace):
        return True

    async def __aenter__(self):
        return VoidContext()

    async def __aexit__(self, etype, e, trace):
        async def exit():
            return True
        return exit

    # iterate over nothing / behave like empty sequence

    def __iter__(self):
        return self

    def __reversed__(self):
        return self

    def __bytes__(self):
        return b''

    def __contains__(self, other):
        return False

    # be a no-op coroutine and generator-iterator

    def __await__(self):
        return self

    def __next__(self):
        raise StopIteration

    def send(self, value):
        pass

    def throw(self, type, value=None, traceback=None):
        pass

    def close(self):
        pass

    # asynchronously iterate over nothing

    def __aiter__(self):
        return self

    async def __anext__(self):
        raise StopAsyncIteration

    async def asend(self, value):
        return _async_no_op

    async def athrow(self, type, value=None, traceback=None):
        return _async_no_op

    async def aclose(self):
        return _async_no_op

    # All operators follow the "always emit None" paradigm
    # Many are "usually mathematic" and could behave like 0, but since they
    # could be used with any `other` class then they are interpreted as
    # emitting data and follow the paradigm.
    # Multiplying sequences is a good example of why behaving like 0 is
    # probably the wrong choice.
    # This is also consistent with "discard input data" especially in the case
    # of the in-place operators.

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __matmul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __pow__(self, other, modulo=None):
        pass

    def __lshift__(self, other):
        pass

    def __rshift__(self, other):
        pass

    def __and__(self, other):
        pass

    def __xor__(self, other):
        pass

    def __or__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __rmatmul__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    def __rfloordiv__(self, other):
        pass

    def __rmod__(self, other):
        pass

    def __rdivmod__(self, other):
        pass

    def __rpow__(self, other):
        pass

    def __rlshift__(self, other):
        pass

    def __rrshift__(self, other):
        pass

    def __rand__(self, other):
        pass

    def __rxor__(self, other):
        pass

    def __ror__(self, other):
        pass

    def __iadd__(self, other):
        return self

    def __isub__(self, other):
        return self

    def __imul__(self, other):
        return self

    def __imatmul__(self, other):
        return self

    def __itruediv__(self, other):
        return self

    def __ifloordiv__(self, other):
        return self

    def __imod__(self, other):
        return self

    def __ipow__(self, other, modulo=None):
        return self

    def __ilshift__(self, other):
        return self

    def __irshift__(self, other):
        return self

    def __iand__(self, other):
        return self

    def __ixor__(self, other):
        return self

    def __ior__(self, other):
        return self

    def __neg__(self):
        return self

    def __pos__(self):
        return self

    def __abs__(self):
        return self

    def __invert__(self):
        return self


class VoidException(BaseException):
    """Use a BaseException to hopefully bypass any user exception handling"""
    pass


class VoidContext(object):
    """Always raises an exception to immediately exit the context"""

    # save memory
    __slots__ = ('__weakref__',)

    def __bool__(self):
        raise VoidException()

    def __len__(self):
        raise VoidException()

    def __length_hint__(self):
        raise VoidException()

    def __eq__(self, other):
        raise VoidException()

    def __le__(self, other):
        raise VoidException()

    def __ge__(self, other):
        raise VoidException()

    def __gt__(self, other):
        raise VoidException()

    def __lt__(self, other):
        raise VoidException()

    def __call__(self, *args, **kwds):
        raise VoidException()

    def __getitem__(self, key):
        raise VoidException()

    def __getattr__(self, attr):
        raise VoidException()

    def __setitem__(self, key, value):
        raise VoidException()

    def __setattr__(self, attr, value):
        raise VoidException()

    def __delitem__(self, key):
        raise VoidException()

    def __delattr__(self, attr):
        raise VoidException()

    def __complex__(self):
        raise VoidException()

    def __float__(self):
        raise VoidException()

    def __int__(self):
        raise VoidException()

    def __index__(self):
        raise VoidException()

    def __round__(self):
        raise VoidException()

    def __trunc__(self):
        raise VoidException()

    def __floor__(self):
        raise VoidException()

    def __ceil__(self):
        raise VoidException()

    def __str__(self):
        raise VoidException()

    def __repr__(self):
        raise VoidException()

    def __format__(self, format_spec):
        raise VoidException()

    def __enter__(self):
        raise VoidException()

    def __exit__(self, etype, e, trace):
        raise VoidException()

    def __aenter__(self):
        raise VoidException()

    def __aexit__(self, etype, e, trace):
        raise VoidException()

    def __iter__(self):
        raise VoidException()

    def __reversed__(self):
        raise VoidException()

    def __bytes__(self):
        raise VoidException()

    def __contains__(self):
        raise VoidException()

    def __await__(self):
        return self

    def __next__(self):
        raise StopIteration

    def __aiter__(self):
        return self

    def __anext__(self):
        raise StopAsyncIteration

    async def asend(self, value):
        return _async_no_op

    async def athrow(self, type, value=None, traceback=None):
        return _async_no_op

    async def aclose(self):
        return _async_no_op

    def __add__(self, other):
        raise VoidException()

    def __sub__(self, other):
        raise VoidException()

    def __mul__(self, other):
        raise VoidException()

    def __matmul__(self, other):
        raise VoidException()

    def __truediv__(self, other):
        raise VoidException()

    def __floordiv__(self, other):
        raise VoidException()

    def __mod__(self, other):
        raise VoidException()

    def __divmod__(self, other):
        raise VoidException()

    def __pow__(self, other, modulo=None):
        raise VoidException()

    def __lshift__(self, other):
        raise VoidException()

    def __rshift__(self, other):
        raise VoidException()

    def __and__(self, other):
        raise VoidException()

    def __xor__(self, other):
        raise VoidException()

    def __or__(self, other):
        raise VoidException()

    def __radd__(self, other):
        raise VoidException()

    def __rsub__(self, other):
        raise VoidException()

    def __rmul__(self, other):
        raise VoidException()

    def __rmatmul__(self, other):
        raise VoidException()

    def __rtruediv__(self, other):
        raise VoidException()

    def __rfloordiv__(self, other):
        raise VoidException()

    def __rmod__(self, other):
        raise VoidException()

    def __rdivmod__(self, other):
        raise VoidException()

    def __rpow__(self, other):
        raise VoidException()

    def __rlshift__(self, other):
        raise VoidException()

    def __rrshift__(self, other):
        raise VoidException()

    def __rand__(self, other):
        raise VoidException()

    def __rxor__(self, other):
        raise VoidException()

    def __ror__(self, other):
        raise VoidException()

    def __iadd__(self, other):
        raise VoidException()

    def __isub__(self, other):
        raise VoidException()

    def __imul__(self, other):
        raise VoidException()

    def __imatmul__(self, other):
        raise VoidException()

    def __itruediv__(self, other):
        raise VoidException()

    def __ifloordiv__(self, other):
        raise VoidException()

    def __imod__(self, other):
        raise VoidException()

    def __ipow__(self, other, modulo=None):
        raise VoidException()

    def __ilshift__(self, other):
        raise VoidException()

    def __irshift__(self, other):
        raise VoidException()

    def __iand__(self, other):
        raise VoidException()

    def __ixor__(self, other):
        raise VoidException()

    def __ior__(self, other):
        raise VoidException()

    def __neg__(self):
        raise VoidException()

    def __pos__(self):
        raise VoidException()

    def __abs__(self):
        raise VoidException()

    def __invert__(self):
        raise VoidException()


Void = VoidType()
