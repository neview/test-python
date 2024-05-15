# 绘制四边形
# import turtle
# turtle.pensize(4) # 像素 4
# turtle.pencolor('red') # 颜色 红色
#
# turtle.forward(100) # 沿X轴运动
# turtle.right(90) # 旋转 90度
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(45)
# turtle.backward(200)
#
# turtle.mainloop() # 启动动画


# 绘制小猪佩奇
from turtle import *


def nose(x, y):
    """画鼻子"""
    penup()  # 抬起画笔，使得turtle移动时不留下轨迹,相当于在现实生活中提起画笔或铅笔，不接触纸张。
    goto(x, y)  # 将turtle立即移动到坐标为 (x, y) 的位置,不论当前画笔状态如何（提起或放下），都会直接跳转到指定坐标
    pendown()  # 将turtle的画笔放下，之后的移动将会在画布上留下痕迹，相当于在纸上落笔开始绘图。
    setheading(-30)  # 设置turtle当前面向的方向，角度参数可以是0-360度之间的整数或浮点数，其中0代表正东，90代表正北，180代表正西，270代表正南。
    begin_fill()  # 标记填充区域的开始，配合end_fill()使用，可以填充由turtle路径包围的区域。
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 30 <= i < 90: # or 或者
            a = a + 0.08
            left(3)  # 使turtle左转或右转指定的角度值，改变turtle的行进方向
            forward(a)  # 用于控制turtle向前移动指定的距离
        else:
            a = a - 0.08
            left(3)
            forward(a)
    end_fill()
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    # 设置画笔的颜色（红，绿，蓝）
    pencolor(255, 155, 192)  # 设置turtle画笔的颜色，接受RGB三元组作为参数，如(255, 155, 192)为一种粉色。
    setheading(10)
    begin_fill()
    circle(5)  # 绘制一个半径为radius的圆形。
    color(160, 82, 45)  # 设置线条颜色（若没有filling()则影响轮廓）或填充颜色，这里看起来可能是个笔误，因为在begin_fill()和end_fill()之间应使用fillcolor()来更改填充色。
    end_fill()
    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()


def setting():
    """设置参数"""
    pensize(4)
    # 隐藏海龟
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(10)


def main():
    """主函数"""
    setting()
    nose(-100, 100)
    # head(-69, 167)
    # ears(0, 160)
    # eyes(0, 140)
    # cheek(80, 10)
    # mouth(-20, 30)
    done()

main()