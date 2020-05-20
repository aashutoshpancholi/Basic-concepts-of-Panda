import pandas as pd
import numpy as np


#IMPORTING DATA into spyder

cars_data = pd.read_csv('FILE_NAME.csv' , index_col = 0 , na_values = ["??" , "????"])


#CREATE COPY of ORIGIONAL DATA

#SYNTAX = NEW FILE NAME = OLD FILE NAME.COPY()

cars_data_copy = cars_data.copy()

#CORRELATION

#SYNTAX = DATAFRAME_NAME.CORR(SELF , METHOD = "pearson")

numerical_data = cars_data_copy.select_dtypes(exclude = [object])

print(numerical_data.shape)


#CORRELATION between NUMERICAL VARIABLES

corr_matrix = numerical_data.corr()