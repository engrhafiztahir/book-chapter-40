#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Today topic will be about the picking out the information from dictionary within the dictionary.
#Let take an example of dictionary within the dictionary

customers = {
    0: {
        "first name":"John",
        "last name": "Ogden",
        "address": "301 Arbor Rd.",
    },
    1: {
        "first name":"Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145",
    },
    2: {
        "first name":"Jill",
        "last name": "Somers",
        "address": "3 Main St.",
    },
}
#This is the example of dictionary within the dictionary.
#Now to picup the particualr information use the following code
print(customers[0])
#The print statement is associated with the index number of the inner dictionary.
#Let take another example.
print(customers[1])
print(customers[2])
#So you see that each of the particular dictionary can be accessed through this command
#Now, we can also access a prticualr information in a particular dictionary. Let's take another example. 
print(customers[0]["address"])
# In this above code you can see that the index 0 of customers and after that the address has accessed
#Let's take another example 
print(customers[1]["address"])
print(customers[2]["address"])
#This is how we can access the particular information from the dictionary within the dictionary.
#Now let's solve the exercise.


# In[ ]:




