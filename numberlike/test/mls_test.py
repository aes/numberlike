# -*- coding: utf-8 -*-
from numberlike import mls
#from numberlike.test.common import raises


class TestRadixate(object):
    def test_examples(self):
        def check(x, r, y):
            z = mls.radixate(x, r)
            assert z == y, "x: %r, r: %r, \ny: %r => \nz: %r" % (x, r, y, z)
        for num, radixes, digits in (
                (0.1234, (10,) * 4, [1, 2, 3, 4]),
                (0.9876, (10,) * 4, [9, 8, 7, 6]),
                (1/3.,   (10,) * 4, [3, 3, 3, 3]),
                (1/4.,   (10,) * 4, [2, 5, 0, 0]),
                (1/5.,   (10,) * 4, [2, 0, 0, 0]),
                (1/6.,   (10,) * 16, [1] + [6] * 15),
                (1/11.,  (10,) * 16, [0, 9] * 8),
                (1/3.,   (1000,) * 5, [333] * 5),
                (0.1234567890123456789, (10,) * 19,
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ):
            yield check, num, radixes, digits


class TestDigitate(object):
    def test_examples(self):
        def check(d, r, expect):
            z = mls.digitate(d, r)
            msg = "d: %r, r: %r => %r != expected: %r" % (d, r, z, expect)
            assert z == expect, msg
        for digits, radixes, result in (
                ((0, 0, 0, 0), '@@@@', '@@@@'),
                ((1, 2, 3, 4), '@@@@', 'ABCD'),
                ((23, 24, 25, 0), 'aaaa', 'xyza'),
        ):
            yield check, digits, radixes, result


class TestMLS(object):
    def test_examples(self):
        def check(lat, lon, code):
            z = mls.mls(lat, lon)
            msg = "lat: %r, lon: %r, code: %r != %r" % (lat, lon, code, z)
            assert z == code, msg
        for lat, lon, code in (
                (59.312071,  18.034916, "JO99ah44EV"),
                (59.312099,  18.035667, "JO99ah44GV"),
                (14.525090, 121.073791, "PK04mm86UA"),
                (46.765019, -93.280021, "EN36is63JO"),
        ):
            yield check, lat, lon, code
