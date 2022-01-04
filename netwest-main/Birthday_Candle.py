def birthdaycakecandkes(n,count=0):
    tallest=n[0]
    for i in n:
        if tallest<i:
            tallest=i
    for i in n:
        if tallest==i:
            count+=1
    return "the maxumum height candles are ",tallest,"units high.There are ", count,"of them"
use=int(input("enter number of candles:-"))
inter=input("enter candles:-\n")
list1=[]
for i in range (1,use):
    list1.append(int(input()))
print(birthdaycakecandkes(list1))