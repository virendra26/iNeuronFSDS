#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Question1: Disarium number

def disarium(num):
    temp = 0
    for i in range(len(str(num))):
        temp += int(str(num)[i]) ** (i + 1)
    return temp == num

num=int(input('Enter any number '))
print('is given number disarium :',disarium(num))


# In[5]:


#Question 2: Disarium number between 1 to 100:

print('Disarium number between 1 to 100 are:')
for i in range(1,101):
    temp=0
    for j in range(len(str(i))):
        temp+=int(str(i)[j])**(j+1)
        if temp==i:
            print(i)
        


# In[7]:


#Question 3: Happy number

def Happy_num(n):
    past = set()
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True
n=int(input('Enter a number '))
print('Given number is Happy? :',Happy_num(n))


# In[4]:


#Question 4: Happy numbers in interval 1 to 100

def happy(num):
    rem = 0
    hnum = 0;    
    while(num > 0):
        rem = num%10;    
        hnum = hnum + (rem*rem);    
        num = num//10;
    return hnum;


print("HAPPY NUMBERS WITHIN RANGE 1 to 100 ARE -")
for i in range(1,101):
    happy_num = i
    while(happy_num != 1 and happy_num != 4):
        happy_num = happy(happy_num)
    if(happy_num == 1):
        print(i,end=" ")


# In[6]:


#Question 5 Harshad Number
num = int(input("Enter the Number to Check Harshad Number = "))
Sum = 0
rem = 0

temp = num
while temp > 0:
    rem = temp % 10
    Sum = Sum + rem
    temp = temp // 10

print('The Sum of the Digits = ',Sum)

if num % Sum == 0:
    print("Given number is Harshad number")
else:
    print("its not a harshad number")


# In[8]:


#Question 6:Pronic Number
def PronicNumber(num):    
    flag = False;    
        
    for i in range(1, num+1):    
        if((i*(i+1)) == num):    
            flag = True;    
            break;    
    return flag;    
     
print("Pronic numbers between 1 and 100: ");    
for i in range(1, 101):    
    if(PronicNumber(i)):    
        print(i)  


# In[ ]:




