import numpy as np
import pandas as pd
import random as r
import matplotlib.pyplot as plt
import seaborn as sn



"""
#f1=pd.read_csv(r"C:\Users\VENKATESH\OneDrive\Desktop\project\gender_submission.csv")
f2=pd.read_csv(r"C:\Users\VENKATESH\OneDrive\Desktop\project\train.csv")
#f3=pd.read_csv(r"C:\Users\VENKATESH\OneDrive\Desktop\project\test.csv")

data=pd.DataFrame(f2)
#d2=pd.DataFrame(f3)
#print(d1.columns)
#print(d2.columns)

data['Age'].fillna(r.choice(data['Age']), inplace=True)
data['Cabin'].fillna(r.choice(data['Cabin']), inplace=True)
data['Embarked'].fillna(r.choice(data['Embarked']), inplace=True)
data.to_csv('C:\Users\VENKATESH\OneDrive\Desktop\project\train.csv',index=False)
f2=pd.read_csv(r"C:\Users\VENKATESH\OneDrive\Desktop\project\train.csv")

data= pd.DataFrame(f2)
print(data.columns)

print(data.describe())

#a=s.barplot(y='PassengerId',x='Embarked', hue='Embarked', data=data, width=0.1)
#.set(text="Number of passengers embarked from each city")
a=s.countplot(x='Embarked',data=data,hue='Embarked')
#s.lineplot(x='Embarked',y='PassengerId', hue='Embarked', data=data)

a.legend(['Southampton','Cherbourg','Queenstown'],loc='upper right')
a.set_title('Number of passengers embarked from each city')
a.set(xlabel='Cities', ylabel='Number of passengers')

plt.show()

# displot chat for nu.of males and females
s.distplot(data.Age, kde=True, hist=True, hist_kws={'alpha':1} )
plt.show()

print('males surviveal data')
male=data[data['Sex']=='male']
print(sum(male['Survived']==1))
print(sum(male['Survived']==0))
female= data[data['Sex']=='female']
print('female survivals')
print(sum(female['Survived']==1))
print(sum(female['Survived']==0))