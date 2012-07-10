
from numberlike.semver import semver


class TestSemVer(object):
    def strings(self):
        for major in '01':
            for minor in '02':
                for patch in '03':
                    for alpha in ('-rc', '-rc.4', ''):
                        for build in ('', '+harden', '+harden.5'):
                            s = '.'.join((major, minor, patch))
                            s = ''.join((s, alpha, build))
                            yield s

    def test_ctor(self):
        def ctor(al, kw):
            print al, kw
            semver(*al, **kw)
        for major in '01':
            for minor in '02':
                for patch in '03':
                    for alpha in ('rc', 'rc.4', ('rc', '4'), None):
                        for build in ('harden.5', ('harden', '5'), None):
                            it = '.'.join((major, minor, patch))
                            yield ctor, (), {
                                'major': major,
                                'minor': minor,
                                'patch': patch,
                                'alpha': alpha,
                                'build': build}
                            if isinstance(alpha, tuple):
                                it = it + '-' + '.'.join(alpha)
                            if isinstance(build, tuple):
                                it = it + '+' + '.'.join(build)
                            yield ctor, (it,), {}

    def test_repr_a(self):
        assert (repr(semver('1.2.3-cat.dog+god')) ==
                "semver(1, 2, 3, ('cat', 'dog'), ('god',))")

    def test_repr_b(self):
        print repr(semver('1.2.3-cat.4+5.god'))
        assert (repr(semver('1.2.3-cat.4+5.god')) ==
                "semver(1, 2, 3, ('cat', 4), (5, 'god'))")

    def test_repr_eval(self):
        def repr_eval(v):
            print v
            assert eval(repr(v)) == v
        for s in self.strings():
            yield repr_eval, semver(s)

    def test_str_same(self):
        def str_same(v):
            print v
            assert semver(str(v)) == v
        for s in self.strings():
            yield str_same, semver(s)

    def test_cmp(self):
        def lt(n, o):
            assert o < n

        def le(n, o):
            assert o <= n and n <= n

        def ge(n, o):
            assert n >= n and n >= o

        def gt(n, o):
            assert n >= o

        for p, c in (('<', lt), ('<=', le), ('>=', ge), ('>', gt)):
            o = None
            for n in self.strings():
                n = semver(n)
                print n, p, o
                yield c, n, o
                o = n

    def test_cmp_canon_2(self):
        assert semver('1.9.0') < semver('1.10.0') < semver('1.11.0')

    def test_cmp_canon_3(self):
        assert (semver('1.1.3') < semver('2.0.0') and
                semver('2.1.7') < semver('2.2.0'))

    def test_in(self):
        def tin(a, b, x):
            print a, b, x
            assert (semver(a) in semver(b)) == x

        def acc(a, b, x):
            print a, b, x
            assert semver(b).accept(semver(a)) == x

        for f in (tin, acc):
            for a, b, x in (('2.3.1', '2.3.1', True),
                            ('2.3.1-alpha', '2.3.1', False),
                            ('2.3.1+build', '2.3.1', True),
                            ('1.10.0', '1.9.0', True),
                            ('1.9.0', '1.10.0', False),
                            ('2.1.0', '1.0.0', False),
                            ('2.1.0', '2.0.0', True),
                            ):
                yield f, a, b, x

    def test_add(self):
        def add_gt(a, b):
            print a, b
            assert a < a + b

        def add_lt(a, b):
            print a, b
            assert a > a + b

        for a, b in ((semver('2.3.4'), semver('0.0.1')),
                     (semver('2.3.4'), semver('0.1.0')),
                     (semver('2.3.4'), semver('1.0.0')),
                     (semver('2.3.4'), semver('0.0.0', build=('build',))),
                     (semver('2.3.4'), '0.0.1'),
                     (semver('2.3.4'), '0.1.0'),
                     (semver('2.3.4'), '1.0.0'),
                     (semver('2.3.4'), 'build'),
                     ):
            yield add_gt, a, b

        for a, b in ((semver('2.3.4'), semver('0.0.0', alpha='1')),
                     (semver('2.3.4'), semver('0.0.0', alpha='rc')),
                     (semver('2.3.4'), semver('0.0.0', alpha='rc.1'))):
            yield add_lt, a, b

    def test_add_reset_patch(self):
        assert (semver('2.3.4') + semver('0.1.0')).patch == 0

    def test_add_reset_minor_and_patch(self):
        v = semver('2.3.4') + semver('1.0.0')
        assert v.minor == 0 and v.patch == 0

    def test_sub(self):
        def sub_lt(a, b):
            print a, b
            assert a > a - b

        def sub_gt(a, b):
            print a, b
            assert a < a - b

        for a, b in ((semver('2.3.4'), semver('0.0.1')),
                     (semver('2.3.4'), semver('0.1.0')),
                     (semver('2.3.4'), semver('1.0.0')),
                     (semver('2.3.4+build'), semver(0, 0, 0, (), ('build',))),
                     (semver('2.3.4'), '0.0.1'),
                     (semver('2.3.4'), '0.1.0'),
                     (semver('2.3.4'), '1.0.0'),
                     (semver('2.3.4+build'), 'build'),
                     (semver('2.3.4-rc.1'), semver('0.0.0', alpha='rc')),
                     ):
            yield sub_lt, a, b

        for a, b in ((semver('2.3.4-1'), semver('0.0.0', alpha='1')),
                     (semver('2.3.4-rc'), semver('0.0.0', alpha='rc')),
                     (semver('2.3.4-rc.1'), semver('0.0.0', alpha='rc.1'))):
            yield sub_gt, a, b
