import scipy.optimize
import math
import time
def f(x):
    return math.cos(x)/(1+x**2)
def derivative(x):
    return (-math.sin(x)/(1+x**2))-((math.cos(x)*2*x)/(1+x**2)**2)


print (scipy.optimize.bisect(f,0.1,2.4))
start_time=time.time()
for i in range(10000):
    scipy.optimize.bisect(f,0.1,2.4)
print ('execution time',time.time()-start_time)

start_time=time.time()
for i in range(10000):
    scipy.optimize.newton(f,1.57,fprime=derivative)
print ('execution time',time.time()-start_time)

start_time=time.time()
for i in range(10000):
    scipy.optimize.newton(f,1.57,fprime=None)
print ('execution time',time.time()-start_time)


start_time=time.time()
for i in range(10000):
    scipy.optimize.brentq(f,0.1,2.4)
print ('execution time',time.time()-start_time)

