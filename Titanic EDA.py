
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import data : training and test set

df_train = pd.read_csv("data-train.csv")
df_test = pd.read_csv("data-test.csv")

# Join Datasets for EDA

df_train['dataset'] = 'training'
df_test['dataset'] = 'test'

df = df_train.append(df_test)
df.reset_index(inplace=True)


print(df.columns)
print('\n')
print('===========================================================================')
print('\n')
print(df.shape)
print('\n')
print('===========================================================================')
print('\n')
print(df.iloc[:, [0,1,2,5,6]].describe())
print(df.iloc[:, [7,9]].describe())
print(df.iloc[:, [3,4,8,10]].describe())

print('\n')
print('===========================================================================')
print('\n')

# identifying important features in variables (missing values, number of unique values
#df_missing = pd.DataFrame({'column': df.columns, 'Data type': df.dtypes ,'Missing': df.isnull().sum(), 'unique_val': df.nunique()})
#print(df_missing)

## Data vizualization
fig, ax = plt.subplots(4, 3, figsize=(30, 30))
sns.countplot(df['Survived'], ax=ax[0, 0])
ax[0, 0].set(title='2014 Revenue', xlabel='Total Revenue', ylabel='Customer')
sns.countplot(df['Pclass'], hue=df['Sex'], ax=ax[0, 1])
sns.countplot(df['Survived'], hue=df['Sex'], ax=ax[0, 2])
sns.distplot(df['Age'].dropna(), kde=False, ax=ax[1, 0])
sns.distplot(df['Fare'].dropna(), kde=False, ax=ax[1, 1])
sns.boxplot(x=df['Pclass'], y=df['Fare'].dropna(), ax=ax[1, 2])
sns.countplot(df['Embarked'], ax=ax[2, 1])
sns.countplot(df['Embarked'], hue=df['Survived'], ax=ax[2, 2])
sns.violinplot(x='Survived', y='Age', data=df, ax=ax[3, 0])
sns.violinplot(x='Survived', y=(df['Parch']+df['SibSp']), data=df, ax=ax[3, 1])
sns.boxplot(x=df['Survived'], y=(df['SibSp']+df['Parch']).dropna(), ax=ax[3, 2])
