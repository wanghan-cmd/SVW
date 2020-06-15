#!/usr/bin/env python
# coding: utf-8

# In[14]:


# 对汽车投诉信息进行分析
import pandas as pd
from pandas import DataFrame
print("原始数据导入：")
CarData = DataFrame(pd.read_csv(r'C:\Users\MateBook 13\Desktop\Py_learning\Data_Engine_with_Python-master\L1\car_data_analyze\car_complain.csv'))
print(CarData)

#以逗号拆分problem
print("\n\n数据预处理：")
CarData = CarData.drop('problem',axis=1).join(CarData.problem.str.get_dummies(','))
print(CarData)

#将problem转换到每个对应的汽车品牌的行上，并计数
CarData_1 = CarData.melt(
    id_vars = CarData.columns[:7].to_list(),
    var_name = 'problem_type',
    value_name = 'count'
    )
CarData_1 = CarData_1[CarData_1['count']!=0]
print(CarData_1)


# In[26]:


#自定义函数，统计投诉总数
def Complain_count(dimension):
    s1 = CarData_1.groupby(dimension)['id'].nunique().sort_values(ascending = False).rename('投诉计数')
    s2 = CarData_1.groupby(dimension)['id'].count().sort_values(ascending = False).rename('投诉总数')
    s3 = (s2/s1).rename('平均投诉次数')
    return pd.DataFrame([s1,s2,s3]).T


# In[29]:


Complain_count(['brand'])


# In[31]:


Complain_count('car_model')


# In[30]:


#计算品牌和车型投诉总数
Complain_count(['brand','car_model'])

