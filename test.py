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


import asyncio
import math
import unittest

from void import Void


class TestVoid(unittest.TestCase):
    def test_hash(self):
        self.assertEqual(hash(Void), hash(None))

    def test_bool(self):
        self.assertFalse(Void)

    def test_len(self):
        self.assertEqual(len(Void), 0)

    def test_equal(self):
        self.assertEqual(Void, 0)
        self.assertEqual(Void, [])
        self.assertEqual(Void, '')

    def test_not_equal(self):
        self.assertNotEqual(Void, 1)
        self.assertNotEqual(Void, 42)
        self.assertNotEqual(Void, -743.8)
        self.assertNotEqual(Void, 'x')
        self.assertNotEqual(Void, ['x'])

    def test_less_or_equal(self):
        self.assertTrue(Void <= None)
        self.assertTrue(Void <= False)
        self.assertTrue(Void <= [])
        self.assertTrue(Void <= 0)
        self.assertTrue(Void <= 17)
        self.assertFalse(Void <= -1)
        self.assertFalse(Void <= 'x')
        # because True is 1 and Void is 0
        self.assertTrue(Void <= True)

    def test_greater_or_equal(self):
        self.assertTrue(Void >= None)
        self.assertTrue(Void >= False)
        self.assertTrue(Void >= [])
        self.assertTrue(Void >= 0)
        self.assertTrue(Void >= -17)
        self.assertFalse(Void >= 1)
        self.assertFalse(Void >= 'x')
        # because True is 1 and Void is 0
        self.assertFalse(Void >= True)

    def test_greater_than(self):
        self.assertTrue(Void > -17)
        self.assertFalse(Void > 0)
        self.assertFalse(Void > 1)
        # fails for not strictly mathematical comparisons
        with self.assertRaises(TypeError):
            Void > []
        with self.assertRaises(TypeError):
            Void > None

    def test_less_than(self):
        self.assertFalse(Void < -17)
        self.assertFalse(Void < 0)
        self.assertTrue(Void < 1)
        # fails for not strictly mathematical comparisons
        with self.assertRaises(TypeError):
            Void < []
        with self.assertRaises(TypeError):
            Void < None

    def test_call(self):
        self.assertIsNone(Void('x', 'y', foo='bar'))

    def test_getitem(self):
        self.assertIsNone(Void['x'])
        self.assertIsNone(Void[17])

    def test_getattr(self):
        self.assertIsNone(Void.jnfknjg)

    def test_setitem(self):
        Void['dfgdgd'] = 'fgfdbfdbgfb'
        Void[0] = 'gfdfgfd'
        Void[18] = 'gfdfgfd'

    def test_setattr(self):
        Void.dkjfgndkgjnkdfgn = 'kmdflgkmfdlgmkl'

    def test_delitem(self):
        del Void['ou9jgrg']
        del Void[45]

    def test_delattr(self):
        del Void.fdgdfgdfdf934

    def test_complex(self):
        self.assertEqual(complex(Void), complex(0, 0))

    def test_float(self):
        self.assertEqual(float(Void), 0.0)

    def test_int(self):
        self.assertEqual(int(Void), 0)

    def test_round(self):
        self.assertEqual(round(Void), 0)

    def test_trunc(self):
        self.assertEqual(math.trunc(Void), 0)

    def test_floor(self):
        self.assertEqual(math.floor(Void), 0)

    def test_ceil(self):
        self.assertEqual(math.ceil(Void), 0)

    def test_str(self):
        self.assertEqual(str(Void), 'Void')
        self.assertEqual('{0}'.format(Void), 'Void')

    def test_repr(self):
        self.assertEqual(repr(Void), 'Void')

    def test_format(self):
        self.assertEqual(format(Void, '^6'), ' Void ')

    def test_context(self):
        init_value = 'some value'
        never_changed = init_value

        with Void as eternal_nothingness:
            eternal_nothingness.anything
            never_changed = 'getattr failed to fail'

        with Void as silence:
            silence()
            never_changed = 'call failed to fail'

        with Void as devourer:
            raise Exception('this should always get eaten')

        self.assertEqual(never_changed, init_value)

    async def _run_async_context(self):
        init_value = 'some async value'
        never_changed = init_value

        async with Void as eternal_nothingness:
            eternal_nothingness.anything
            never_changed = 'getattr failed to fail'

        async with Void as silence:
            silence()
            never_changed = 'call failed to fail'

        async with Void as devourer:
            raise Exception('this should always get eaten')

        self.assertEqual(never_changed, init_value)

    def test_async_context(self):
        asyncio.run(self._run_async_context())

    def test_iter(self):
        init_value = 'some value'
        never_changed = init_value

        for x in Void:
            never_changed = 'failed to not iter'

        self.assertEqual(never_changed, init_value)

    def test_reversed(self):
        init_value = 'some value'
        never_changed = init_value

        for x in reversed(Void):
            never_changed = 'failed to not reverse iter'

        self.assertEqual(never_changed, init_value)

    def test_bytes(self):
        self.assertEqual(bytes(Void), b'')

    def test_contains(self):
        self.assertNotIn('x', Void)
        self.assertNotIn(None, Void)

    async def _run_coroutine(self):
        await Void

    def test_coroutine(self):
        asyncio.run(self._run_coroutine())

    async def _run_aiter(self):
        init_value = 'some value'
        never_changed = init_value

        async for x in Void:
            never_changed = 'failed to not iter'

        self.assertEqual(never_changed, init_value)

    def test_aiter(self):
        asyncio.run(self._run_aiter())

    def test_add(self):
        self.assertIsNone(Void + 'x')
        self.assertIsNone(Void + 434543)
        self.assertIsNone(Void + [])

    def test_sub(self):
        self.assertIsNone(Void - 'x')
        self.assertIsNone(Void - 3242)
        self.assertIsNone(Void - {})

    def test_mul(self):
        self.assertIsNone(Void * 0)
        self.assertIsNone(Void * 'fdss')
        self.assertIsNone(Void * ('abc', 'def'))

    def test_matmul(self):
        self.assertIsNone(Void @ 'dsfsf')

    def test_truediv(self):
        self.assertIsNone(Void / 0)
        self.assertIsNone(Void / 'sdfsd')

    def test_floordiv(self):
        self.assertIsNone(Void // 0)
        self.assertIsNone(Void // {'hello': 'world'})

    def test_mod(self):
        self.assertIsNone(Void % 0)
        self.assertIsNone(Void % ['oat milk', 'broccoli'])

    def test_divmod(self):
        self.assertIsNone(divmod(Void, 0))

    def test_pow(self):
        self.assertIsNone(pow(Void, 17, 342))
        self.assertIsNone(Void ** 2)

    def test_lshift(self):
        self.assertIsNone(Void << 43)

    def test_rshift(self):
        self.assertIsNone(Void >> 12442)

    def test_and(self):
        self.assertIsNone(Void & b'\x0303ERROR\x03 WHY IS THIS CTCP')

    def test_xor(self):
        self.assertIsNone(Void ^ complex(16, 3))

    def test_or(self):
        self.assertIsNone(Void | b'\x00')

    def test_radd(self):
        self.assertIsNone('x' + Void)
        self.assertIsNone(434543 + Void)
        self.assertIsNone([] + Void)

    def test_rsub(self):
        self.assertIsNone('x' - Void)
        self.assertIsNone(3242 - Void)
        self.assertIsNone({} - Void)

    def test_rmul(self):
        self.assertIsNone(0 * Void)
        self.assertIsNone('fdss' * Void)
        self.assertIsNone(('abc', 'def') * Void)

    def test_rmatmul(self):
        self.assertIsNone('dsfsf' @ Void)

    def test_rtruediv(self):
        self.assertIsNone(0 / Void)
        self.assertIsNone('sdfsd' / Void)

    def test_rfloordiv(self):
        self.assertIsNone(0 // Void)
        self.assertIsNone({'hello': 'world'} // Void)

    def test_rmod(self):
        self.assertIsNone(0 % Void)
        self.assertIsNone(['oat milk', 'broccoli'] % Void)

    def test_rdivmod(self):
        self.assertIsNone(divmod(17, Void))

    def test_rpow(self):
        self.assertIsNone(2 ** Void)

    def test_rlshift(self):
        self.assertIsNone(43 << Void)

    def test_rrshift(self):
        self.assertIsNone(12442 >> Void)

    def test_rand(self):
        self.assertIsNone(b'\x0303ERROR\x03 WHY IS THIS CTCP' & Void)

    def test_rxor(self):
        self.assertIsNone(complex(16, 3) ^ Void)

    def test_ror(self):
        self.assertIsNone(b'\x00' | Void)

    def test_iadd(self):
        global Void
        Void += 'foo'

    def test_isub(self):
        global Void
        Void -= 'foo'

    def test_imul(self):
        global Void
        Void *= 'foo'

    def test_imatmul(self):
        global Void
        Void @= 'foo'

    def test_itruediv(self):
        global Void
        Void /= 'foo'

    def test_ifloordiv(self):
        global Void
        Void //= 'foo'

    def test_imod(self):
        global Void
        Void %= 'foo'

    def test_ipow(self):
        global Void
        Void **= 'foo'

    def test_ilshift(self):
        global Void
        Void <<= 'foo'

    def test_irshift(self):
        global Void
        Void >>= 'foo'

    def test_iand(self):
        global Void
        Void &= 'foo'

    def test_ixor(self):
        global Void
        Void ^= 'foo'

    def test_ior(self):
        global Void
        Void |= 'foo'

    def test_neg(self):
        self.assertIs(-Void, Void)

    def test_pos(self):
        self.assertIs(+Void, Void)

    def test_abs(self):
        self.assertIs(abs(Void), Void)

    def test_invert(self):
        self.assertIs(~Void, Void)
