
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

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
df_missing = pd.DataFrame({'column': df.columns, 'Data type': df.dtypes ,'Missing': df.isnull().sum(), 'unique_val': df.nunique()})
print(df_missing)
