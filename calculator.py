# This app can take multiple numbers and output their calculations

x = float(input())
o = str(input())
y = float(input())


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


# TO-DO: Take multiple entries
def operation(f):
    match f:
        case ("+"):
            print(x, "+", y, "=", add(x, y))
        case ("-"):
            print(x, "-", y, "=", subtract(x, y))
        case ("*"):
            print(x, "*", y, "=", multiply(x, y))
        case ("/"):
            print(x, "/", y, "=", divide(x, y))
        case ("^"):
            print(x, "^", y, "=", pow(x, y))


operation(o)
