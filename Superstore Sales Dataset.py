#!/usr/bin/env python
# coding: utf-8

# # Superstore Sales Dataset

# In[59]:


import pandas as pd # Data Manipulation and Analysis
import numpy as np # Linear Algebra
import matplotlib.pyplot as plt # Data Manipulation
import seaborn as sns # Data Manipulation 
import plotly.express as px
import warnings
warnings.filterwarnings('ignore') # Ignore warning


# In[60]:


df = pd.read_csv(r'c:\Users\pawar\Downloads\train.csv') 
#To load the csv file in jupyter notebook assuming your dataset is a CSV file named 'train.csv'


# In[61]:


df.head() # First Five rows of the dataset


# In[5]:


df.info() # Information about the dataset


# In[6]:


df.shape # shape of the dataset


#  9800 rows & 18 columns

# In[7]:


df.describe() # Summary Statistics of numerical columns


# In[8]:


df.dtypes # Data Types of columns 


# In[9]:


df.isnull().sum() # Missing Values in the dataset


# In[10]:


df.drop(columns=['Postal Code'], inplace=True) # Drop is used for to drop a specific column 


# In[11]:


df.duplicated().sum() # Count the number of duplicated rows in dataframe


# # Univariate Analysis(Single Variable Analysis):

# Univariate analysis is the simplest form of statistical analysis. It involves looking at one variable at a time to 
# understand the data distribution

# In[21]:


sns.countplot(data=df, x='Segment',palette ='Set3')
plt.title('Bar Plot of Segment')
plt.show()


# In[28]:


sns.countplot(data=df, x='Ship Mode',palette ='Set2')
plt.title('Bar Plot of Ship Mode')
plt.show()


# In[38]:


sns.countplot(data=df, x='Category',palette ='Set3') # 
plt.title('Bar Plot of Category')
plt.show()


# In[47]:


plt.figure(figsize = (15,5))
order= df['State'].value_counts().index
sns.countplot(data=df, x='State',order=order,palette='plasma')
plt.title("Distribution of State")
plt.xticks(rotation=90)
plt.show()


# In[64]:


plt.figure(figsize=(15, 5))
top_cities = df['City'].value_counts().head(10)
sns.barplot(x=top_cities.index, y=top_cities.values, palette='magma')
plt.title("Distribution of Top 20 Cities")
plt.xticks(rotation=90)
plt.show()


# # Bivariate Analysis(Multiple Variable Analyis)

# The Bivariate looks at the relationship between two variables, while multivariate analysis looks at the relationships 
# between multiple variables.

# In[54]:


heatmap_data = df.pivot_table(index='Segment', columns='Category', values='Sales', aggfunc='sum')
plt.figure(figsize=(10,6))
sns.heatmap(heatmap_data, annot=True, cmap='viridis', fmt='.0f', cbar_kws={'label':'Total Sales'})
plt.title("Segment Sales by Product Category")
plt.show()


# In[58]:


df.summary = df.groupby(['Category', 'Sub-Category',])['Sales'].sum().reset_index()
df.summary


# In[63]:


# Summarize the Sales data by Category, Ship Mode, and Sub-Category
df_summary = df.groupby(['Category', 'Ship Mode', 'Region'])['Sales'].sum().reset_index()

# Create a treemap
fig = px.treemap(
    df_summary,
    path=['Category', 'Ship Mode', 'Region'],
    values='Sales',
)
fig.show()


# In[ ]:




