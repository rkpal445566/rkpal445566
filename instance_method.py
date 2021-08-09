class student:
    def __init__(self,name,marks):
        self.name=mame
        self.marks=marks
    
    
    def desplay(self):
        print("student name:",self.name) 
        print("student markes:",self.marks)
    
    def gread(self):
        if marks>=60:
            print("you got first grad")
        
        elif marks>=50:
            print("you got second gred")

        elif marks >=40:
            print("you got third gred")
        else:
            print("you are fale") 
        
    n=int(input("inter a number"))    
        for i in range(n):


            name=int(input("inter a name"))
            marks=int(input("inter  a number"))
            
                s=student(name,marks)
                s.desplay()
                s.gread()
                print("end",)
