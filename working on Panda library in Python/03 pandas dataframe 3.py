import pandas as pd
import numpy as np


#IMPORTING DATA into spyder

cars_data = pd.read_csv('FILE_NAME.csv' , index_col = 0 , na_values = ["??" , "????"])


#CONVERTING VARIABLE'S DATA TYPES

#1): ASTYPE is used toexpliicitly convert types from one to another

#SYNTAX = DATAFRAME_NAME.astype(dtype)

#cars_data['VARIABLE_NAME'] = cars_data['VARIABLE_NAME'].astype('DATATYPE_NAME in which convert')

cars_data['color'] = cars_data['color'].astype('object')


#CATEGORY vs OBJECT DATA TYPE

#1): NBYTES() is used to get the total BYTES consumed by elements f the COLUMNS

#SYNTAX = NDARRAY.NBYTES

#if OBJECT DATA TYPE :

cars_data['FuelType'].nbytes

#if CATEGORY DATA TYPE :

cars_data['FuelType'].astype('category').nbytes


#REPLACE the values

#1): REPLACE()  is used to replace a value with desired value

#SYNTAX = DATAFRAME_NAME.REPLACE([TO_REPLACE , VALUE])

cars_data['Doors'].replace('three' , 3 , inplace = True)


#DETECT THE MISSING VALUES

#1): DATAFRAME.ISNULL.SUM()  is used to check the count of missing values present in each column

#SYNTAX = DATAFRAME_NAME.ISNULL.SUM()

cars_data.isnull().sum()