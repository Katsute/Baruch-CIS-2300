#!/usr/bin/env python
# coding: utf-8

#                                             ### In Class Exercise-1 ###
#                                             
# Create a separate jupyter notebook file called ICE1_FirstLastname to complete the following in-class exercises. Use input, output, variables, F-strings, and other concepts that you learned in this session.

# 1. Write a program to get user's firstname, last name, street address, city, state, zipcode and then print the output in a format similar to below: 
# Linmei Huang
# 1 Bernard Baruch Way
# New York, NY 10010

# In[1]:


print("Keith Chiu", "1 Bernard Baruch Way", "New York, NY 10010", sep='\n')


# 2. Write a program to output following wages of employees (some are bi-weekly, monthly, and yearly). Be sure to properly format their wages such that they are aligned, with proper formatting: 
#    - Andrew $45,400.66 
#    - Jack   $999.99 
#    - Mary   $2,700.05 
#    - Lisa   $100,030.45

# In[3]:


stringf = "${:,.2f}"
print(
    "Andrew" + '\t' + stringf.format(45_400.66),
    "Jack"   + '\t' + stringf.format(999.99),
    "Mary"   + '\t' + stringf.format(2_700.05),
    "Lisa"   + '\t' + stringf.format(100_030.45),
    sep='\n'
)

