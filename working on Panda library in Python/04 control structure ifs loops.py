import pandas as pd
import numpy as np

#INSERT a NEW COLUMN

#SYNTAX = DATAFRAME_NAME.INSERT()

car_data.insert(10 , "COLUMN_NAME" , "")

#EXAMPLE of IF ELIF ELSE nad FOR LOOP

for i in range(0 , len(car_data['prize']) , 1):
    if (car_data['prize'][i] <= 10000):
        car_data['prize_class'][i] = "LOW"
    elif (car_data['prize'][i] > 20000):
        car_data['prize_class'][i] = "HIGH"
    else:
        car_data['prize_class'][i] = "MEDIUM"
        
#EXAMPLE OF WHILE LOOP
        
i = 0

while i < len(car_data['prize']):
    if (car_data['prize'][i] <= 10000):
        car_data['prize_class'][i] = "LOW"
    elif (car_data['prize'][i] > 20000):
        car_data['prize_class'][i] = "HIGH"
    else:
        car_data['prize_class'][i] = "MEDIUM"
        
    i = i + 1
    
    
#EXAMPLE OF WHILE LOOP with SERIES
    
#SERIES.VALUE_COUNTS() returns series containg countof unique values
    
car_data['prize_class'].values_count()