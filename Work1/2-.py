#!/usr/bin/env python
# coding: utf-8

# In[46]:


m = 0
a = 0
list1 = [1,2,3,4,5]
while m < 5:
    
    x = int(input("Değer Giriniz : "))
    c = 0
    if x > 1:
        for i in range(2,x):
            if x%i == 0:
                list1[m] = ( x ,"Sayısı Asal Değildir")
                c = 1;
                break           
    else:
        list1[m] =  ( x ,"Sayısı Asal Değildir")
        c = 1

    if c == 0:
        list1[m] = ( x ,"Sayısı Asaldır")
    
    m = m + 1

for i2 in list1:
    print(list1[a])
    a = a + 1


        


# In[ ]:




