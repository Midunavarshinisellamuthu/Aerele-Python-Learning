from calculator import divide


def test_divide():
    a = 20
    b = 4
    res = divide(a, b)
    assert res == 5
