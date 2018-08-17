from .func import func_add, func_sub


def func(x):
    return x+1


def test_anwser():
    assert func(3) == 4


def test_add():
    assert func_add(3, 2) == 5


def test_sub():
    assert func_sub(3, 2) == 1
