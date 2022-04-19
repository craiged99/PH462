#TASK 4

from scipy import random
import scipy.integrate as integrate
import math
import numpy as np


#Define limits 

aa = 0
bb = 1

#Number of points to sample

N = 1000

#Creating array of random values between a and b

arrayA1 = []
arrayA2 = []
arrayA3 = []
arrayB1 = []
arrayB2 = []
arrayB3 = []
arrayC1 = []
arrayC2 = []
arrayC3 = []
for i in range(N):
    arrayA1.append(random.uniform(aa,bb))
    arrayA2.append(random.uniform(aa,bb))
    arrayA3.append(random.uniform(aa,bb))
    arrayB1.append(random.uniform(aa,bb))
    arrayB2.append(random.uniform(aa,bb))
    arrayB3.append(random.uniform(aa,bb))
    arrayC1.append(random.uniform(aa,bb))
    arrayC2.append(random.uniform(aa,bb))
    arrayC3.append(random.uniform(aa,bb))

#Define function

def f(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    a = np.array([a1, a2, a3])
    b = np.array([b1, b2, b3])
    c = np.array([c1, c2, c3])

    return 1/(abs(np.dot((a+b),c)))

#Create array for results for integral for each N

result = []
fx2 = []
result1 = []
fx21 = []

for h in range(len(arrayA1)):
    A1 = arrayA1[h]
    A2 = arrayA2[h]
    A3 = arrayA3[h]
    B1 = arrayB1[h]
    B2 = arrayB2[h]
    B3 = arrayB3[h]
    C1 = arrayC1[h]
    C2 = arrayC2[h]
    C3 = arrayC3[h]

    result.append(f(A1,A2,A3,B1,B2,B3,C1,C2,C3))
    result1.append(f(A1,A2,A3,B1,B2,B3,C1,C2,C3)**2)

    
#Sum up all results

sumofintegral = sum(result)
sumoffx2 = sum(fx2)

#Find variance

Variance = math.sqrt(((sum(result1)/N)-(sum(result)/N)**2)/N)

#Monte Carlo results

MC = (1/float(N))*sumofintegral




print('The estimate of the value of the integral is ' + str(MC))
print('The error is ' + str(Variance))
print('The error as a percentage is ' + str((Variance/MC)*100)+'%')

