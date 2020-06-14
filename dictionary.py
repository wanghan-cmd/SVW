#!/usr/bin/env python
# coding: utf-8

# In[2]:


#访问字典位置
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0['points'])


# In[4]:


#使用字典中值
alien_0 = {"color": "green", "points": 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


# In[6]:


#增加字典元素（键-值）
alien_0 = {"color": "green", "points": 5}
print(alien_0)

alien_0["x_position"]=0
alien_0["y_position"]=25
print(alien_0)


# In[7]:


#空字典：存储用户提供的数据或者能自动生成大量键-值代码时
alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)


# In[10]:


#修改字典中的值
alien_0 = {'color': 'green','points': 5}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


# In[21]:


#增加alien速度
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
#定义一个新位置：老位置加增量
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("\nNew x-position: " +str(alien_0['x_position']) )


# In[22]:


#删除键-值
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)


# In[23]:


#类似对象组成的字典
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
#最后一组键-值后最好加逗号，为以后在下一行添加键-值做准备
    'phil': 'python',
#花括号前需要缩进4行
    }
#print分成多行
print("Sarah's favorite language is " +
     favorite_language['sarah'].title() +
     ".")


# In[23]:


#类似对象组成的字典
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
#最后一组键-值后最好加逗号，为以后在下一行添加键-值做准备
    'phil': 'python',
#花括号前需要缩进4行
    }
#print分成多行
print("Sarah's favorite language is " +
     favorite_language['sarah'].title() +
     ".")


# In[24]:


#遍历字典中所有的键-值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
#用for循环来遍历，键-值的名称，可使用任何名称（k,v）.
#字典名+方法items()是返回字典中的一个键-值对列表
for k, v in user_0.items():
    print("\nKey: " + k)
    print("Value: " + v)


# In[28]:


#类似对象组成的字典
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name,language in favorite_language.items():
    print(name.title() + "'s favorite language is "
          + language.title() + ".\n")


# In[30]:


#遍历所有键，且按字母顺序打印
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_language.keys()):
    print(name.title() + ", thank you for taking the poll" + ".\n")


# In[31]:


#遍历所有值，并去除重复值
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
#用set()集合去除重复值
for language in set(favorite_language.values()):
    print(language.title())

