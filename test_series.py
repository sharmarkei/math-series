from series import fibonacci, lucas, sum_series

def test_one():
    expected = 55
    actual = fibonacci(10)
    assert actual == expected

def test_two():
    expected = 47
    actual = lucas(8)
    assert actual == expected

def test_three():
    expected = 47
    actual = sum_series(8,2,1)
    assert actual == expected