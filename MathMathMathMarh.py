# Starting Off
print(22/7)
print(355/113)
import math
print(9801/(2206 * math.sqrt(2)))
def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sidesS = oneHalfSideS * 2
    polygonCircumference = numSides * sidesS
    pi = polygonCircumference / 2
    return pi

print(archimedes(8))
print(archimedes(16))

for sides in range (8, 100, 8):
    print(sides, archimedes(sides))

# experiment with the loop above alongside the actual value of Pi. How many
# sides does it take to make the two close?

# Modfiy the Archimeds function to tale the radius of the circle as a parameter
#  Can you get a better answer more quickly using a larger circle?

# Accumulators

acc = 0
for x in range(1, 6):
    acc = acc + x

print(acc)

# compute the sum of the first 100 even numbers
# compute the sim of the first 50 odd numbers
# compute the average of the first 100 odd numbers
# write a function that returns the average of the first N numbers, where
#   N is a parameter
# write a function called factorial that computes the product of the first
#    N numbers, where N is a parameter
# Each number in the Fibonacci sequence id the sim of the previous two numbers
#   The first two numbers in the sequence are 1 and 1. compute the 10th Fibonacci
#   number.
# Write a function to compute the Nth Fibonacci number, where N is a parameter
#   You may assume that N will be greater than or equal to 3.

#  A Monte Carlo Simulation
import random
print(random.random())
# Random here means (0,1) (not including one), resulting in a decimal.
# In computer science, there is no true "random", which is only in its true from in nature. There is a
# way to calculate the computer "random".

# Boolean expressions
# (six possible opperators):
#           > greater than
#           >= greater than or equal to
#           < less than
#           <= less than or equal to
#           == the same as [equal to]
#           != not equal to

dogWeight = 25
print(dogWeight > 25)
kitkatBags = 3425

# Compund Boolean operators:
#   -and
#   -or
#   -not

print(dogWeight < 30 and kitkatBags < 30000)

a = 5
b = 10
c = 75

if a > b:
    c = 75

print(c)

if a > b:
    c = 45
    if b > c:
        a = 25
    else:
        a = -25
else:

    c = 1050505050050505050505050000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    if b == a :
        c = a + b
print(c)
print(a)
d = 55
e: int = 72
f = 44
ans = 0
if d > e:
    ans = 12
else:
    if d == e:
        ans = 50
    else:
        if f < d * e:
            ans = 100
            ans = 75
print(ans)

# Randomized ability to approximate Pi
import turtle
def showMontePi(numDarts):

    scn = turtle.Screen()
    brother = turtle.Turtle()

    scn.setworldcoordinates(-2, -2, 2, 2)
    brother.penup()
    brother.goto(-1,0)
    brother.pendown()
    brother.goto(1,0)
    brother.penup()
    brother.goto(0,1)
    brother.pendown()
    brother.goto(0,-1)


    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)
        brother.goto(x,y)

        if distance <= 1:
            inCircle = inCircle + 1
            brother.color("blue")
        else:
            brother.color("red")
        brother.dot
    pi = inCircle / numDarts * 4
    scn.exitonclick()
    return pi

showMontePi(100)






