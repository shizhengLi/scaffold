from hello import add


def test_add():
    assert add(1, 2) == 3


def test_add_with_nagetive_number():
    assert add(1, -1) == 0
