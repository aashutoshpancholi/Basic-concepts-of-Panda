import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

#IMPORTING DATA into spyder

cars_data = pd.read_csv('FILE_NAME.csv' , index_col = 0 , na_values = ["??" , "????"])

#REMOVE MISSING VALUES from data frame

#SYNTAX = DATAFRAME_NAME.DROPNA()

cars_data.dropna(axis = 0 , inplace = True)


#SCATTER PLOT of PRIZE VS AGE with DEFAULT ARGUMENTS.

sns.set(style = 'darkgrid')

sns.regplot(x=cars_data['Age'] , y=cars_data['Prize'] , marker = "*" , fit_reg = False)

#SCATTER PLOT of PRIZE VS AGE by FuelType

sns.lmplot(x='Age' , y='Prize' , data=cars_data ,
           fit_reg=False , hue = 'FuelType' , 
           legend  True , palette='set1')


#HISTOGRAM wit DEFAULT KERNEL DENSITY ESTIMATE

sns.distplot(cars_data['Age'] , kde = False , bins = 5)



#BAR PLOT of FREQUENCY DISTRIBUTION OF FUEL TYPE OF THE CARS

sns.countplot(x='fuelType' , data = cars_data)



#GROUPED BAR PLOT of FUEL TYPE and AUTOMATIC

sns.countplot(x='fuelType' , data = cars_data , hue = 'Automatic')

pd.crosstab(index = cars_data['Automatic'] , 
            columns = cars_data['FuelTypes'] , 
            dropna = True)



#BOX AND WHISKERS PLOT - NUMRICAL VARIABLE of prize to visualize interpret five number summary

sns.boxplot(y=cars_data['Prize'])


#BOX AND WHISKERS PLOT - NUMRICAL and CATEGORICAL VARIABLE

sns.boxplot(x = cars_data['FuelType'] , y=cars_data['Prize'])


#GROUPED BOX and WHISKERS PLOT of PRIZE vs FUELTYPE and AUTOMATIC

sns.boxplot(x = 'FuelType' , y=cars_data['Prize'] , 
            hue = 'Automatic' , data = cars_data)



#BOX WHISKERS PLOT and HISTOGRAM on the same window

f,(ax_box , ax_hist) = plt.subplots(2 , gridspec_kw={"height_ratios": (.15 , .85)})

sns.boxplot(cars_data["Prize"] , ax = ax_box)

sns.distplot(cars_data["Prize"] , ax = ax_hist , kde = False)



#PAIR WISE PLOTS

sns.pairplot(cars_data , kind  "scatter" , hue = "FuelType")
plt.show()