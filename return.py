def cals(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
call=cals(100,300)
for i in call:
    print(i)
    i=i+1      
print("***********************************************")
#kyword argument

def funname(a,b):
    rk=a+b
    print(rk)
funname(a=10,b=20)   

## variable lenth

def  fi(*n):
    print("variable lenth")
fi() 
fi(10)   
fi(10,20,30)
print("********************************************************")
#################################g  gloable variable
a=100
def fun():
    a=20
    print(a)
def fun2():
    
    print(a)
fun()
fun2()    
print("**********************************************************")

####################################################
#factorial number= 1

def factorial2(n):
    f=1
    while n:
        f=f*n
        n-=1
    return f
print(factorial2(5))   
print("********************************************")
##########################################################
# prim number =2         

x=int(input("inter a number"))
f=1
while x:
      f=f*x
      x-=1
      print(f) 
      print("*************************************************")

##############################################################





