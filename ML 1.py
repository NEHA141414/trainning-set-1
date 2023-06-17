#!/usr/bin/env python
# coding: utf-8

#     Start
#     next
#     third
#     variable declaratiobn
#     

# In[1]:


a=10
b=5.1
c='hay'


# In[2]:


a=10


# In[3]:


a


# In[4]:


print(a)


# In[5]:


b=5.1
c="neha"


# In[6]:


c


# In[7]:


type(c)


# In[8]:


a=10
b=5


# In[9]:


#operators are = +,-,*,/,//,**


# In[10]:


print(a+b)
print(a-b)
print(a*b)
print(a/b)


# In[11]:


print(10//3)# integer divide


# In[12]:


print(2**3)


# In[13]:


print(10%5)
print(10%4)


# In[14]:


print(a,b)
print(f"this is value of a ={a}")


# In[15]:


#logical operator
and ,or , not


# In[ ]:


rain=True
temp=40
playing=not rain  and temp<50


# In[ ]:


print(playing)


# In[ ]:


# if else condition


# In[ ]:


a=10
if a%2==0:
    print("even")
else:
    print("odd")


# In[ ]:


# i have a number and i divided it by 3 and need to check reminder


# In[ ]:


a=int (input())
a


# In[ ]:


type(a)


# a= int(input())
# if a%3==0 :
#     print("zero")
# elif a%3==1 :
#     print("one")
# else:
#     print("two")

# Loops

# In[ ]:


range(10)


# In[ ]:


a=list(range(10))


# In[ ]:


a


# In[ ]:


a=list(range(1,11,2))


# In[ ]:


a


# In[ ]:


for i in range (2,21,2) :
    print(i)


# In[ ]:


for i in range (21,2,-2) :
    print(i)


# In[ ]:


a=int(input())
flag=True
for i in range(2,a//2) :
    if a%i == 0:
        print("not prime")
        flag=False
        break
if flag==True :
    print("prime")


# In[ ]:


2
4
8
16
32
2^10


# In[ ]:


for i in range(1,11) :
    print(2**i)


# Function

# In[ ]:


def fun1():
    print("Hello world")


# In[ ]:


fun1()


# In[ ]:


def fun2(a):
    print(a)


# In[ ]:


fun2(10)


# In[ ]:


fun2("hey wac")


# In[ ]:


def add(a,b):
    print(a+b)
    


# In[ ]:


add(5,4)


# In[ ]:


# recurtion


# In[ ]:


sum=0
for i in range(1,11):
    sum+=i
    print(sum)


# In[ ]:


def sum(a):
    if a ==1:
        return 1
    #recursive function
    return a+sum(a-1)


# In[ ]:


sum(10)


# In[ ]:


def fact (a):
    if a ==0 or a ==1:
        return 1
    return a*fact(a-1)


# In[ ]:


fact(0)


# In[65]:


def fibo(a):
    if a ==0 or a==1:
        return a
    return fibo (a-1)+fibo(a-2)


# In[67]:


fibo(6)


# In[68]:


for i in range(17):
    print(fibo(i))


# Strings

# In[ ]:


a="Hello"


# In[ ]:


a


# In[ ]:


for i in a :
    print(i)


# In[ ]:


a.upper()


# In[ ]:


a.casefold()


# In[ ]:


a.count("neha")


# In[ ]:


a=input("your name=").strip()


# In[ ]:


print(a.strip())


# Data structures

# In[ ]:


# tuples
#list
#sets
#dict


# In[ ]:


#mutable and imutable


# In[ ]:


a=tuple([1,2,3,4,"neha"])


# In[ ]:


a


# In[ ]:


a[0]


# In[ ]:


type(a)


# In[ ]:


b=(2,3,4,5,32,343,55321)


# In[ ]:


b


# In[ ]:


type(a),type(b)


# In[ ]:


#single line assignment
a,b,c=5,10,15


# In[ ]:


a,b,c


# In[ ]:


print(a+b+c)


# In[ ]:


print(a+b)


# In[22]:


#list
l=[1,3,4,5,6,7,8,9]


# In[23]:


l


# In[24]:


type(l)


# In[25]:


l[1]


# In[26]:


l[0]


# In[27]:


l[0]=10


# In[28]:


l


# In[29]:


l=[1,2,3,4,5]


# In[30]:


l


# In[31]:


len(l)


# In[34]:


for i in range(len(l)):
    l[i] +=5


# In[35]:


l


# In[36]:


l=[20,30,50,10]
l


# In[50]:


#list comphension
l=[i+5 for i in l]


# In[51]:


l


# In[43]:


print(l+l)


# In[44]:


l.append(100)


# In[45]:


l


# In[46]:


l.clear()


# In[47]:


l


# In[52]:


max(l)


# In[53]:


l=[1,2,3,4,5,6,7,8,9]


# In[54]:


l


# In[55]:


max(l)


# In[56]:


#sets


# In[58]:


a={1,2,3,2,31,12,32,21,2,2,2,1,1,1,4,4,4,43,3,3,3,3}


# In[59]:


a


# In[60]:


#dict


# In[62]:


#fibonacci --->recursively
# 0 1 1 2 3 4 5


# In[70]:


d={"apple":100,"banana":120,"mango":[110,150],"orange":200}


# In[71]:


d


# In[72]:


d.keys()


# In[74]:


d.values()


# In[75]:


for i in d.keys():
    print(i)


# In[85]:


for i in d.keys():
    print(f"{i} has price ={d[i]}")


# In[86]:


for i in d.keys():
    d[i] -=30


# In[87]:


d


# In[93]:


d1={"apple":100,"banana":120,"mango":[120,150,300],"orange":200}


# In[94]:


d1


# In[95]:


d1["mango"]


# In[96]:


type(d1["mango"])


# In[97]:


d1["mango"][1]


# In[98]:


l1=["a","b","c","d"]
l2=[1,2,3,4]


# In[99]:


d={}
for i in range(len(l1)):
    d[l1[i]]=l2[i]


# In[100]:


d


# In[102]:


','.join(f"{l1[i]}:{l2[i]}" for i in range(len(l1)))


# In[105]:


s="abcaabbaaa"


# In[110]:


s[:4]


# In[111]:


s[-1:-2:-4]


# In[115]:


s==s[ : :-1]


# In[121]:


def palin(s):
    print(s)
    print(s[::-1])
    return s==s[ : : -1]


# In[122]:


palin("abc")


# In[123]:


l=list(range(10))


# In[124]:


l


# In[125]:


l[:7]


# In[126]:


l[1:8]


# In[127]:


l[::-1]


# In[128]:


s="    hello world      "


# In[130]:


s


# In[133]:


s


# In[134]:


s=s.strip().split()


# In[135]:


s


# In[ ]:




