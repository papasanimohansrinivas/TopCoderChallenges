
# coding: utf-8

# # Debitron Machine Learning NoteBook / TopCoder
# 
# ### Challenge asks us to maximise daily collected Amount_Due
# 
# ##### Initially I wanted to see whether Bot will fail with the task or not given the balance from my model

# ### Requirements:
# ####      Python 2.7 
# #### Sklearn 
# #### Pandas
# #### Pickle
# #### Anaconda or Jupyter NoteBook for running this notebook

# 
# 
# ### I am going to use this notebook for exploratory purposes and serialise models depending on the results

# ### Serialised models are always found in the 'Serialised Model' and you could use them in production or validation

# In[171]:


from __future__ import division

import sklearn


# ### get file paths for given project files
# 
# 
# 
# ### make sure change below path style  according to system you are using
# 
# ### I am running this code on windows so paths are written in that manner 

# In[172]:


file_path='C:/Users/papasani.mohan/Pictures/TopCoder/Debitron Challenge/Training Data/'


# In[173]:


import pandas as pd


# In[174]:


file_1 = file_path+'CompiledDDBs_Challenge_v3_2.xlsx'
file_2 = file_path+'DataDictionary_Challenge_v2.xlsx'


# In[175]:


read_excel=pd.read_excel


# In[176]:


file_=read_excel(file_1)


# ### Data Display

# In[167]:


file_.head(7)
# file__.head(12)


# ### Labelling the data

# In[177]:


# map(type,file_['CLIENT_ID'])
file_['BOT_JOB']=[1 if u=='APPROVED' else 0 for u in file_['BOT_JOB'] ]


# In[178]:



file__=read_excel(file_2)


# In[179]:


file__.head(10)


# In[180]:


def normalise(column_name,dataframe):
    normalized_df=(dataframe[column_name]-dataframe[column_name].min())/(dataframe[column_name].max()-dataframe[column_name].min())
    return normalized_df


# ##  Model_1
# 
# ##### Seperate Columns  balance0,balance1, from file_ and load them ... into seperate dataframe
# 

# ## Data ....
# 
# #### Take  desired columns from 'file_'  dataframe and combine them into a new 'df' dataframe
# 
# 

# In[181]:


df=file_[['balance'+str(ind) for ind in xrange(60,0,-1)]+['SAVING_BALANCE']+['BOT_JOB']]


# ### Normalise DataFrame
# 
# #### I normalised dataframe so that algorithm runs smooth
# 
# #### below is z means normalisation
# 

# In[182]:


df1 = (df - df.mean())/df.std()


# In[183]:


def display_df1():
    display(df1)


# In[184]:


df2 = (df-df.min())/(df.max()-df.min())


# In[185]:


# display(df2)


# #### I split data set as 2:3 as a sample 

# In[186]:


train,test = df2[:20000],df2[20000:]


# In[187]:


# train


# ### LogisticRegression
# 
# ##### My belief is that with enough data u can predict well with Logistic Regression
# 
# 
# 

# ### sklearn is a Machine Learning library  / module 
# 
# #### If you don't have sklearn module you can follow instructions from here
# __[sklearn installation](http://scikit-learn.org/stable/install.html )__
# 

# In[188]:


from sklearn.linear_model import LogisticRegression

# from sklearn.linear_model import LinearRegression

from sklearn.naive_bayes import GaussianNB


# #### below code  initiate LogisticRegression model 

# In[189]:



model=LogisticRegression()

model_2 = GaussianNB()

names =[column for column in  train.columns if column!='BOT_JOB']


# #### Drop any nan values or missing values from dataFrame 
# 
# ### below code elimantes any nan values in dataFrame
# 
# ### all these functions are from sklearn library

# In[190]:



train=train.dropna()

test = test.dropna()


# In[191]:


def validate_nans():
    
    new_df = train.isnull()
    for b in new_df:
        i=0
        for a in new_df[b]:
            if a==True:
                print "gode save england",i,new_df[b].iloc[i],spare[b].iloc[i]
                pass
            i+=1
        


# In[192]:


validate_nans()


# ### I now train the model with training data

# In[194]:


print len(names)

print names
model.fit(train[names],train['BOT_JOB'])

model_2.fit(train[names],train['BOT_JOB'])


# In[100]:


results=model.predict(test[names])
results_2 = model_2.predict(test[names])


# In[103]:


verify=test['BOT_JOB']


# ### I wrote a my own accuracy function 

# In[102]:


def model_accuracy(results,verify):
    
#     global results,verify
    
    assert len(verify)==len(results)
    
    ans = list(results)
    
    verify = list(verify)
    
    s=[1 if verify[j]==ans[j] else 0 for j in xrange(len(verify))]
    
    return ((sum(s)+0.0)/len(verify))*100

print "accuracy of my current model is:".upper(),model_accuracy(results_2,verify)
    


# ### Lets serialise the data 

# In[105]:

def demonstration_of_serialised_model():
    
    import pickle

    path= "C:/Users/papasani.mohan/Pictures/TopCoder/Debitron Challenge/Scripts/Serialised Models"


    # In[106]:


    pickle.dump(model,open(path+"/LogRmodel_1","wb"))


    # ### You could find serialised model for production in the  'Serialised Models' folder 

    # ### It's also  simple to load model from pickle library 

    # In[107]:


    ml=pickle.load(open(path+"/LogRmodel_1"))


    # In[108]:


    ml.predict(test[names])

