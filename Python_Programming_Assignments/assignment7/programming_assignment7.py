#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question1: Sum of arrray

arr=[5,6,7,3,4,8,9]

asum=0

for ele in arr:
    asum+=ele
print('sum of array elements is ',asum)    


# In[3]:


#Question2:Largest element in array

arr=[1,3,5,2,4,8,9,26,4,61,3]

num=arr[0]
for i in range(len(arr)):
    if arr[i]>num:
        num=arr[i]
print('Largest element in array is ',num)        


# In[6]:


#Question3:Array rotation

def arr_rot(arr,d):
    l=len(arr)
    arr[:]=arr[d:l]+arr[0:d]
    return arr

arr=[1,3,5,7,9,2,4,8]

print('array after rotation by 2 places is ',arr_rot(arr,2))


# In[9]:


#Question4:Split array and add first part to end

def Split_Array(arr, n, k):
    for i in range(0, k):
        y = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]

        arr[n-1] = y

arr = [12,40,27,83,42,63,57]
n = len(arr)
k = 1
Split_Array(arr, n, k)

for i in range(0, n):
    print(arr[i], end = ' ')


# In[11]:


#Question 5:monotonic array

def monotone(arr):
  
    return (all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or
            all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)))

arr1=[1,3,4,5,6,9]
arr2=[4,2,4,5,1,6]
print('Is given array monotonic:',monotone(arr1))
print('Is given array monotonic:',monotone(arr2))


# In[ ]:




