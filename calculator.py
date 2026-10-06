def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("2 + 3 =", add(2, 3))
print("10 - 4 =", subtract(10, 4))
print("5 * 3 =", multiply(5, 3))
print("10 / 2 =", divide(10, 2))