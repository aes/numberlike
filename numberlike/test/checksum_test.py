# -*- coding: utf-8 -*-
from random import randint
from numberlike.checksum import Luhn, Verhoeff, Mod7, Mod97, Isbn10
from numberlike.test.common import assert_raises
# FIXME: Isbn13


class TestLuhn(object):
    data = (
        (0, 0, 0),  # 10 - 0
        (1, 8, 18),  # 10 - 2*1
        (2, 6, 26),  # 10 - 2*2
        (10, 9, 109),  # 10 - (1*1 + 2*0)
        (11, 7, 117))  # 10 - (1*1 + 2*1)

    # obvious mutations of the above
    fail_data = (3, 17, 23, 104, 112, '5', '0004', '14', '23', '101', '112')

    def test_checkdigit(self):
        def check(n, c):
            print (n, c)
            assert Luhn.checkdigit(n) == c

        for n, c, z in self.data:
            yield check, n, c
            yield check, str(n), c

    def test_verify(self):
        def check(n, x):
            print (n, x)
            assert Luhn.verify(n) == x

        for n, c, z in self.data:
            yield check, z, True

        for n in self.fail_data:
            yield check, n, False

    def test_strip(self):
        def check(n, x):
            print (n, x)
            assert Luhn.strip(n) == x

        for n, c, z in self.data:
            yield check, z, n

        for n in self.fail_data:
            yield assert_raises, ValueError, Luhn.strip, (n,), {}

    def test_protect(self):
        def check(n, x):
            print (n, x)
            assert Luhn.protect(n) == x

        for n, c, z in self.data:
            yield check, n, z

    def test_roundtrip(self):
        for i in range(1000):
            Luhn.strip(Luhn.protect(randint(0, 2 ** 32 - 1)))


class TestVerhoeff(object):
    data = (
        (142857, 0, 1428570),
        )

    def test_canon(self):
        def check(n, z):
            print (n, z, Verhoeff.protect(n))
            assert Verhoeff.protect(n) == z
        for n, c, z in self.data:
            yield check, n, z

    def test_roundtrip(self):
        for i in range(1000):
            Verhoeff.strip(Verhoeff.protect(randint(0, 2 ** 32 - 1)))


class TestMod(object):
    def test_roundtrip(self):
        for csum in (Mod7, Mod97):
            for i in range(1000):
                x = randint(0, 2 ** 32 - 1)
                print (csum, x)
                csum.strip(csum.protect(x))


class TestISBN10(object):
    data = (
        ('030640615', '2', '0306406152'),
        )

    def test_canon(self):
        def check(n, z):
            print (n, z, Isbn10.protect(n))
            assert Isbn10.protect(n) == z
        for n, c, z in self.data:
            yield check, n, z

    def test_roundtrip(self):
        for i in range(1000):
            x = randint(0, 2 ** 32 - 1)
            print (x)
            Isbn10.strip(Isbn10.protect(x))


class TstISBN10(object):
    data = (
        ('030640615', '2', '0306406152'),
        )

    def test_canon(self):
        def check(n, z):
            print (n, z, Isbn10.protect(n))
            assert Isbn10.protect(n) == z
        for n, c, z in self.data:
            yield check, n, z

    def test_roundtrip(self):
        for i in range(1000):
            Isbn10.strip(Isbn10.protect(randint(0, 2 ** 32 - 1)))
