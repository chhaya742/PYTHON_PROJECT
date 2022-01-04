# To find non divisible subset

1. To find  non divisible subset from  a list first of all we will make a function "Subset():"
```python
def Subset():
```

-  then we will take two parameter S for list and k for number from which we will divide the elements of list.
```python
def Subset(S, k):
```
- now we will take a variable freq to calculate frequency 
and in that variable we will store a list this list will contain 0 elements k times. 
```python
freq=[0]*k
```
-  now we will iterate the list  by using for loop and freq will take one by one element of list and it will module by k and what ever remainder will come, it will add one to that index 
and in last we will get a list.

-  and it will return maximum frequency from that list

```python
def Subset(S, k):
    freq=[0]*k
    for i in S:
        freq[i%k]+=1
    return (max(freq))
```
what ever will be maximum frequency means this much subset will not divisible by value of k.

```python
Input

3  4
1 7 2 4 

```
```python
Output
3
```