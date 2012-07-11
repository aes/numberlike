# -*- coding: utf-8 -*-

class nonarithmetic(object):
    """Base class to forbid arithmetic operations.

    The purpose of this is to ensure that code numbers are not accidentally
    included in calculations.

    Notice that some "sensible" operations are still permitted:

    * and, nonzero, or, rand, ror
    * hex, oct
    * coerce, float, int, long
    * cmp, mod, pos, rmod
    * getnewargs, index
    """
    pass


def _setup():
    score = """\
        abs add div divmod floordiv invert lshift mul neg pow radd rdiv
        rdivmod rfloordiv rlshift rmul rpow rrshift rshift rsub rtruediv rxor
        sub truediv trunc xor"""
    plain = 'conjugate denominator imag numerator real'


    for s in score.split():
        q = s
        def raiser(*al, **kw):
            raise ArithmeticError('Arithmetic on code: __%s__' % q, q)
        setattr(nonarithmetic, "__%s__" % s, raiser)

    for p in plain.split():
        q = p
        def raiser(*al, **kw):
            raise ArithmeticError('Arithmetic on code: %s' % q, q)
        setattr(nonarithmetic, p, raiser)

    global _setup
    del _setup

_setup()
