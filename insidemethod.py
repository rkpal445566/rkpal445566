#inside the class use instance variables
class employe:
    def __init__(self):
        self.name="Name"
        self.sall=111111
    def mathr(self):
        print("instance mehode",self.name)
        print("salary:",self.sall)
        address="jhadiyahi"
        print(address)
ob=employe()
ob.mathr()
print("***************************************************")



#oug side the class using object referance variabale


class employe:
    def __init__(self):
        self.a=10
        self.b=20
    def mtho(self):
        print(self.a)
o=employe()
o.mtho()
o.d=40
print(o.__dict__)

print ("************************************************")


#how to delet instance variable


class abc:
    def __init__(self):
        self.a=100
        self.b=200
    def mth(self):
        del self.a
        
ob=abc()
print(ob.__dict__)
ob.mth()
print(ob.__dict__)
del ob.b
print(ob.__dict__)        
print("**********************************************")


#static variabel of use in side class


class x:
    a=10
    def __init__(self):
        self.b=20
        
    def m1(self):
        print(self.a)
ob=x()
print(ob.b)    
ob.m1()        
print("*******************************************************")

#we can use all variable and 


class abcd:
    a=1000
    def __init__(self):
        self.b=2000
    def m1(self):
        abcd.c=3000
    
    
    @classmethod
    def m2(cls):
        cls.d=4000
        abcd.e=5000
    


    @staticmethod
     def m3():
         abcd.d=6000
         print(abcd.__dict__)

    t=abcd()      
