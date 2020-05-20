#import os
#os.chdir('F:\spyder work')

#cd F:\spyder work

import os

import pandas as pd

os. chdir('F:\spyder work') #Pandas cd F:\spyder work



#HOW TO READ CSV FILE FORMAT IN SPYDER

data_csv = pd.read_csv('CSV_FILE_NAME.csv')

#Remove the extra id column by passing index_col=0

data_csv = pd.read_csv('CSV_FILE_NAME.csv' , index_col=0)

#JUNK values can be converted to missing values by passing them as a list tothe parameter "NA_VALUES"

data_csv = pd.read_csv('CSV_FILE_NAME.csv' , index_col=0 , na_values=["???"])
data_csv = pd.read_csv('CSV_FILE_NAME.csv' , index_col=0 , na_values=["???" , "###"])






#HOW TO READ EXCEL FILE FORMAT IN SPYDER

data_xlsx = pd.read_exel('EXCEL_FILE_NAME.xlsx' , sheet_name = 'SHEET_NAME')


#Remove index column and replace "???" and "###" MISSING VALUES

data_xlsx = pd.read_excel('EXCEL_FILE_NAME.xlsx' , index_col=0 , na_values=["???" , "###"])





#HOW TO READ TEXT FILE FORMAT IN SPYDER

data_text = pd.read_table('TEXT_FILE_NAME.txt')

#Provide a delimiter to the parameters "SEP" or "DELIMITER"

data_text = pd.read_table('TEXT_FILE_NAME.txt' , sep = '\t')
data_text = pd.read_table('TEXT_FILE_NAME.txt' , delimiter = '\t')

#READ_CSV also  used to read TEXT FILE

data_text = pd.read_csv('TEXT_FILE_NAME.txt' , delimiter = " ")