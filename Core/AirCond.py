""" Wattary's Brain """

# Note: This file Require Numpy , Pandas and Sci-kit learn  Modules

# Importing the modules
import numpy as np
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer
from sklearn.svm import SVC


class AirCond:
    Score = 0.0
    TestSetSize = 0.0
    TrainSetSize = 0.0
    Predaction = 0


    def __init__(self,DataSet):
        self.DataSet=DataSet



    def Model_fitting(self,Val):
        df=self.DataSet
        X=df.iloc[:,0:4].values
        Y=df.iloc[:,4:5].values

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
        self.Predaction=str(Clssifier.predict(np.array([(4,Val,25,30)],dtype=float))).strip("[].")

    def display(self):
           print("Score is :"+str(self.Score*100))

          # print(self.DataSet.columns)
           print("Dataset Test size :"+str(self.TestSetSize))

           print("DataSet Train size:"+str( self.TrainSetSize))

           if self.Predaction =='0':
               print("Air conditioner is OFF")
           elif self.Predaction =='1':
                print("Air conditioner is ON")

# ------------------------- Main ----------------------------#


data = np.asarray([(1, 12.00,  25,30,1),
                   (2, 11.00,  26,31,1),
                   (3, 12.00, 25,30,1),
                   (4, 11.30,  27,32,1),
                   (5, 12,  28,33,0),
                   (6, 4,  24,29,0),
                   (7, 16, 23,28,1),
                   (8, 17, 24,29,1),
                   (9, 18, 28,33,1),
                   (10, 2, 29,34,0),
                   (11, 3, 30,35,0),
                   (12,15, 28,33,1),
                   (13,13, 26,31,1),
                   (14,17, 24,29,1),
                   (15,18, 26,31,1),
                   (16,19, 25,30,0),
                   (17,20, 27,33,0),
                   (18,21, 26,31,0)
                   ],
                  dtype=np.float32)
Data2df=pd.DataFrame(data)
Data2df.columns =['day', 'time', 'Interior_Value','Exterior_Value','user_value']


# initilzing the model
obj=AirCond(Data2df)
# making the model fiting the data
#obj.Model_fitting()

# displaying the description of the prediction
#obj.display()

# dectionry for saving the values
grades = {}
Time=1
while Time <= 24:

    id =Time
    grade = 2
    obj.Model_fitting(Time)
    grades[id] = [obj.Predaction,obj.Score]
    Time+=1


print(grades.items())