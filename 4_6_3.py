from random import random as rand
x = []
for i in range(10):
    x.append( rand() * 10 )
print x

greatest = 1
for z in x:
    if z > greatest:
        greatest = z
print greatest