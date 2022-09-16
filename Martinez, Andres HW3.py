#!/usr/bin/env python
# coding: utf-8

# # Week 3 (Wed) - Booleans, Tuples, and Dictionaries

# ## Booleans

# A ``boolean`` is one of the simplest Python types, and it can have two values: ``True`` and ``False`` (with uppercase ``T`` and ``F``):

# In[ ]:


a = True
b = False


# Booleans can be combined with logical operators to give other booleans:

# In[ ]:


True and False


# In[ ]:


True or False


# In[ ]:


(False and (True or False)) or (False and True)


# Standard comparison operators can also produce booleans:

# In[ ]:


1 == 3


# In[ ]:


1 != 3


# In[ ]:


3 > 2


# In[ ]:


3 <= 3.4


# ## Exercise 1

# Write an expression that returns ``True`` if ``x`` is strictly greater than 3.4 and smaller or equal to 6.6, or if it is 2, and try changing ``x`` to see if it works:

# In[ ]:


x = 3.7

# your solution here


# ## Tuples

# Tuples are, like lists, a type of sequence, but they use round parentheses rather than square brackets:

# In[ ]:


t = (1, 2, 3)


# They can contain heterogeneous types like lists:

# In[ ]:


t = (1, 2.3, 'spam')


# and also support item access and slicing like lists:

# In[ ]:


t[1]


# In[ ]:


t[:2]


# The main difference is that they are **immutable**, like strings:

# In[ ]:


t[1] = 2


# We will not go into the details right now of why this is useful, but you should know that these exist as you may encounter them in examples.

# ## Dictionaries

# One of the data types that we have not talked about yet is called *dictionaries* (``dict``). If you think about what a 'real' dictionary is, it is a list of words, and for each word is a definition. Similarly, in Python, we can assign definitions (or 'values'), to words (or 'keywords').

# Dictionaries are defined using curly brackets ``{}``:

# In[ ]:


d = {'a':1, 'b':2, 'c':3}


# Items are accessed using square brackets and the 'key':

# In[ ]:


d['a']


# In[ ]:


d['c']


# Values can also be set this way:

# In[ ]:


d['r'] = 2.2


# In[ ]:


print(d)


# The keywords don't have to be strings, they can be many (but not all) Python objects:

# In[ ]:


e = {}
e['a_string'] = 3.3
e[3445] = 2.2
e[complex(2,1)] = 'value'


# In[ ]:


print(e)


# In[ ]:


e[3445]


# If you try and access an element that does not exist, you will get a ``KeyError``:

# In[ ]:


e[4]


# Also, note that dictionaries do *not* know about order, so there is no 'first' or 'last' element.

# It is easy to check if a specific key is in a dictionary, using the ``in`` operator:

# In[ ]:


"a" in d


# In[ ]:


"t" in d


# Note that this also works for lists:

# In[ ]:


3 in [1,2,3]


# ## Exercise 2

# Try making a dictionary to translate a few English words into Spanish and try using it!

# perro = dog; gato = cat; hola = hello; star = estrella; adios = goodbye; por favor = please; gracias = thank you; 
# lo siento = sorry

# In[ ]:



# your solution here


# ## Exercise 3 - Cryptography

# Cryptography is the study of how to make messages secret or how to read secret messages. A very simple encryption technique is called the *Caesar cipher*, which you can read up more about [here](http://en.wikipedia.org/wiki/Caesar_cipher). The basic idea is that each letter is replaced by a letter that is a certain number of letters away, so for example if the shift was 2, then A would become C, B would become D, etc. (and Z will become B).

# As we will learn in more detail tomorrow, you can write your own functions in Python, the simplest of which can take the form:

# In[ ]:


def encrypt(string):
    # do things here
    return new_string


# Write a function that given a string and a shift, will return the encrypted string for that shift. Note that the same function can be used to decrypt a message, by passing it a negative shift. 
# 
# The rules are: you should only accept and return lowercase letters, and spaces should not be changed.
# 
# Then, decrypt the following message, which was encrypted with a shift of 13:
#     
#     pbatenghyngvbaf lbh unir fhpprrqrq va qrpelcgvat gur fgevat    
#     
# Now if you are up for a challenge, try and decrypt this **and** find the shift:
#     
#     gwc uivioml bw nqvl bpm zqopb apqnb
#     
# Hint: there are several ways you can convert between letters and numbers. One is to use the built-in functions ``chr`` and ``ord`` (and remember you can find out more about a function by using ``?`` in IPython). Another is to set up the alphabet in a string and use item access (``[4]``) to convert from numbers to letters, and the ``index`` method to convert from letters to numbers.

# In[1]:


# you solution here
alpha = 'abcdefghijklmnopqrstuvwxyz'
message = "pbatenghyngvbaf lbh unir fhpprrqrq va qrpelcgvat gur fgevat"

def encrypt(letter,s):
  shift = int(s)
  if letter == ' ':
    new_char = ' '
    return new_char

  for char in alpha:
    
    if letter == char:
      new_char = alpha.index(char)
      int_char = int(new_char)
      int_char += shift
      if int_char > 25:
        int_char -= 26
      new_char = alpha[int_char]

      return new_char


cypher = ''
for x in message:
  new = encrypt(x,13)
  cypher += new
  # print(cypher)

print(cypher)


# In[ ]:





# In[ ]:




