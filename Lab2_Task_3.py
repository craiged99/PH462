import matplotlib.pyplot as plt
import numpy as np
import math


r = 2

def V(n):
    return (np.pi/math.gamma(n/2+1))*r**n

print(V(3))
print(V(5))

