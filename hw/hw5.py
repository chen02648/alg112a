import random

def hillClimbing(f, p, h=0.01):
    failCount = 0                    
    while (failCount < 10000):       
        fnow = f(p)                  
        p1, f1 = neighbor(f, p, h)
        if f1 >= fnow:              
            fnow = f1               
            p = p1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0          
        else:                       
            failCount = failCount + 1
    return (p,fnow)                

def f(x, y, z):
    # return -1 * ( x*x -2*x + y*y +2*y - 8 )
    # return -1*((x-1)**2+(y-2)**2+(z-3)**2)
    return -1*(x**2+y**2+z**2)

hillClimbing(f, [2,1,3])
