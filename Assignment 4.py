#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = [[2,35],[4,60],[5,20],[3,50],[6,50],[5,55],[7,60]]

df = pd.DataFrame(data, columns=['Weight', 'Price'])


# In[2]:


df


# # Task 01:
# Your objective is to manually compute the slope (M) and y-intercept (C) using
# Ordinary Least Squares Linear Regression. Once determined, apply these values to
# predict the price when the vegetable weight is 6.

# In[3]:


x=df['Weight']
y=df['Price'] 


# In[4]:


import numpy as np
np.mean(x)


# In[5]:


np.mean(y)


# In[6]:


dev_x = x - np.mean(x)
dev_y = y - np.mean(y)


# In[7]:


m=np.sum(  (dev_x ) * (dev_y  ) ) / np.sum( (dev_x**2 ) )
m


# In[8]:


c=np.mean(y)-m*np.mean(x)
c


# In[9]:


predicted_price = m* 6 + c   # Predicted Price For Weight = 6
print("Predicted Price For Weight 6 = ",predicted_price)


# # Task 02:
# Compute the residuals for each data point.

# In[10]:


x=df.drop('Price',axis=1) # drop Price from df so  X = only Weight 
y=df.drop('Weight',axis=1) # drop Weight from df so Y  = only Price


# In[11]:


from sklearn.linear_model import LinearRegression
reg=LinearRegression()


# In[12]:


reg.fit(x,y)


# In[13]:


df['predicted_price']=reg.predict(x) 


# In[14]:


df['residuals']=df['Price'] - df['predicted_price']


# In[15]:


print("After Computing the residuals for each data point  :")
df


# # Task 03:
# Calculate both the Mean Squared Error (MSE) and Mean Absolute Error (MAE).

# In[16]:


from sklearn.metrics import mean_squared_error 
mse=mean_squared_error(df['Price'],df['predicted_price'])
print('Mean Squared Error (MSE) = ',mse)


# In[17]:


from sklearn.metrics import mean_absolute_error
mae=mean_absolute_error(df['Price'],df['predicted_price'])
print('Mean Absolute Error (MAE) = ',mae)


# # Final Task:
# Generate an Excel file for the given dataset.

# In[18]:


import pandas as pd
data=pd.DataFrame(df)


# In[23]:


data.to_excel("Assignment_4.xlsx")


# In[24]:


data


# In[ ]:




