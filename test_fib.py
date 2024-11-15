from fib import fibonacci_recursive, fibonacci_iterative
import pytest

def test_fib_rec_9_is_34():
    expected = 34
    result = fibonacci_recursive(9)
    assert expected == result
def test_fib_rec_10_is_55():
    expected = 55
    result = fibonacci_recursive(10)
    assert expected == result
def test_fib_rec_0_is_0():
    expected = 0
    result = fibonacci_recursive(0)
    assert expected == result
def test_fib_rec_1_is_1():
    expected = 1
    result = fibonacci_recursive(1)
    assert expected == result
def test_fib_rec_negative_raise_error():
     with pytest.raises(ValueError):
        fibonacci_recursive(-1)



def test_fib_it_9_is_34():
    expected = 34
    result = fibonacci_iterative(9)
    assert expected == result
def test_fib_it_10_is_55():
    expected = 55
    result = fibonacci_iterative(10)
    assert expected == result
def test_fib_it_0_is_0():
    expected = 0
    result = fibonacci_iterative(0)
    assert expected == result
def test_fib_it_1_is_1():
    expected = 1
    result = fibonacci_iterative(1)
    assert expected == result
def test_fib_it_negative_raise_error():
     with pytest.raises(ValueError):
        fibonacci_iterative(-1)
