#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q1:sum of elements in list

l=[1,2,4,3,5,6,7,8,9]
Sum=0

for ele in l:
    Sum+=ele

print("Sum of elements in given list is ",Sum)


# In[4]:


#Q2:Multiply elements in list

l=[1,2,4,3,5,6,7,8,9]
mult=1

for ele in l:
    mult*=ele

print("Sum of elements in given list is ",mult)


# In[5]:


#Q3. Smallest in list

l=[1,2,4,3,5,6,7,8,9,0,34]
small=l[0]

for i in range(len(l)):
    if l[i]<small:
        small=l[i]

        
print('Smallest number in list is ',small)


# In[8]:


#Q4. largest in list

l=[1,2,4,3,54,6,7,8,9,0,34]
large=l[0]

for i in range(len(l)):
    if l[i]>large:
        large=l[i]

        
print('largest number in list is ',large)


# In[9]:


#Q5: second largest in list

l=[1,2,4,3,54,6,7,8,9,0,34]

l.sort()
l.reverse()
print('second largest in list is  ',l[1])


# In[12]:


#Q.6 N largest in list

l=[1,2,4,3,54,6,7,8,9,0,34]
n=int(input('give the N value= '))


l.sort()
l.reverse()
print(n,'largest in list is  ',l[0:n])


# In[14]:


#Q.7 Even numbers in list

l=[1,2,4,3,54,6,7,8,9,0,34]

print('even numbers in the list are ')
for ele in l:
    if ele%2==0:
        print(ele)


# In[15]:


#Q.8 Odd numbers in list

l=[1,2,4,3,54,6,7,8,9,0,34]

print('odd numbers in the list are ')
for ele in l:
    if ele%2!=0:
        print(ele)


# In[16]:


#Q.9 remove empty list from list

l = [5, 6, [], 3, [], [], 9,12,34,53]
 
print('original list is : ',l )
 
res = [item for item in l if item != []]
 
print('new list is : ',res )


# In[17]:


#Q10. Cloning or coping

l1=[3,4,2,1,5,6,7]

l2=l1

print('Original list is ',l1)
print('Copied list is ',l2)


# In[20]:


#Q.11 Count occurence of element

l1=[3,4,2,1,5,6,7,5,6,3,4,3,22,4,3]


print('in the given list 3 occurs {}'.format(l1.count(3)),'times ')


# In[ ]:




