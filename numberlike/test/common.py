

def raises(exc, fun, *al, **kw):
    try:
        e, _ = None, fun(*al, **kw)
    except Exception, e:
        pass
    return isinstance(e, exc) and e


def assert_raises(exc, fun, al=None, kw=None):
    assert raises(exc, fun, *(al or []), **(kw or {}))


class StringRoundTrip(object):
    def string_checks(self, cls, seq):
        def repr_eval_check(c, a):
            x = cls(arg)
            assert x == eval(repr(x), {c.__name__: c})

        def str_ctor_check(c, a):
            x = cls(arg)
            assert x == c(str(x))

        def str_same_check(c, a):
            x = cls(arg)
            assert str(x) == str(c(str(x)))

        for arg in seq:
            yield lambda c, a: repr(c(a)), cls, arg
            yield lambda c, a: str(c(a)), cls, arg
            yield repr_eval_check, cls, arg
            yield str_ctor_check, cls, arg
            yield str_same_check, cls, arg

    def test_strings(self):
        for c in self.string_checks(self.cls, self.good):
            yield c


class Comparisons(object):
    def comparison_checks(self, cls, seq):
        def lt(n, o):
            assert o < n

        def le(n, o):
            assert o <= n and n <= n

        def ge(n, o):
            assert n >= n and n >= o

        def gt(n, o):
            assert n > o

        o = None
        for n in seq:
            n = cls(n)
            for c in lt, le, ge, gt:
                yield c, n, o
            o = n

    def test_cmp(self):
        for c in self.comparison_checks(self.cls, self.good):
            yield c


class BooleanLogic(object):
    def boolean_checks(self, true, false):
        def _f(f, t):           assert not f
        def _t(f, t):           assert t
        def _or(f, t):          assert t or True
        def _and(f, t):         assert t and True
        def _ror(f, t):         assert True or t
        def _rand(f, t):        assert True and t
        def _coerce_t(f, t):    assert bool(f)
        def _coerce_f(f, t):    assert not bool(f)
