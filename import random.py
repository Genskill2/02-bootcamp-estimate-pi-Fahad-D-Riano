import random
def monte_carlo(n):
    cirpts=0
    sqrpts=0

    for i in range(n**2):
     rx=random.uniform(-1, 1)
     ry=random.uniform(-1, 1)

     og_dist=rx**2 + ry**2

     if og_dist<=1:
        cirpts+=1
    sqrpts+=1

    
    pi = 4* cirpts/ sqrpts 
    print(pi) 


monte_carlo(10000)    