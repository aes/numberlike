
from numberlike.iso import iso3166, iso7812
from numberlike.test.common import raises, assert_raises, StringRoundTrip


class TestIso3166(StringRoundTrip):
    _m = {
        2:   ('AW', 'AWW', "Kittens, People's Reposts of"),
        34:  ('FB', 'FRB', "Frobnia, I AM FROBNIA"),
        456: ('WZ', 'WAZ', "Wazland")}

    def setup(self):
        self._k, iso3166._known = iso3166._known, dict(self._m)

    def teardown(self):
        self._k, iso3166._known = iso3166._known, self._k

    def test_ctor_good(self):
        assert iso3166(2)

    def test_ctor_bad(self):
        assert raises(Exception, iso3166, 5)

    def test_ctor_equiv(self):
        assert set(iso3166(n) for n in ('WZ', 'WAZ', "Wazland")) == set((456,))

    def test_bool_coerce(self):
        assert bool(iso3166(34))

    def test_bool_or(self):
        assert None or iso3166(2)

    def test_bool_or(self):
        assert True and iso3166(456)

    def test_props_name(self):
        def check_name(arg, name):      assert iso3166(arg).name == name
        def check_short(arg, short):    assert iso3166(arg).short == short
        def check_formal(arg, formal):  assert iso3166(arg).formal == formal

        for num, a2, a3, name, short, formal in (
            (2,   'AW', 'AWW', "Kittens, People's Reposts of", "Kittens",
             "People's Reposts of Kittens"),
            (34,  'FB', 'FRB', "Frobnia, I AM FROBNIA", "Frobnia",
             "I AM FROBNIA"),
            (456, 'WZ', 'WAZ', "Wazland", "Wazland", "Wazland")):

            for arg in (num, a2, a3, name):
                yield check_name, arg, name
                yield check_short, arg, short
                yield check_formal, arg, formal

    def test_strings(self):
        for c in self.string_checks(iso3166, (2, 34, 456)):
            yield c

    def test_user_assign(self):
        assert raises(Exception, iso3166, 666)

        iso3166._known[666] = ('XX', 'XXX', 'Hell')

        assert iso3166(666).name == 'Hell'
