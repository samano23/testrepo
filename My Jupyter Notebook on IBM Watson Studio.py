#!/usr/bin/env python
# coding: utf-8

# In[ ]:


My Jupyter Notebook on IBM Watson Studio


# In[5]:


bold = '\33[1m'
print(bold + "Saman Alkhaffaf")
print(bold + "My current role is Head of Business Development and I am interested in the role of Head of Data Analytics")


# In[3]:


bold = '\33[1m'
print(bold + "I am interest in Head of Data Analytics role for the next generation of industrial automation machines and Smart Sensors")


# In[6]:


bold = '\33[1m'
print(bold + "The following code tests the multiplication of two matrices input and displays the output")


# In[12]:


# input two matrices of size n x m
matrix1 = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]
matrix2 = [[5,8,1],
        [6,7,3],
        [4,5,9]]
 
res = [[0 for x in range(3)] for y in range(3)]
 
# explicit for loops
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
 
            # resulted matrix
            res[i][j] += matrix1[i][k] * matrix2[k][j]
 
print (res)

