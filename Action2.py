#!/usr/bin/env python
# coding: utf-8

# In[24]:


#使用pandas处理数据
import pandas as pd
#引入Series和DataFrame
from pandas import Series,DataFrame
#创建数据
data = {'语文':[68,95,98,90,80],
        '数学':[65,76,86,88,90],
        '英语':[30,98,88,77,90]
       }
#生成DataFrame
df = DataFrame(data,index = ['张飞','关羽','刘备','典韦','许褚'])
#成绩统计分析
df1 = df.describe().loc[['mean','max','min','std']]
print("成绩统计分析：")
print(df1)

#按总分排名
df['总分'] = df.sum(axis=1)
df['名次'] = df['总分'].rank(ascending=0)
df2=df.sort_values('名次')
print('\n')
print("成绩总分排名:")
print(df2)

