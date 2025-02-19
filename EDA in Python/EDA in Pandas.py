#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r'C:\Users\laqmaan\OneDrive\Desktop\python project\world_population.csv')
pd.set_option('display.float_format', lambda x: '%.2f' % x)
df


# In[3]:


df.info()


# In[4]:


df.describe()


# In[5]:


df.isnull().sum()


# In[6]:


df.nunique()


# In[7]:


df.sort_values(by = '2022 Population', ascending = False).head(10)


# In[8]:


df


# In[9]:


df.set_index('Continent')


# In[10]:


df.corr(numeric_only = True)


# In[11]:


sns.heatmap(df.corr(numeric_only = True), annot = True)
plt.show()


# In[12]:


df.groupby('Continent').mean(numeric_only = True).sort_values(by = '2022 Population', ascending = False)


# In[13]:


df[df['Continent'].str.contains('Oceania')]


# In[14]:


df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean(numeric_only = True).sort_values(by = '2022 Population', ascending = False)
df2


# In[15]:


df.columns


# In[16]:


df3 = df2.transpose()
df3


# In[17]:


df3.plot(figsize = (14,7))


# In[18]:


plt.show(kind = 'bar')


# In[20]:


df.boxplot(figsize = (20,10))


# In[21]:


df


# In[22]:


df.select_dtypes(include = 'float')


# In[23]:


df.select_dtypes(include = 'number')


# In[24]:


df.select_dtypes(include = 'object')


# In[25]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




