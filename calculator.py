# This app can take multiple numbers and output their calculations

x = float(input("First Number: "))
y = float(input("Second Number: "))


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def pow(x, y):
    return x**y


print(x, " + ", y, " = ", add(x, y))
