# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from . import parametric
from . import eq, neq, lt, le, ge, gt, raises, call, ok


def test():
    class Base1: pass

    class Base2: pass

    @parametric
    class A(Base1, object): pass

    yield ok, issubclass(A, Base1)
    yield ok, not issubclass(A, Base2)

    yield ok, A(1) == A(1)
    yield ok, A(2) == A(2)
    yield ok, A(1) != A(2)

    a1 = A(1)()
    a2 = A(2)()

    yield ok, type(a1) == A(1)
    yield ok, type(a2) == A(2)
    yield ok, isinstance(a1, A(1))
    yield ok, not isinstance(a1, A(2))
    yield ok, issubclass(type(a1), A)
    yield ok, issubclass(type(a1), Base1)
    yield ok, not issubclass(type(a1), Base2)

    # Test multiple type parameters and hashability.
    yield ok, A(1, 2) == A(1, 2)
    yield raises, TypeError, lambda: A({})


def test_argument():
    @parametric
    class A:
        def __init__(self, x):
            self.x = x

    a = A(1)(5.)

    yield eq, a.x, 5.
