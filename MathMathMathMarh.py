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
