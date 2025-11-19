#https://github.com/Awesomepop7/lab11-EGL
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)
def exp(a, b):
    return a ** b
