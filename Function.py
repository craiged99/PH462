
from scipy import random
import scipy.integrate as integrate
import math
import numpy as np
import matplotlib.pyplot as plt

#Monte Carlo integration function
def monte(dim,func,N,a1,b1,*args):
    #dim = no. of dimesions
    #func = function
    #N = no. of sample points
    #a1 = lower limit
    #b1 = higher limit
    #For multiple dimensions repeat a1 and b1.

    lists = [[] for i in range(dim)] #Create empy lists

    a,b = [],[]
    
    a.append(a1) #add limits to arrays of a & b
    b.append(b1)
    
    for i in range(dim*2-2): #limits of mulit-dimensional to arrays of a & b
        if i == 0 or i == 2:
            a2 = args[i]
            b2 = args[i+1]
            a.append(a2)
            b.append(b2)
    for i in range(dim): #Get array of random values between limits
        for j in range(N):
            lists[i].append(random.uniform(a[i],b[i]))
            

            
    answer = []     
    result = []
    result2 = []
    
    
    for i in range(N): #Substitute random values into fx 
        answer = []
        for j in range(dim):
            vlisty = lists[j]
            vlisty2 = vlisty[i]
            answer.append(vlisty2) 
        
        result.append(func(*answer))
        result2.append(func(*answer)**2) #For variance 
    
    
    Variance = math.sqrt(((sum(result2)/N)-(sum(result)/N)**2)/N) 
    
    
    if dim == 1:
        MC = (b[0]-a[0])/float(N)*sum(result)
        res = integrate.quad(lambda x: func(x), a[0], b[0])

    
    if dim == 2:
        
        MC = ((b[1]-a[1])*(b[0]-a[0]))/float(N)*sum(result)
        res = integrate.dblquad(lambda x,y: func(x,y), a[0], b[0], a[1], b[1])
        
    if dim == 3:
        
        MC = ((b[2]-a[2])*(b[1]-a[1])*(b[0]-a[0]))/float(N)*sum(result)
        res = integrate.tplquad(lambda x,y,z: func(x,y,z), a[0], b[0], a[1], b[1],a[2],b[2])

    if dim == 9:
        MC = (1/float(N))*sum(result)
        
        
        
    print('')
    print('The estimate of the value of the integral is ' + str(MC))
    print('The error is ' + str(Variance))
    print('The error as a percentage is ' + str((Variance/abs(MC))*100)+'%')
    print('')
    print('The actual result is '+ str(res[0]))
    
    
#Metropolis Method Function    
def metro(fx,px,xi,N,a,b):
    #fx = function
    #px = sampling function
    #xi = inital guess
    #N = No. of sample points
    #a = lower limit
    #b = upper limit

    res = []
    
    for i in range(N):
        
        si = random.uniform(a,b) #Find random value between limits
        xtrial = xi+si #Add value to inital guess
        
        
        w = px(xtrial)/px(xi)
        
        if w >= 1:
            xi = xtrial
            
        else:
            r = random.uniform(0,1)
            if r <= w:
                xi = xtrial
            else:
                xi = xi
                
        if i % 2 == 0:
            res.append(xi)
            
    Ifull = []
            
    
    for i in range(len(res))      :
        f_it = fx(res[i])
        p_it = px(res[i])
        Ifull.append(f_it/p_it)
        
    Int = np.mean(Ifull)
        
    #Plot histogram    
    plt.hist(res,bins=100)
            
            
    #actual result
    res = integrate.quad(lambda x: fx(x), a, b)
    
    
    print('Esimate is '+ str(Int))
    print('Result is ' + str(res[0]))


#Task 2 Functions:
def f2a(x):
    return 2

def f2b(x):
    return -x

def f2c(x):
    return x**2

def f2d(x,y):
    return x*y+x

#Task 5 Functions

def p5a(x):
    A = 1 / (2 - 2 * np.exp(-10))
    return math.exp(-abs(x))*A

def f5a(x):
    return 2*np.exp(-x**2)

def p5b(x):
    A = 5/(4*np.pi)
    return A*4*x *(np.pi - x)/np.pi**2

def f5b(x):
    return 1.5*np.sin(x)


