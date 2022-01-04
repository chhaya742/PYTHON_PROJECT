print('****😇🙏WELCOME TO allIndia_cab🙏😇****')
print(  )
import json  
import random
places=['flora','khopi','pisoli','katraj','khed-shivpura','pawna lake','sinhagad','pnsht','bisapur','mavl','tikona ford','lonavla','toll plaza','railway station']
with open("data.json",'r') as f:
    data1=json.load(f)
var1=input("enter your current location__")
var2=input("enter your destiny place__")
def ola():
    if var1 in places and var2 in places :
        select1=input("what you want..\nauto\ncab\ntaxi\nbike___\n")
        print(    )
        print(select1)
        print('drivers list')
        list1=[]
        for i in data1: 
            if select1==data1[i]['vehical']:  
                list1.append(data1[i])
        print()
        h=1
        for k in list1:
            print(h)
            for l in k:
                print('   ',l,"=",k[l])
            print(     )
            h+=1
        b=random.randint(a=10,b=50)
        print(b  ,'km')
        select=int(input("select..."))
        print(list1[select-1]["name"])
        print('contact_no.__',list1[select-1]["phone_no"])
    
        r=(random.randint(a=0,b=len(places)))
        print('current location of driver__',places[r])
        print("driver will be pickup you within",random.randint(a=10,b=50),'minut')
        print(   )
        p=list1[select-1]["amount/km"]
        print('Total Payment=',p*b)
        print("you will be reach after",random.randint(a=1,b=3),':',random.randint(a=1,b=60),'minut')
        amount1=p*b
        print(  )
        book=input("do you want to book yes or no\n")
        if book=='yes':
            otp=random.randint(a=1000,b=9999)
            otp1=otp
            print('genreted otp..',otp)
            otp2=int(input("enter otp.."))
            if otp2==otp1:
                print("succesfull")
            else:
                print("enter correct otp")
            pay=input("what you will prefer for payment\nonline\ncash on\n")
            if pay=='cash on':
                print('pay to driver')
            elif pay=='online':
                orl=input("by phone number or QRL code\n")
                if orl=='QRL code':
                    print("scan code and send mony")
                    money=int("enter money")
                    if money==amount1:
                        print("payment succesfull")
                    else:
                        print('opps')
                elif orl=='phone number':
                    number=input("enter number")
                    money=int(input("enter money"))
                    if money==amount1:
                        print("payment succesfull")
                    else:
                        print('opps')
            fead=input('give your feadback *****__')
            if fead=='*'or fead=='**':
                print('😥bad')
            elif fead=='***'or fead== '****':
                print('🙂good')
            elif fead=='*****':
                print('😊exillent')
        else:
            print('back')
ola()






            






            

