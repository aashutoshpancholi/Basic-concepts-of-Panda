import pandas as pd
import numpy as np


#IMPORTING DATA into spyder

cars_data = pd.read_csv('FILE_NAME.csv' , index_col = 0 , na_values = ["??" , "????"])


#CREATE COPY of ORIGIONAL DATA

#SYNTAX = NEW FILE NAME = OLD FILE NAME.COPY()

cars_data_copy = cars_data.copy()


#HOW TO CREATE A FREQUENCY TABLE

#PANDAS.CROSSTAB() is used to simple cross tabulation of one two or more factors

pd.crosstab(index = cars_data_copy)['FuelType'] , columns = 'count' , dropna = True


#TWO WAY TABLE

pd.crosstab(index = cars_data_copy['Automatic'] , 
                columns = cars_data_copy ['FuelType'] , 
                dropna = True)
                

#TWO WAY TABLE - JOINT PROBABILITY
                
pd.crosstab(index = cars_data_copy['Automatic'] , 
                columns = cars_data_copy ['FuelType'] ,
                normalize = True ,
                dropna = True)            


#TWO WAY TABLE - MARGINAL PROBABILITY
                
pd.crosstab(index = cars_data_copy['Automatic'] , 
                columns = cars_data_copy ['FuelType'] ,
                margins = True ,
                normalize = True ,
                dropna = True)  


#TWO WAY TABLE - CONDITIONAL PROBABILITY
                
pd.crosstab(index = cars_data_copy['Automatic'] , 
                columns = cars_data_copy ['FuelType'] ,
                margins = True ,
                dropna = True ,
                normalize = 'index')

#TWO WAY TABLE - CONDITIONAL PROBABILITY 2

pd.crosstab(index = cars_data_copy['Automatic'] , 
                columns = cars_data_copy ['FuelType'] ,
                margins = True ,
                dropna = True ,
                normalize = 'columns')