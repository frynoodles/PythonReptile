# @coding:UTF-8 
# @program: PythonReptile
# @author: frynoodles
# @created: 2021-01-27 18:52

import turtle


turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80 / 2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
turtle.done()
# 吐槽：梦回小学学的小海龟（忘记是啥软件了）

