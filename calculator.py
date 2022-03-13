# This app can take multiple numbers and output their calculations


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


# Gets two numbers and the operator, and returns the sum
def calculator():
    x = float(input("FN "))
    o = str(input("O  "))

    # If user inputs "=", the program will just return the sum
    if o == "=":
        return operation(o, x, y=0)

    while o != "=":
        y = float(input("SN"))
        x = operation(o, x, y)

        print("sum: ", x)
        o = str(input("O2 "))
        y = float(input())

    return operation(o, x, y)


# TO-DO: Take multiple entries
# Takes two numbers and the operator. It then prints the calculation (x _ y = sum), before returning the sum
def operation(f, x, y):
    match f:
        case "+":
            print(x, "+", y, "=", end=" ")
            return add(x, y)
        case "-":
            print(x, "-", y, "=", end=" ")
            return subtract(x, y)
        case "*":
            print(x, "*", y, "=", end=" ")
            return multiply(x, y)
        case "/":
            print(x, "/", y, "=", end=" ")
            return divide(x, y)
        case "^":
            print(x, "^", y, "=", end=" ")
            return pow(x, y)
        case _:
            print(x, "=", end=" ")
            return x


flag = 1

while flag != 0:
    print(calculator())
    flag = float(input("Continue? (0) "))
