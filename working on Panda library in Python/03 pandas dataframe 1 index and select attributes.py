# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:07:53 2020

@author: AaShUtOsH
"""


import pandas as pd
import numpy as np

#INDEXING and SELECTING DATA

#HEAD returns FIRST N ROWS from the data frame (N-1 so 6 means return 5 rows)

#SYNTAX = DATAFRAME_NAME.head([n])

cars_data.head(6)

#TAIL returns LAST N ROWS from the data frame

#SYNTAX = DATAFRAME_NAME.teil([n])

cars_data.head(6)

#TO ACCESS A SCALAR VALUE by using AT and IAT

#     1.   AT : provides LABEL BASED SCALAR LOOKUPS

#SYNTAX = DATAFRAME_NAME.at[ROW LABEL , "COLUMN LABEL"]

cars_data.at[4 , "FUELTYPE"]

#     2.   IAT : provides INTEGER BASED SCALAR LOOKUPS

#SYNTAX = DATAFRAME_NAME.iat[ROW NUMBER , "COLUMN NUMBER"]

cars_data.iat[4 , 6]

#TO ACCESS A GROUP OF ROWS and COLUMNS by LABELS .loc[] can be used.

#SYNTAX = DATAFRAME_NAME.loc[: , "COLUMN LABEL"]

cars_data.at[: , "FUELTYPE"]