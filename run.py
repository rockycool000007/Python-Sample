import sys

def addNumbers(num1, num2):
    return num1 + num2


def subNumbers(num1, num2):
    return num1 - num2


def mulNumbers(num1, num2):
    return num1 * num2


def divNumbers(num1, num2):
    return num1 / num2

print(addNumbers(int(sys.argv[1]),int(sys.argv[2])))