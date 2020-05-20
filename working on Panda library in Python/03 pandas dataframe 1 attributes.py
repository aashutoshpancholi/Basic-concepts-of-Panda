# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:11:40 2020

@author: AaShUtOsH
"""


import pandas as pd
import numpy as np

#HOW TO IMPORT DATA INTO SPYDER

cars_data = pd.read_csv("FILE_NAME".csv)

#COPY of ORIGIONAL DATA

#     1.   SHALLOW COPY (ANY changes made in COPY will also BE CHANGED in ORIGIONAL)

samp = cars_data.copy(deep=False)

samp = cars_data

#     2.   DEEP COPY (ANY changes made in COPY will NOT BE CHANGED in ORIGIONAL)

samp1 = cars_data.copy(deep=True)

samp1 = cars_data


#ATTRIBUTES OF DATA FRAME


#TO GET THE INDEX (ROW LABELS) OF A DATA FRAME

#SYNTAX = DATAFRAME_NAME.index

cars_data.index

#TO GET THE INDEX (COLUMN LABELS) OF A DATA FRAME

#SYNTAX = DATAFRAME_NAME.columns

cars_data.columns

#TO GET THE TOTAL NUMBER OF ELEMENTS OF A DATA FRAME

#SYNTAX = DATAFRAME_NAME.size

cars_data.size

#TO GET THE DIMENTIONALITY OF A DATA FRAME

#SYNTAX = DATAFRAME_NAME.sape

cars_data.shape

#TO GET THE MEMORY USAGE OF EACH COLUMN IN BYTES OF A DATA FRAME

#SYNTAX = DATAFRAME_NAME.memory_usage()

cars_data.memory_usage()

#TO GET THE NUMBER OF AXES ARRAY DIMENSIONAL OF A DATA FRAME

#SYNTAX = DATAFRAME_NAME.ndim

cars_data.ndim
