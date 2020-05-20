import os
import pandas as pd
import numpy as np


#IMPORTING DATA into spyder

cars_data = pd.read_csv('FILE_NAME.csv' , index_col = 0 , na_values = ["??" , "????"])


#CREATE COPY of ORIGIONAL DATA

#SYNTAX = NEW FILE NAME = OLD FILE NAME.COPY()

cars_data_copy = cars_data.copy()
cars_data_copy2 = cars_data_copy.copy()

#IDENTIFY THE MISSING VALUES

#SYNTAX = DATAFRAME_NAME.ISNA.SUM()    and    DATAFRAME_NAME.ISNULL.SUM()

cars_data_copy.isna().sum()
cars_data_copy.isnall.sum()

#SUBSET THE ROWS THAT HAVE ONE OR MORE MISSING VALUES

missing= cars_data_copy[cars_data_copy.isnull().any(axis=1)]


#APPROACHE TO FILL THE MISSING VALUES

#     1):   By MEAN / MEDIAN in case of NUMERICAL VARIABLE
#     2):   By CLASS which has MAXIMUM COUNT in case of CATEGORICAL VARIABLE


#IMPUTING MISSING VALUES

#SYNTAX = DATAFRAME_NAME.DESCRIBE()


#1):     IMPUTING MISSING VALUES of 'Age' by using MEAN

cars_data_copy['Age'].mean()

#IMPUTING MISSING VALUES of 'Age' by using SPECIFIED VALUE

#SYNTAX = DATAFRAME_NAME.FILLNA()

cars_data_copy['Age'].fillna(cars_data_copy['Age'].mean() , inpalce = True)


#2):     IMPUTING MISSING VALUES of 'KM' by using MEDIAN

cars_data_copy['KM'].median()

#IMPUTING MISSING VALUES of 'KM' by using SPECIFIED VALUE

#SYNTAX = DATAFRAME_NAME.FILLNA()

cars_data_copy['KM'].fillna(cars_data_copy['KM'].median() , inpalce = True)


#1):     IMPUTING MISSING VALUES of 'HP' by using MEAN

cars_data_copy['HP'].mean()

#IMPUTING MISSING VALUES of 'HP' by using SPECIFIED VALUE

#SYNTAX = DATAFRAME_NAME.FILLNA()

cars_data_copy['HP'].fillna(cars_data_copy['HP'].mean() , inpalce = True)

#3):     IMPUTING MISSING VALUES of 'FUELTYPE' by using SERIES.VALUE_COUNTS()

cars_data_copy['FuelType'].value_counts()

#IMPUTING MISSING VALUES of 'FUELTYPE' by using MODE

#SYNTAX = SERIES.VALUE_COUNT(0)

cars_data_copy['FuelType'].value_counts().index=[0]

#IMPUTING MISSING VALUES of 'FUELTYPE' by using SPECIFIED VALUE

#SYNTAX = DATAFRAME_NAME.FILLNA()

cars_data_copy['FuelType'].fillna(cars_data_copy['FuelType'].value_counts().index[0] 
                                  , inpalce = True)


#IMPUTING MISSING VALUES using LAMBDA FUNCTIONS for both NUMERICAL and CATEGORICAL VARIABLES

cars_data_copy2 = cars_data_copy2.apply(lambda x:x.fillna(x.mean()) \
                                        if x.dtype=='float' \
                                        else x.fillna(x.value_counts().index[0]))
