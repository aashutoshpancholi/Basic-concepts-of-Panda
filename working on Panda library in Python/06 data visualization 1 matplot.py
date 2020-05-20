import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

#IMPORTING DATA into spyder

cars_data = pd.read_csv('FILE_NAME.csv' , index_col = 0 , na_values = ["??" , "????"])


#REMOVE MISSING VALUES from data frame

#SYNTAX = DATAFRAME_NAME.DROPNA()

cars_data.dropna(axis = 0 , inplace = True)



#HOW TO DRAW SCATTER PLOT GRAPH

plt.scatter(cars_data['Age'] , cars_data['Prize'] , c = 'red')

plt.scatter('Scatter plot of Prize vs Age of the cars.')

plt.xlabel('Age(months)')
plt.ylabel('prize(Rs)')

plt.show()



#HOW TO DRAW HISTOGRAM GRAPH used for NUMERICAL VARIABLE

plt.hist(cars_data['KM'] , 
         color = 'green' , 
         edgecolor = 'black' 
         bins = 5)

plt.title('Histogram of Kilmeter.')

plt.xlabel('Kilometer')
plt.ylabel('Frequency')

plt.show()



#HOW TO DRAW BAR PLOT used for categorical variable

counts = [979 , 120 , 12]
fuelTypes = ('Petrol' , 'Diesel' , 'CNG')
index = np.arrange(len(fuelType))

plt.bar(index , counts , color = ['red' , 'blue' , 'cyan'])

plt.title('Bar plot graph of fuel types.')

plt.xlabel('Fuel Types')
plt.ylabel('Frequency')
plt.xticks(index , fuelType , rotation = 90)

plt.show()