import math
from math import *

print("true value of simple pendulum's time period")
x = int(input("0 for Radian mode, 1 for Degree mode"))
if x == 0:
    theta = float(input("what is the initial angle of pendulum with respect to equilibrium position, in radians"))
if x == 1:
    thetadeg = float(input("what is the initial angle of pendulum with respect to equilibrium position, in degrees"))
    theta = thetadeg * 3.141592653589793238462643383279/180


l = float(input("input the length of the string-mass system in meters"))
g = float(input("input the local gravitational acceleration"))


T = float((2*3.141592653589793238462643383279*(l/g)**0.5)*(((factorial(2*0)/((2**0)*factorial(0))**2)**2)*(sin(theta/2))**(2*0)
                                                           +((factorial(2*1)/((2**1)*factorial(1))**2)**2)*(sin(theta/2))**(2*1)
                                                           +((factorial(2*2)/((2**2)*factorial(2))**2)**2)*(sin(theta/2))**(2*2)
                                                           +((factorial(2*3)/((2**3)*factorial(3))**2)**2)*(sin(theta/2))**(2*3)
                                                           +((factorial(2*4)/((2**4)*factorial(4))**2)**2)*(sin(theta/2))**(2*4)
                                                           +((factorial(2*5)/((2**5)*factorial(5))**2)**2)*(sin(theta/2))**(2*5)
                                                           +((factorial(2*6)/((2**6)*factorial(6))**2)**2)*(sin(theta/2))**(2*6)
                                                           +((factorial(2*7)/((2**7)*factorial(7))**2)**2)*(sin(theta/2))**(2*7)
                                                           +((factorial(2*8)/((2**8)*factorial(8))**2)**2)*(sin(theta/2))**(2*8)
                                                           +((factorial(2*9)/((2**9)*factorial(9))**2)**2)*(sin(theta/2))**(2*9)
                                                           +((factorial(2*10)/((2**10)*factorial(10))**2)**2)*(sin(theta/2))**(2*10)
                                                           +((factorial(2*11)/((2**11)*factorial(11))**2)**2)*(sin(theta/2))**(2*11)
                                                           +((factorial(2*12)/((2**12)*factorial(12))**2)**2)*(sin(theta/2))**(2*12)
                                                           +((factorial(2*13)/((2**13)*factorial(13))**2)**2)*(sin(theta/2))**(2*13)
                                                           +((factorial(2*14)/((2**14)*factorial(14))**2)**2)*(sin(theta/2))**(2*14)
                                                           +((factorial(2*15)/((2**15)*factorial(15))**2)**2)*(sin(theta/2))**(2*15)
                                                           +((factorial(2*16)/((2**16)*factorial(16))**2)**2)*(sin(theta/2))**(2*16)))



print("the time period of the pendulum is", T,"seconds")




#((factorial(2*n)/((2**n)*factorial(n))**2)**2)*(sin(theta/2))**(2*n)










