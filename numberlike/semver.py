# -*- coding: utf-8 -*-

try:
    string = basestring
except:
    string = str


def split_idlist(s):
    if isinstance(s, string):
        s = s.split('.')
    return tuple(isinstance(w, string) and w.isdigit() and int(w) or w
                 for w in s if w != '')


def str_to_tuple(s):
    major, minor, s = s.split('.', 2)
    s, build = (s.split('+', 1) + [''])[:2]
    patch, alpha = (s.split('-', 1) + [''])[:2]
    return (int(major), int(minor), int(patch),
            split_idlist(alpha), split_idlist(build))


class semver(tuple):
    """Implementation of some essential features of Semantic Versioning.

    The Semantic Version homepage is at http://semver.org/

    A semver is immutable and can be constructed in a number of ways:

    1. semver('1.2.3-alpha-a.1+build.1-a')
    2. semver(1, 2, 3, ('alpha-a', 1), ('build', '1-a'))
    3. semver('1.2.3') - 'alpha-a' - 1 + 'build' + '1-a'

    String conversion gives the first and the second is the string
    representation.

    Comparisons consider the presence of an pre-release component to be
    negative, but its contents are compared normally.

    The containment operator ``in`` is implemented to mean "satisfies", so
    that ``semver('1.2.3') in semver('1.2.0')`` but not the converse.
    """

    def __new__(cls, major=0, minor=None, patch=None, alpha=None, build=None):
        if isinstance(major, string) and '.' in major:
            major = str_to_tuple(major)

        if isinstance(major, tuple):
            build = major[4] if build is None and len(major) >= 5 else build
            alpha = major[3] if alpha is None and len(major) >= 4 else alpha
            patch = major[2] if patch is None and len(major) >= 3 else patch
            minor = major[1] if minor is None and len(major) >= 2 else minor
            major = major[0] if major else 0

        major = int(major or 0)
        minor = int(minor or 0)
        patch = int(patch or 0)
        alpha = split_idlist(alpha or ())
        build = split_idlist(build or ())

        return super(semver, cls).__new__(
            cls, (major, minor, patch, alpha, build))

    major = property(lambda s: s[0], doc="Major version component")
    minor = property(lambda s: s[1], doc="Minor version component")
    patch = property(lambda s: s[2], doc="Patch version component")
    alpha = property(lambda s: s[3], doc="Pre-release version extra")
    build = property(lambda s: s[4], doc="Build version extra")

    def __repr__(self):
        return "semver(%d, %d, %d, %r, %r)" % self

    def __str__(self):
        major, minor, patch, alpha, build = self
        return ("%d.%d.%d" % (major, minor, patch) +
                ("-" + '.'.join(str(p) for p in alpha) if alpha else '') +
                ("+" + '.'.join(str(b) for b in build) if build else ''))

    def __cmp__(self, other):
        if not isinstance(other, semver):
            return NotImplemented

        major, minor, patch, alpha, build = self
        return (
            cmp((major, minor, patch),
                (other.major, other.minor, other.patch)) or
            -cmp(bool(alpha), bool(other.alpha)) or
            cmp(alpha, other.alpha) or
            cmp(build, other.build))

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __contains__(self, other):
        if not isinstance(other, semver):
            return NotImplemented

        return self.major == other.major and self <= other

    def accept(self, other):
        return other in self

    def __add__(self, other):
        major, minor, patch, alpha, build = self
        if isinstance(other, semver):
            if other.major:
                return semver(major + other.major, 0, 0)

            elif other.minor:
                return semver(major, minor + other.minor, 0)

            elif other.patch:
                return semver(major, minor, patch + other.patch)

            else:
                return semver(major, minor, patch,
                              alpha + other.alpha, build + other.build)
        elif isinstance(other, string):
            try:  # v + '0.0.1'
                return self + semver(other)
            except:  # v + 'build'
                return semver(major, minor, patch,
                              alpha, build + split_idlist(other))
        elif isinstance(other, int):
            return semver(major, minor, patch, alpha, build + (other,))

        return NotImplemented

    def __sub__(self, other):
        major, minor, patch, alpha, build = self
        if isinstance(other, semver):
            if self.major >= other.major > 0:
                return semver(major - other.major, 0, 0)

            elif self.minor >= other.minor > 0:
                return semver(major, minor - other.minor, 0)

            elif self.patch >= other.patch > 0:
                return semver(major, minor, patch - other.patch)

            elif other.alpha or other.build:
                return semver(major, minor, patch,
                              tuple(p for p in alpha if p not in other.alpha),
                              tuple(b for b in build if b not in other.build))
            else:
                return NotImplemented
        elif isinstance(other, string):
            try:  # v - '0.0.1'
                return self - semver(other)
            except:  # v - 'alpha'
                return semver(major, minor, patch,
                              alpha + split_idlist(other), build)
        elif isinstance(other, int):
            return semver(major, minor, patch, alpha + (other,), build)
