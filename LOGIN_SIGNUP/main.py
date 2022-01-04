import json
import re
import os
file_exist=os.path.exists("userdetail.json")
print(file_exist)
if file_exist==False:
    dic1={}
    list3=[]
    user=input("signup or login")
    if user=="signup":
        name=input("enter user name")
        print("your password length should be between 8-18")
        pas=input("creat a strong password")
        if len(pas)>=5 and len(pas)<=18:
            if re.search("[a-z]",pas) and re.search("[A-Z]",pas) and re.search("[0-9]",pas) and re.search("[@#$%&]",pas):
                pas2=input("confirm password")
                if pas==pas2:
                    print("congrats ",name,"you have succesfully signup")
                    dob=input("enter your date of birth in form of - 00/00/1900__  ")
                    descr=input("description  ")
                    hobbies=input("hobbies  ")
                    gender=input("gender  male of female   ")
                    dic1={}
                    print("congrats ",name,"you have succesfully signup")
                    list1=["name","pas2","dob","descr","hobbies","gender"]
                    list2=[name,pas2,dob,descr,hobbies,gender]
                    i=0
                    while i <len(list2):
                        dic1.update({list1[i]:list2[i]})
                        i+=1
                    dic2={}
                    list4=[]
                    list4.append(dic1)
                    dic2.update({pas:list4})
                    with open("userdetail.json","w") as h:
                        json.dump(dic2,h,indent=3)
                else:
                    print("both password are not same")
            else:
                print("your password is not strong,try again") 
elif file_exist==True:
        list3=[]
        user=input("signup or login")
        if user=="signup":
            name=input("enter user name")
            print("your password length should be between 8-18")
            pas=input("creat a strong password")
            with open("userdetail.json","r") as f:
                data=json.load(f)
            if len(pas)>=6 and len(pas)<=18:
                if re.search("[a-z]",pas) and re.search("[A-Z]",pas) and re.search("[0-9]",pas) and re.search("[@#$%&]",pas):
                    pas2=input("confirm password")
                    if pas==pas2:
                        print("congrats ",name,"you have succesfully signup")
                        dob=input("enter your date of birth in form of - 00/00/1900__  ")
                        descr=input("description  ")
                        hobbies=input("hobbies  ")
                        gender=input("gender  male of female   ")
                        print("congrats ",name,"you have succesfully signup")
                        list1=["name","pas2","dob","descr","hobbies","gender"]
                        list2=[name,pas2,dob,descr,hobbies,gender]
                        i=0
                        dic1={}
                        while i <len(list2):
                            dic1.update({list1[i]:list2[i]})
                            i+=1
                        list4=[]
                        list4.append(dic1)
                        data.update({pas:list4})
                        with open("userdetail.json","w") as h:
                            json.dump(data,h,indent=4)
                    else:
                        print("both password are not same")
                else:
                    print("your password is not strong,try again") 
        elif user=="login":
            user_name=input("enter user name")
            password=input("enter password")
            with open("userdetail.json","r") as f:
                data=json.load(f)
            for i in data:
                if i==password:
                    print("user is true")
                    print(data[i])
                else:
                    print("sorry your password is wrong")
                

                
        
                
