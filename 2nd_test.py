#!/usr/bin/env python
# coding: utf-8

# In[10]:


a,b =100000,2.3


# In[11]:


type (a)


# In[12]:


type (b)


# In[13]:


x =a+b


# In[14]:


print (x)


# In[15]:


5+2*3-4/2


# In[16]:


(5+2)*(3-4)/2


# In[17]:


e= input('enter data : ')


# In[18]:


type (e)


# In[20]:


num1 = input(' enter the 1st number ')
num2 = input(' enter the 2nd number ')
num1 = float(num1)
num2 = float(num2)
print('sum = ',num1+num2)
print('sub = ',num1-num2)
print('div = ',num1/num2)
print('mul = ',num1*num2)


# In[21]:


p=5


# In[22]:


l=5


# In[23]:


p==l


# In[ ]:


p is l


# In[1]:


age = input(' enter your age : ')
Gender = input(' enter your gender : ')
age = float (age)
if age >= 18 and (Gender =='male' or Gender =='m') :
    print('OK')
elif age < 18 and (Gender =='male' or Gender =='m'):
    print ('you cant do that')
elif age >= 18 and (Gender =='female' or Gender =='f'):
    print('ok')
elif age < 18 and (Gender =='female' or Gender =='f'):
    print('you cant do that')
else :
    print ('undefind gender')


# In[4]:


num1 = input('enter your 1st number')
num2 = input('enter your 2nd number')
op = input('enter the opratian')
num1= float (num1)
num2= float (num2)
if op == '+':
    res=num1+num2
    print("SUM = ", res)
elif op =='*' or 'X' or 'x':
    res = num1*num2
    print("MUL = ", res)
elif op =='/' or '\\':
    res=num1/num2
    print("DVI = ", res)
elif op == '-':
    res=num1-num2
    print("SUB = ", res)


# In[7]:


namesT = ('hassan' , 'ali' , 'waled')
ages =['20' , '30' , '40']
print (len(namesT))
print(namesT)
print(max(namesT))
ages.index


# In[12]:


ages = list(ages)


# In[13]:


ages


# In[14]:


type(ages)


# In[15]:


ages.append(90)


# In[16]:


ages = tuple(ages)


# In[17]:


ages


# In[18]:


type(ages)


# In[19]:


list1 = { 'name' , 'gender' , 'age'}


# In[21]:


dic1 =dict.fromkeys(list1)


# In[22]:


dic1


# In[15]:


name = input (' enter your name ')
number= 3
masge = 'welcome MR %s python %d' % (name , number)
for s in range(len(masge)):
    print(masge[s])


# In[14]:


msg = ('wlcome to python')
for s in range(len(msg)):
    print(msg[s])


# In[18]:


dic2 = {'name' : 'hassan','gender' : 'male' , 'age' : 21}
for key , value in dic2.items():
    print (key,",",value )


# In[1]:


num = input('enter a number:')
while num !='0':
    print ('continue')
    num = input('enter a number:')
print ('the end')


# In[5]:


for i in range(0,5):
    print('*',end=' ')


# In[10]:


for line in range (2):
    for i in range(0,5):
        print('*' ,end = ' ' )
    print ('\n')


# In[17]:


word = 'hassan'
for g in word :
    if g == 'a':
        continue
    print(g)


# In[3]:


def hassan(row = 1 , col =1):
    for line in range(row):
        for i in range(col):
            print ('*', end = ' ')
        print('\n')


# In[4]:


hassan()
print ('welcome to the python \n')
hassan()


# In[17]:


def change(x):
    "pla pla pla"
    x = [1,2,3,4]
    print("values inside the function :", x)
    
mylist=[ 10 , 20 , 30];
change(mylist);
print("valus outside the function" , mylist)   


# In[14]:


total = 0

def sub( num1 , num2):
    global total
    total= num1 - num2
    print("outside the local " , total)
    
sub(40,10)
print("print the global total" , total)


# In[18]:


totalo = 0

def subb( num1 , num2):
    total= num1 - num2
    print("outside the local " , total)
    return(total)
    
def summ( num1 , num2):
    total= num1 + num2
    print("outside the local " , total)
    return(total)


# In[19]:


summ = summ (10,20)
subb = subb(10,20)
print("print the global total ",total)
print("print the global summ ",summ)
print("print the global sub ",sub)


# In[11]:


def max_two_numbers(num1,num2) :
    if num1 > num2:
        return (num1)
    else :
        return (num2)
        
    
def max_three_numbers (num1,num2,num3):
     m = max_two_numbers(num1,num2)
     fin = max_two_numbers(m,num3)
     return(fin)
    
num1 = input('enter the firest number :')
num2 = input('enter the sacend number :')
num3 = input('enter the theerd number :')
res = max_three_numbers(num1,num2,num3)
print('max = ',res)


# In[14]:


def uniquelist(nonuniquelist):
    res = []
    for n in nonuniquelist :
        if n not in res :
            res.append(n)
    return(res)

numbers = [1,1,1,85,4,894,51,23,186,4,123,1,1,12,56,7,8,456,1,5,5,9,9,5]
hassan = uniquelist(numbers)
print(hassan)


# In[ ]:




