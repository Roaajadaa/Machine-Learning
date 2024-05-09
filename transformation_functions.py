#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np


# In[6]:


def Reciprocal_transformation (feature_to_tranforme) :
    feature_Reciprocal_transformation =   1 / feature_to_tranforme
    return feature_Reciprocal_transformation 


# In[7]:


def square_root_transformation (feature_to_tranforme) :
    feature_square_root_transformation = feature_to_tranforme**(1/2)
    return feature_square_root_transformation 


# In[8]:


def log_transformation(feature_to_transform):
    return np.log(feature_to_transform)


# In[ ]:




