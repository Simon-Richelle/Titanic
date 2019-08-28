
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
import re
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_val_score


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
