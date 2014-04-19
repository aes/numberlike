# -*- coding: utf-8 -*-

try:
    string = basestring
except:
    string = str


def radixate(x, radixes):
    magic = 8.3267e-17  # Why? I don't know, but it works to 19 digits
    digits = []
    for radix in radixes:
        scaled = x * radix
        digit = int(scaled)
        x = scaled - digit + magic  # wtf: magic
        digits.append(digit)
    return digits


def digitate(digits, basechars):
    return ''.join(chr(d + ord(b)) for d, b in zip(digits, basechars))


def dedigitate(s, basechars):
    return [ord(c.lower()) - ord(b.lower()) for c, b in zip(s, basechars)]


def radixnum(digits, radixes):
    x = 0.0
    for d, r in reversed(zip(digits, radixes)):
        x = (d + x) / r
    return x


def mls(lat, lon):
    enc = lambda x: digitate(radixate(x, (18, 10, 24, 10, 24)), 'A0a0A')
    xlon = enc((lon + 180) / 360.)
    xlat = enc((lat + 90) / 180.)
    return ''.join(sum(zip(xlon, xlat), ()))


def un_mls(xmls):
    digits = dedigitate(xmls, "AA00aa00AA")
    xlon, xlat = digits[0::2], digits[1::2]
    return (180 * radixnum(xlat, (18, 10, 24, 10, 24)) - 90.,
            360 * radixnum(xlon, (18, 10, 24, 10, 24)) - 180.)
