import turtle

## Part 1.1
def koch(t, length):
  if length < 15:
    t.fd(length)
  else:
    koch(t, length / 3)
    t.lt(60)
    koch(t, length / 3)
    t.rt(120)
    koch(t, length / 3)
    t.lt(60)
    koch(t, length / 3)

## Part 1.2
def snowflake(t, length):
  for i in range(3):
    koch(t, length)
    t.rt(120)

## ------ Setup ------
bob = turtle.Turtle()
bob.speed(0)
bob.pu()
bob.setpos(-350, 200)
bob.pd()

## ---- Call only one ----
#koch(bob, 700)
snowflake(bob, 700)

turtle.mainloop()