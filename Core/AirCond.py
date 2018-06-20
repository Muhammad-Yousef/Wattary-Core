""" Wattary's Brain """

# Note: This file Require Numpy , Pandas and Sci-kit learn  Modules

# Importing the modules
import numpy as np
import pandas as pd
#from pandas.tests.scalar import timestamp
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer
from sklearn.svm import SVC
import datetime

class AirCond:
    Score = 0.0
    TestSetSize = 0
    TrainSetSize = 0
    Predaction = 0



    def __init__(self,DataSet):
        self.DataSet=DataSet



    def Model_fitting(self,DateVal,HourVal,MinutesVal,Int_Value,Ext_Value ):
        df=self.DataSet
        X=df.iloc[:,1:6].values
        Y=df.iloc[:,6:7].values

        #slicing the DataSet into Train and Test
        X_train,X_test,Y_train,Y_test=train_test_split( X,Y,test_size=0.20,random_state=1,stratify=Y)

        self.TestSetSize=len(X_test)+len(Y_test)
        self.TrainSetSize=len(X_train)+len(Y_train)
        Clssifier=DecisionTreeClassifier(criterion='entropy',random_state=0)
        #Clssifier=SVC()
        #fitting the Classfier in DataSet

        Clssifier.fit(X_train,Y_train)
        self.Score=Clssifier.score(X_test,Y_test)

        # frist is Max Temp And secound is MinTem thrid is Year fourth is Day
        self.Predaction=str(Clssifier.predict(np.array([(DateVal,HourVal,MinutesVal,Int_Value,Ext_Value)],dtype=float))).strip("[].")

    def display(self):
           print("Score is :"+str(self.Score*100))

          # print(self.DataSet.columns)
           print("Dataset Test size :"+str(self.TestSetSize))

           print("DataSet Train size:"+str( self.TrainSetSize))

           if self.Predaction =='0':
               return True
           elif self.Predaction =='1':
               return False

# ------------------------- Main ----------------------------#
DateTime=np.asarray([
                    ('2018-05-01T12:00'),
                    ('2018-05-02T13:00'),
                    ('2018-05-03T01:56'),
                    ('2018-05-04T12:56'),
                    ('2018-05-05T17:56'),
                    ('2018-05-06T19:00'),
                    ('2018-05-07T16:00'),
                    ('2018-05-08T15:00'),
                    ('2018-05-09T23:59'),
                    ('2018-05-10T23:00'),
                    ('2018-05-11T08:00'),
                    ('2018-05-12T09:00'),
                    ('2018-05-13T10:00'),
                    ('2018-05-14T11:00'),
                    ('2018-05-15T19:00'),
                    ('2018-05-16T20:00'),
                    ('2018-05-07T07:00'),
                    ('2018-05-07T03:00')
                    ], dtype='datetime64')
DateTime2DF=pd.DataFrame(DateTime)
DateTime2DF.columns=['DateTime']

# comverting to timestamp and splitting the date form date time
DateTime2DF['Dates'] =pd.to_datetime(DateTime2DF['DateTime']).dt.date

# model doesn't work on date data. Therefore we need to convert it into numerical value.
# The following code will convert the date into numerical value:
DateTime2DF['Dates']=DateTime2DF['Dates'].map(datetime.datetime.toordinal)

# comverting to timestamp and splitting the date form date time

#DateTime2DF['Time'] = (DateTime2DF['DateTime'])
#DateTime2DF['Time'] =pd.to_datetime(DateTime2DF['Time'],errors='ignore')


#print(DateTime2DF['Dates'])

data = np.asarray([(12,00,25,30,1),
                   (13,00,26,31,1),
                   (14,00,25,30,1),
                   (15,00,27,32,1),
                   (19,00,28,33,0),
                   (20,00,24,29,0),
                   (16,00,23,28,1),
                   (17,00,24,29,1),
                   (18,00,28,33,1),
                   (1,00,29,34,0),
                   (2,00,30,35,0),
                   (10,00,28,33,1),
                   (11,00,26,31,1),
                   (8,00,24,29,1),
                   (7,00,26,31,1),
                   (4,00,25,30,0),
                   (5,00,27,33,0),
                   (6,00,26,31,0)

                   ],
                  dtype=np.int32)

data2DF=pd.DataFrame(data)
data2DF.columns =['Hour','minutes','Interior_Value','Exterior_Value','user_value']

#this is combination between the DateTime and the other Values in data2DF
bigdata = pd.concat([DateTime2DF, data2DF], axis=1)

# initilzing the model
obj = AirCond(bigdata)

# Time = datetime.datetime(2018, 5, 7,12,00)
DateTime=datetime.datetime.now()

Interior_Value=30
Exterior_Value=35
"""
 making the model fiting the data by passing to it:
    1- Date of the day
    2- Hours
    3- minutes
    4- Interior_Value
    5- Exterior_Value
"""
obj.Model_fitting(DateTime.date().toordinal(),DateTime.hour,DateTime.minute,Interior_Value,Exterior_Value)
   # displaying the description of the prediction
obj.display()

# dectionry for saving the values


H = DateTime.hour
grades = {}
Time=1
while Time <= 24:
 if(H>24):
    H=1
    id = Time
    grade = 2
    obj.Model_fitting(DateTime.date().toordinal(), H, DateTime.minute, Interior_Value, Exterior_Value)
    grades[id] = [obj.Predaction, obj.Score]
    H = H + 1
    Time += 1
 else :
    id =Time
    grade = 2
    obj.Model_fitting(DateTime.date().toordinal(), H, DateTime.minute, Interior_Value, Exterior_Value)
    grades[id] = [obj.Predaction,obj.Score]
    H=H+1
    Time+=1

#print(grades.items())
