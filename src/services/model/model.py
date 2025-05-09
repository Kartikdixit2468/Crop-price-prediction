# Made by Kartik Dixit 

# Importing Packages
import pandas as pd
import numpy as np
import category_encoders as ce
from sklearn.model_selection import train_test_split
from pycaret.regression import *
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import pandas_profiling as pp
import matplotlib.pyplot as plt
import seaborn as sns


# Reading the data
df = pd.read_csv("../input/crop-price-prediction/corn yield.csv")

# For analu=ysing data (Optional)   # checkout it on jupyter notebook for better representation and understanding
df.head()
df.isnull().sum()

for i in df:
    print(i,df[i].value_counts(),sep="\n",end="\n")


# Filtering Data
cols_to_be_removed = ["Program","Week Ending","Ag District","Ag District Code","County","County ANSI","Zip Code","Region","Watershed","CV (%)","Domain Category","Commodity","Geo Level","watershed_code","Domain"]

df.drop(columns=cols_to_be_removed,axis = 1,inplace=True)
prof = pp.ProfileReport(df)



