from turtle import *


def test():
    penup()
    goto(10, 20)
    pendown()
    a = 0.4
    for i in range(120):
        if 0 < i or 30 < i < 90:
            a = a + 0.08
            left(3)
            forward(a)
        else:
            a = a - 0.08
            left(3)
            forward(a)


test()
