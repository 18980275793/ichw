import turtle
import math

def bb(n):
    return float(0.1+0.1*n)

def aa(n):
    return float(20+10*n)

def orbit(n,col):
    a=aa(n)
    b=bb(n)
    u=200
    t=turtle.Pen()
    t.speed(0)
    t.color(col)
    t.pensize(7-n)
    t.penup()
    t.goto(math.cos((150+30*n)*3.14159/u)*a/(1.0-b*math.cos((150+30*n)*3.14159/u)),a*math.sin((150+30*n)*3.14159/u)  /  (1.0-b*math.cos((150+30*n)*3.14159/u)))
    t.pendown()
    for x in range(150+30*n,2*u+n*50):
        t.goto(              math.cos(x*3.14159/u)*a/  (1.0-b*math.cos(x*3.14159/u))             ,a*math.sin(x*3.14159/u)  /  (1.0-b*math.cos(x*3.14159/u))                                   )
        ppp=(150+50*n)
        if x==ppp:
            t.begin_fill()
            t.circle(4)
            t.end_fill()
    t.hideturtle()
    return
               
def main():
    a=turtle.Pen()
    a.penup()
    a.goto(0,-5)
    a.pendown()
    a.color('gold')
    a.begin_fill()
    a.circle(10)
    a.end_fill()
    a.hideturtle()
    COL=['brown','blue','green','red','black','orange','cyan']
    for i in range(1,7):
        orbit(i,COL[i])
    return

main()