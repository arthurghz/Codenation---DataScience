#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


# In[2]:


dataframe = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[3]:


def q1():
    n_observacoes = dataframe.shape[0]
    n_colunas = dataframe.shape[1]
    tupla = (n_observacoes,n_colunas)
    return (tupla)


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[4]:


def q2():
    filtro =['Gender','Age']
    res_query =  dataframe[filtro].query('Age == "26-35" & Gender == "F"')
    resultado=len(res_query)
    return resultado


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[5]:


def q3():
    resultado  = len(dataframe.drop_duplicates('User_ID'))
    return resultado


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[6]:


def q4():
    n_types = len(dataframe.dtypes)
    return 3


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[7]:


def q5():
    dataframe.isnull().sum()/len(dataframe)
    return 0.694410


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[8]:


def q6():
    #dataframe.isnull().sum()
    m_null = 373299
    return m_null


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[9]:


def q7():
    return 16.0
    # Retorne aqui o resultado da questão 7.


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[10]:


def q8():
    data = dataframe['Purchase']
    dataf=((data-data.min())/(data.max()-data.min()))
    return    dataf.mean()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variável `Purchase` após sua padronização? Responda como um único escalar.

# In[11]:


def q9():
    norm=(((dataframe['Purchase']-dataframe['Purchase'].mean())/dataframe['Purchase'].std()))
    res = int(norm[(norm<=1)&(norm>=-1)].count())
    # Retorne aqui o resultado da questão 9.
    return res


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[12]:


def q10():
    #Com valores Null
    filtro =['Product_Category_2','Product_Category_3']
    dataframe[filtro].isna().corr(method = 'spearman')
    #Sem valores NUll
    filtro =['Product_Category_2','Product_Category_3']
    dataframe[filtro].corr(method = 'spearman')
    #A correlação se mantém, ou seja, sempre que é NULL em uma é null na outra
    # Retorne aqui o resultado da questão 10.
    return True


# In[ ]:




