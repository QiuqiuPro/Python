
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import sklearn
import sklearn.cross_validation as cv
import sklearn.grid_search as gs
import sklearn.feature_extraction.text as text
import sklearn.naive_bayes as nb
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:

df = pd.read_csv('data/troll.csv')


# In[3]:

df[['Insult', 'Comment']].tail()


# In[ ]:



