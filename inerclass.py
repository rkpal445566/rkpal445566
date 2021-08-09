class test:
    def __init__(self):
        print("outer class")
    
    class iner1:
        def __del__(self):
            print("this is a iner class of destructor")

t1=test()   
t2=t1.iner1()   
t2=None   

#destructor of use:-
import time
class test:
    def __init__(self):
        print("object anitisalition atomaticaly")
    def __del__(self):
        print("prafom cleanup activities")
t1=test()
time.sleep(5)
print("i love you") 