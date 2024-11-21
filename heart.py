import math
from turtle import *
def hearta(k):
     return 15* math.sin(k)**3

def heartb(k):
     return 12* math.cos(k) - math.cos (2* k) -2 *math.cos(3*k) - math.cos(4*k)
speed(0)
bgcolor("black")

for i in range(10000):
      x=hearta(i) * 20
      y=heartb(i) * 20
      goto(x, y)
      color("blue")
      penup()
      goto(0,0)
      pendown()
      color("blue")
      write("s",font=("Arial",40,"bold"))
      done()
