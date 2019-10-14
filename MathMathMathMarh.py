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

