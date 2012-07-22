
from numberlike.isbn import ISBN, ISBN10, ISBN13
from numberlike.test.common import raises, assert_raises
from numberlike.test.common import StringRoundTrip, Comparisons, Constructor


class ISBNt(ISBN):
    class _checksum:
        verify = classmethod(lambda *al: True)


class TestISBN(object):
    def test_ctor_good(self):
        assert ISBNt('01234')

    def test_ctor_bad(self):
        assert raises(Exception, ISBNt, (0,))


class Common(StringRoundTrip, Comparisons, Constructor):
    def test_cmp(self):
        for c in self.comparison_checks(self.cls, self.good[:3]):
            yield c


class TestISBN10(Common):
    cls = ISBN10

    good = (
        '917-448-512-1',
        '917-448-513-X',
        '917-448-514-8',
        '917-448-513-',
        '917-448-513',
        '917448513-X',
        '917448513-',
        '917448513')

    bad = (
        '',
        '12345345',
        '91-7448-512-X',
        '91--7448513',
        '91--7448513-X',
        '91-7448513-X')


class TestISBN13(Common):
    cls = ISBN13

    good = (
        '978-91-7448-512-7',
        '978-91-7448-513-4',
        '978-91-7448-514-1',
        '978-91-7448-512-',
        '978-91-7448-512',
        )

    bad = (
        '',
        '97891-7448512-6',
        '978-91-7448-512-6',
        '978-91-7448-513-6',
        )
