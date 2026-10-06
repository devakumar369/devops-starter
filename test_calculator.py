from calculator import add, subtract, multiply, divide
def test_add():
    assert add(2, 3) == 5 # nosec B101
def test_subtract():
    assert subtract(10, 4) == 6 # nosec B101
def test_multiply():
    assert multiply(5, 3) == 15 # nosec B101
def test_divide():
    assert divide(10, 2) == 5 # nosec B101
def test_divide_by_zero():
    assert divide(10, 0) == "Cannot divide by zero" # nosec B101