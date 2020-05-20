import pandas as pd
import numpy as np

import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix

#data_income = pd.read_csv('income.csv')
data_income = pd.read_excel('income.xlsx')

data = data_income.copy()

data.head()

#TO CHECK VARIABLE DATA TYPE
print(data.info())

#CHECK FOR MISSING VALUES
data.isnull()

#GET SUMMARY OF NUMERICAL VARIABLE
summary_num = data.describe()
print(summary_num)

#GET SUMMARY OF CATEGORICAL VARIABLE
summary_cate = data.describe(include="O")  # capital O stands for OBJECT
print(summary_cate)


#FREQUENCY OF EACH CATEGORY

data['JobType'].value_counts()
data['occupation'].value_counts()


#CHECKING FOR UNIQUE CLASSES

print(np.unique(data['gender']))
print(np.unique(data['marital']))


#GO BACK and READ DATA BY including "NA_VALUES" ?

data = pd.read_excel('income.xlsx' , na_values=[" ?"])

#DATA PRE PROCESSING

data.isnull().sum()

missing = data[data.isnull().any(axis=1)]

data2 = data.dropna(axis=0)

#RELATIONSHIP BETWEEN INDEPENDENT VARIABLE

correlation = data2.corr()

#CROSS TABLE and DATA VISUALIZATION

#EXTRACT the COLUMN NAMES
data2.columns


#GENDER PROPORTION TABLE

gender = pd.crosstab(index = data2["gender"] , 
                     columns = 'count' ,
                     normalize = True)

print(gender)



#GENDER vs SALARY STATUES

gender_salstat = pd.crosstab(index = data2["gender"] ,
                     columns = data2['salstat'] ,
                     margin = True,
                     normalize = 'index')

print(gender_salstat)



#FREQUENCY DISTRIBUTION of SALARY STATUS

salstat = sns.countplot(data2['salstat'])



#HISTOGRAM of AGE

sns.distplot(data2['age'] , bins = 100 , kde = False)



#LOGISTIC REGRESSION

#REINDEXING the salary statues names to 0,1
data2['salstat'] = data2['salstat'].map({' less than or equal to 50,000' :0 , ' greater than 20,000' :1})
print(data2['salstat'])

new_data = pd.get_dummies(data2, drop_first=True)

#STORING THE COLUMN NAMES
columns_list = list(new_data.columns)
print(columns_list)

#SEPARATING THE INPUT NAME FROM DATA
features = list(set(columns_list)-set(['salstat']))
print(features)


#STORING OUTPUT VALUES in Y

y = new_data['salstat'].values
print(y)


#STORING THE VALUES FROM INPUT FEATURES
x =  new_data[features].values
print(x)

#SPLITTING THE DATA INTO TRAIN AND TEST
train_x , test_x , train_y , test_y = train_test_split(x , y , test_size=0.3 ,)

#MAKE ON INSTANCE OF THE MODEL
logistic = LogisticRegression()

#FITTING TE VALUES FOR X AND Y
logistic.fit(train_x,train_y)
logistic.coef_
logistic.intercept_

#PREDICTION from TEST DATA
prediction = logistic.predict(test_x)
print(prediction)

#CONFUSION MATRIX
confusion_matrix = confusion_matrix(test_y, prediction)
print(confusion_matrix)

#CALCULATE ACCURACY
accuracy_score = accuracy_score(test_y, prediction)
print(accuracy_score)

#PRINTING MISCLASSIFIED VALUES FROM PREDICTION
print('Misclassified samples: %d' % (test_y != prediction).sum())


#REMOVING INSIGNIFICANT VARIABLES

#REINDEXING the salary statues names to 0,1
data2['salstat'] = data2['salstat'].map({' less than or equal to 50,000' :0 , ' greater than 20,000' :1})
print(data2['salstat'])

cols = ['gender' , 'JobType']
new_data = data2.drop(cols,axis=1)

new_data = pd.get_dummies(new_data , drop_first = True)

#STORING THE COLUMN NAMES
columns_list = list(new_data.columns)
print(columns_list)


#SEPARATING THE INPUT NAME FROM DATA
features = list(set(columns_list)-set(['salstat']))
print(features)


#STORING OUTPUT VALUES in Y

y = new_data['salstat'].values
print(y)


#STORING THE VALUES FROM INPUT FEATURES
x =  new_data[features].values
print(x)

#SPLITTING THE DATA INTO TRAIN AND TEST
train_x , test_x , train_y , test_y = train_test_split(x , y , test_size=0.3 , random_state=1)


#MAKE ON INSTANCE OF THE MODEL
logistic = LogisticRegression()

#FITTING TE VALUES FOR X AND Y
logistic.fit(train_x,train_y)

#PREDICTION from TEST DATA
prediction = logistic.predict(test_x)
print(prediction)

#CALCULATE ACCURACY
accuracy_score = accuracy_score(test_y, prediction)
print(accuracy_score)

#PRINTING MISCLASSIFIED VALUES FROM PREDICTION
print('Misclassified samples: %d' % (test_y != prediction).sum())