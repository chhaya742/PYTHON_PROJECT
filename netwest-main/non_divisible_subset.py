def Subset(S, k):
    freq=[0]*k
    for i in S:
        freq[i%k]+=1
    return (max(freq))
k=int(input("value of k:-"))
n=int(input("enter size of list:-"))
S=[]
for i in range(0,n):
    S.append(int(input()))
print()
print(Subset(S,k)) 
