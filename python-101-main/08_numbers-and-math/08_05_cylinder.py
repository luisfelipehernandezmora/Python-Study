# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.
import math
r=3.14
h=5
pi=math.pi
sur= 2*(pi*r**2)+2*pi*r*h
vol=(pi*r**2)*h

print("The surface area of a cilinder of radius:", r,"and height:",h,"is:",sur,'''
while the volumen is:''',vol)