from graph import *
import math

def ellips(a, b, XC, YC, color, nak=0):
    alfa=0
    A=[]
    for i in range(25):
        x=a*math.cos(alfa)
        y=b*math.sin(alfa)
        X=x*math.cos(nak)+y*math.sin(nak)
        Y=-x*math.sin(nak)+y*math.cos(nak)
        A.append((X+XC,Y+YC))
        alfa+=math.pi/12   
    brushColor(color)
    elip=polygon(A)
    return elip


#obj2=ellips(30, 50, 100, 100, 'red')

#obj1=ellips(30, 50, 150, 100, 'green')
#B=[]
#B.append(obj1)
#B.append(obj2)
#print(B[0])
line(0,0,150,100)
X=0
T=0
B=[]

el1=ellips(30, 50, 100+X, 100, 'red')
    

el2=ellips(30, 50, 150+X, 100, 'green')

  
B.append(el1)
B.append(el2)
 
def perem():
    global X
    global T
    global B
    if T > 1 :
        print('Nach')
        deleteObject(B[0])
        deleteObject(B[1])
        print(B)
        el1=ellips(30, 50, 100+X, 100, 'red', T*math.pi/6)
        el2=ellips(30, 50, 150+X, 100, 'green',-T*math.pi/6 )
        B.insert(0,el1)
        B.insert(1,el2)
        print(B)
    for k in range(len(B)):
        moveObjectBy(B[k], 30, 0)
    print(X)
    print(B)
    
    X = 30+X
    T = T+1
    
onTimer(perem, 1000)

run()
