# First program
# find tallest candles

1.Firstly we will make a function  'birthdaycakecandles' to find out how many candles are tallest.
```python
def birthdaycakecandkes():
```

For making this function

- we will take  two parameter one for list and second one is default parameter. It intialize from 0 this parameter will use for count.
```python
def birthdaycakecandkes(n,count=0):
```

Then in that funtion we  make one more  function max .

For making max fuction.

- we will take a variable tallest, in that variable we will assign 0, the position element of list.

-  Then we will iterate the list using for loop.

-  If tallest  is less then first element of list, then 
tallest will update by that element .
Like list will iterate one by one and in last we will get a max number.
```python
def birthdaycakecandkes(n,count=0):
    tallest=n[0]
    for i in n:
        if tallest<i:
            tallest=i
```

2.for finding accuracy of tallest we will apply one more loop on list and 
-  If tallest is equal to any element of list   will count.
```python
for i in n:
    if tallest==i:
        count+=1
```


now we will call 'birthdaycakecandkes' and pass argument 

For passing argument 

-  we will ask size of list how many candles want user.
-  then we will iterating a loop on size of list and will tale input element from user and append them in a list and this list  passed as argument 

It will return the accuracy of heighest candles.

Input:
```python
5 
4 5 6 6 3

```
```python 
Output 

2

```

