import time
class test1:
    def __init__(self):
        print("constructor exicute")

    def __del__(self):
        print("gravege calector deinisilize an object")
t1=[test1(),test1(),test1()]
print("list object elegible garbage callector")

del t1
time.sleep(5)
print("end of applicatione")