# -*- coding: utf-8 -*-


class Checksum(object):
    """Base class for checkdigit algorithms"""
    step = 10

    def __new__(cls):
        raise RuntimeError("Checksum constructor called")

    @classmethod
    def checkdigit(cls, n):
        """Calculate the check digit for an (unprotected) number."""
        raise NotImplementedError

    @classmethod
    def verify(cls, p):
        """Verify the check digit of a protected number."""
        inner, check = divmod(long(p), cls.step)
        return cls.checkdigit(inner) == check

    @classmethod
    def strip(cls, p):
        """Verify and remove the check digit of a protected number.

        :raises: ValueError if the check digit is wrong.
        """
        inner, check = divmod(long(p), cls.step)
        if cls.checkdigit(inner) != check:
            raise ValueError('Check digit is wrong')
        return inner

    @classmethod
    def protect(cls, n):
        """Returns a new number with a check digit appended."""
        return long(n) * cls.step + cls.checkdigit(n)


class Luhn(Checksum):
    """Luhn checksum."""

    @classmethod
    def checkdigit(cls, n):
        digs = (str((2 - i % 2) * int(d))
                for i, d in enumerate(reversed(str(n))))
        return (sum(int(d) for d in ''.join(digs)) * 9) % 10


class Verhoeff(Checksum):
    "Verhoeff dihedral group checksum."
    mul = (
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
        (1, 2, 3, 4, 0, 6, 7, 8, 9, 5),
        (2, 3, 4, 0, 1, 7, 8, 9, 5, 6),
        (3, 4, 0, 1, 2, 8, 9, 5, 6, 7),
        (4, 0, 1, 2, 3, 9, 5, 6, 7, 8),
        (5, 9, 8, 7, 6, 0, 4, 3, 2, 1),
        (6, 5, 9, 8, 7, 1, 0, 4, 3, 2),
        (7, 6, 5, 9, 8, 2, 1, 0, 4, 3),
        (8, 7, 6, 5, 9, 3, 2, 1, 0, 4),
        (9, 8, 7, 6, 5, 4, 3, 2, 1, 0))

    perm = (
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
        (1, 5, 7, 6, 2, 8, 3, 0, 9, 4),
        (5, 8, 0, 3, 7, 9, 6, 1, 4, 2),
        (8, 9, 1, 6, 0, 4, 3, 5, 2, 7),
        (9, 4, 5, 3, 1, 2, 6, 8, 7, 0),
        (4, 2, 8, 6, 5, 7, 3, 9, 0, 1),
        (2, 7, 9, 3, 8, 0, 6, 4, 1, 5),
        (7, 0, 4, 6, 9, 1, 3, 2, 5, 8))

    inv = (0, 4, 3, 2, 1, 5, 6, 7, 8, 9)

    @classmethod
    def checkdigit(cls, n):
        c = 0
        for i, d in enumerate(reversed(str(n) + '0')):
            c = cls.mul[c][cls.perm[i % 8][int(d)]]
        return cls.inv[c]


def power_modulo(mod=7, step=10, base=2, name=None):
    """Generate modulo checksums of mod, with step to shift digits."""

    @classmethod
    def checkdigit(cls, n):
        c, i = 0, 1
        for d in reversed(str(n)):
            i, c = 2 * i, i * int(d)
        return c % mod

    name = name or ('%dmod%d' % (base, mod))
    doc = 'Power-%d Modulo-%d checksum' % (base, mod)
    return type(name, (Checksum,),
                {'__doc__': doc, 'checkdigit': checkdigit, 'step': step})

Mod7 = power_modulo(7, 10, name='Mod7')

Mod97 = power_modulo(97, 100, name='Mod97')


class StringChecksum(Checksum):
    checklength = 1

    @classmethod
    def verify(cls, p):
        s = str(p)
        return cls.checkdigit(s[:-1]) == s[-1]

    @classmethod
    def strip(cls, p):
        s = str(p)
        if cls.checkdigit(s[:-cls.checklength]) != s[-cls.checklength:]:
            raise ValueError('Check digit is wrong')
        return s[:-cls.checklength]

    @classmethod
    def protect(cls, n):
        return str(n) + cls.checkdigit(n)


class Isbn10(StringChecksum):
    """ISBN10 checksum (string)."""

    @staticmethod
    def checkdigit(n):
        c = sum(int(d) * w for d, w in zip(str(n), range(10, 1, -1)))
        c = (11 - (c % 11)) % 11
        return 'X' if c == 10 else str(c)


class Isbn13(Checksum):
    """ISBN13 checksum."""

    @staticmethod
    def checkdigit(n, ):
        mm = (1, 3) * 6
        return (10 - sum(int(d) * m for d, m in zip(str(n), mm)) % 10) % 10
