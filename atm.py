import time
print(" please inter your card")
time.sleep(3)
pin=int(input("please inter your pin number"))

password=123
balance=50000
if pin==password:
    while True:
        print("""
            1==balance
            2==withdral_balance
            3==devite_balance
            4==exit
            """)
        try:
            option=int(input(" please inter a  choice amount"))
        except:
            print("choice your wrong option....")

        if option==1:
            print("your corrent balance",{balance})
            print("************************************************")
            print("************************************************")
            print("************************************************")

        if option==2:
            withdraw=int(input("plese inter withdraw amount"))    
            balance=balance-withdraw
            
            print(f"withdral your amount",{withdraw})
            print("*****************************************")
            print("************************************************")
            print("************************************************")
            print("your carrent balance",{balance})
       
        if option==3:
            devite_amount=int(input("inter a devite amount"))
            balance=balance+devite_amount
            print("update balance",{balance})
            print("**********************************************************")
            print("**********************************************************")
        if option==4:
            break
   
else:
    print(" this is  a wrong pin number.please try agen")        
