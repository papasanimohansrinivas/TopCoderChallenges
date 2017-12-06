
# coding: utf-8

# In[37]:


import pickle 

from pandas import DataFrame,read_excel


# ### _filepaths for serialised model and test files_
# 
# ### 

# In[85]:


test_file_path = "C:/Users/papasani.mohan/Pictures/TopCoder/Debitron Challenge/Testing Data/"

persistent_model_path = "C:/Users/papasani.mohan/Pictures/TopCoder/Debitron Challenge/Scripts/Serialised Models"


# In[86]:


test_file="testdata.xlsx"


# In[87]:


linear_model=pickle.load(open("C:/Users/papasani.mohan/Pictures/TopCoder/Debitron Challenge/Scripts/Serialised Models/LogRmodel_1"))


# In[88]:


excel_file = read_excel(test_file_path+test_file)
# df=DataFrame(read_excel(test_file_path+test_file))


# In[89]:


df=DataFrame(excel_file)


# ### drop rows with nan values 

# In[165]:


clm_names = ['balance'+str(l) for l in xrange(60,0,-1)]+['SAVING_BALANCE']

df=df.dropna()

res = linear_model.predict(df[clm_names])


# In[167]:


df['BOT_JOB_RESULT']=["WILL_GET_APPROVED" if int(t)==1 else "WILL_GET_REJECTED" for t in res]


# In[170]:


df_1 = df.loc[df['BOT_JOB_RESULT']=='WILL_GET_APPROVED']


# In[171]:


df_2 = df.loc[df['BOT_JOB_RESULT']=='WILL_GET_REJECTED']


# In[179]:


df_2.head()


# In[173]:


df_1.sort_values(by='AMOUNT_DUE', ascending=0)


# In[174]:


df_2.sort_values(by='AMOUNT_DUE',ascending=0)


# In[175]:


import pandas


# In[177]:


DDB=pandas.concat([df_2,df_1])


# In[178]:


DDB.to_excel("C:/Users/papasani.mohan/Pictures/TopCoder/Debitron Challenge/RESULT/DDB.xlsx")

