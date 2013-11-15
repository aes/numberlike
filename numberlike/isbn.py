# -*- coding: utf-8 -*-
from numberlike import checksum

try:
    string = basestring
except:
    string = str


class ISBN(tuple):
    pattern = (r'((?:(?P<ean>\d+)-?)?((?P<group>\d+)-?(?P<publisher>\d+)'
               r'-?(?P<title>\d+)-?(?P<check>[0-9X]))')

    EAN, GROUP, PUBLISHER, TITLE, CHECK = 0, 1, 2, 3, 4

    ean = property(lambda s: s[s.EAN])

    group = property(lambda s: s[s.GROUP])

    publisher = property(lambda s: s[s.PUBLISHER])

    title = property(lambda s: s[s.TITLE])

    check = property(lambda s: s[s.CHECK])

    def __repr__(self):
        return '%s("%s")' % (self.__class__.__name__, str(self))

    def __str__(self):
        return '-'.join(it for it in self if it)

    def __new__(cls, egptc):
        if cls == ISBN:
            pass

        if len(egptc) != 5:
            raise ValueError('Wrong length for ISBN tuple')
        else:
            c = egptc[-1]

        if not all(x.isdigit() for x in egptc[:-1] if x is not None):
            raise ValueError('Non-digit ISBN code part')

        if len(c) != 1:
            raise ValueError("More than one character in ISBN check part")

        if not cls._checksum.verify(''.join(x for x in egptc if x)):
            raise ValueError("ISBN checksum failed")

        return super(ISBN, cls).__new__(cls, egptc)


class ISBN10(ISBN):
    _checksum = checksum.Isbn10

    def __new__(cls, a):
        s = str(a)
        x = ''.join(c for c in s if 48 <= ord(c) <= 57 or c == 'X')

        if len(x) == 9:
            x = checksum.Isbn10.protect(x)
            s = s + ('-' if s[-1] != '-' and '-' in s else '') + x[-1]
        elif len(x) != 10:
            raise ValueError("Wrong length for ISBN-10")

        l = s.split('-')

        if len(l) == 4:
            l = [None] + l

        elif len(l) == 2:
            l = [None, None, None] + l[:2]

        elif len(l) == 1:
            l = [None, None, None, x[:-1], x[-1]]

        else:
            raise ValueError("Wrong ISBN-10 separator pattern")

        return super(ISBN10, cls).__new__(cls, l)


class ISBN13(ISBN):
    _checksum = checksum.Isbn13

    def __new__(cls, a):
        s = str(a)
        x = ''.join(c for c in s if 48 <= ord(c) <= 57)

        if len(x) == 12:
            d = checksum.Isbn13.checkdigit(x)
            s = s + ('-' if s[-1] != '-' and '-' in s else '') + str(d)
        elif len(x) != 13:
            raise ValueError("Wrong length for ISBN-13")

        l = s.split('-')
        if len(l) == 5:
            if not all(x.isdigit() for x in l):
                raise ValueError("Non-digit ISBN code part")

            if l[-1] not in '0123456789':
                raise ValueError("Strange ISBN-13 check digit")

        elif len(l) == 2:
            l = None, None, None, l[0], l[1]

        elif len(l) == 1:
            l = None, None, None, x[:-1], x[-1]

        return super(ISBN13, cls).__new__(cls, l)
