

def raises(exc, fun, *al, **kw):
    try:
        e, _ = None, fun(*al, **kw)
    except Exception, e:
        pass
    return type(e) == exc


def assert_raises(exc, fun, al, kw):
    assert raises(exc, fun, *al, **kw)
