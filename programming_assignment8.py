#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question1: Addition of matrices


A = [[1,2,3],
    [4 ,5,6],
    [8,8,9]]

B = [[4,9,1],
    [3,0,3],
    [8,7,9]]

res = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        res[i][j] = A[i][j] + B[i][j]

for r in res:
    print(r)


# In[2]:


#Question 2: Multiply 2 matrices


A = [[1,7,3],
    [41 ,15,6],
    [71 ,28,19]]

B = [[15,8,1],
    [26,7,3],
    [42,13,9]]

res = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(B)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            res[i][j] += A[i][k] * B[k][j]

for r in res:
    print(r)


# In[3]:


#Question3: Transpose of matrics

A = [[2,7],
    [44 ,15],
    [37 ,81]]

res = [[0,0,0],
         [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        res[j][i] = A[i][j]

for r in res:
    print(r)


# In[6]:


#Question4: Sorting of words

str1 = input('Enter a string ')


items = [item.lower() for item in str1.split()]

items.sort()


print("Your sorted string is ")
for ele in items:
    print(ele)


# In[9]:


#Question5: punctuation

import re
 
str1 =input('enter string: ')
 


res = re.sub(r'[^\w\s]', '', str1)
 
print('The string after removing punctuation: ', res)


# In[ ]:




