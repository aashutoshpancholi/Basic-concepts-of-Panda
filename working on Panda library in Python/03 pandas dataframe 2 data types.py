import pandas as pd
import numpy as np


#DATA TYPES IN PANDAS

#     1.   INT64
#     2.   FLOAT64

#HERE ,  64 BIT refers to the MEMORY ALLOCATED TO STORE DATA in EACH CELL (64 bits = 8 BYTES)


#CHARACTER TYPES

#     1.   CATEGORY

#I)   A string variable consist of only a few different values.
#II)  Converting suchh a string variable to a categorical variable will save some memory.
#III) It takes on a limited , fixed number of possible values.

#     2.   OBJECT

#I)   The column will be assigned as object data type when it has mixed types (Number and Strings).
#II)  If a column contains "BLANK" , pandas will default to object data type.
#III) For string , length will not be fixed.





#HOW TO CHEKING DATA TYPES OF EACH COLUMN

#1): DTYPES returns a series with the data types of each column.

#SYNTAX = DATAFRAME_NAME.dtypes

cars_data.dtypes


#HOW TO COUNT OF UNIQUE DATA TYPES

#1): GET_DTYP_COUNTS() returns a series with the data types of each column.

#SYNTAX = DATAFRAME_NAME.get_dtype_counts()

cars_data.get_dtype_counts()


#HOW TO SELECT DATA based on DATA TYPES

#1): PANDAS.DATAFRAME.SELECT_DTYPES() 
# it returns a subset of the column from dataframe based on the column dtypes

#SYNTAX = PANDAS.SELECT_DTYPES(INCLUDE = none , exclude = none)

cars_data.select_dtypes(exclude=[object])


#HOW TO CONCISE SUMMARY OF DATA FRAME

#1): INFO() it returns a concise summary of a dataframe 
# I.G. : data type of index , data types of column , count of non null values , memory usage.

#SYNTAX = DATAFRAME_NAME.INFO()

cars_data.info()


#HOW TO FIND UNIQUE ELEMENTS OF COLUUMNS

#1): UNIQUE() it returns a unique element of a column 

#SYNTAX = NUMPY.UNIQUE(ARRAY)

print(np.unique(DATAFRAME_NAME['COLUMN_NAME']))

print(np.unique(cars_data['Doors']))