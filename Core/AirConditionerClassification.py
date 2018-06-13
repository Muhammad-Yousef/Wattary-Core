#importing some library for the model

import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer
from sklearn.svm import SVC

class AirClassification:

    Score=0.0
    TestSetSize=0.0
    TrainSetSize=0.0
    Predaction=0

    def __init__(self,DataSet):
        self.DataSet=DataSet


    def DateConverter(self):
         DataSet=self.DataSet

         DataSet.CET = pd.to_datetime(DataSet.CET, format='%Y-%m-%d')
         DataSet['year'] = DataSet.CET.dt.year
         DataSet['dayofyear'] = DataSet.CET.dt.dayofyear
         self.DataSet=DataSet

         return self.DataSet


    # convert the Data Set to Datafarme
    def DataToDF(self,DataSet):
        df=self.DataSet
        df = pd.DataFrame(DataSet)
        self.DataSet=df.iloc[:,1:5]
        return self.DataSet

    #Clianing the Data set
    def DataPreprocess(self,Dataset):
        df=self.DataSet
        imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
        imputer =imputer.fit(df.iloc[:,0:2])
        df.iloc[:,0:2]=imputer.transform(df.iloc[:,0:2])
        self.DataSet=df
        return self.DataSet

     #creat a column that contine user values
    def addValues(self,DataSet):
        df=self.DataSet
          #df[(df['MaxTemperatureC'] >21) & (df['MinTemperatureC'] > 8) &(df['UserValue']==0)]
          # #df['UserValue']=np.where(df[(df['MaxTemperatureC'] >21) & (df['MinTemperatureC'] > 8)],'true','false')
        df['UserVal']=np.where((df['MaxTemperatureC']>21),'yes','no')
        #print(len(df[(df['UserVal']=='yes')]))
        df['UserVal']=pd.factorize(df['UserVal'])[0]
        self.DataSet=df
        print(len(DataSet[(DataSet['UserVal']==1)]))

        return self.DataSet



    def Model_fitting(self):
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

        Clssifier.fit(X_test,Y_test)
        self.Score=Clssifier.score(X_train,Y_train)

# frist is Max Temp And secound is MinTem thrid is Year fourth is Day
        self.Predaction=str(Clssifier.predict(np.array([(22,3,2018,5)],dtype=float))).strip("[].")


    def display(self):
           print("Score is :"+str(self.Score*100))

          # print(self.DataSet.columns)
           print("Data set size :"+str(self.TestSetSize))

           print(self.TrainSetSize)

           if self.Predaction =='0':
               print("Air conditioner is OFF")
           elif self.Predaction =='1':
                print("Air conditioner is ON")



DataSetCSV=pd.read_csv('DataSets/weather_madrid.csv',usecols=['CET','MaxTemperatureC','MinTemperatureC'],parse_dates=['CET'])
cl=AirClassification(DataSetCSV)
csv=cl.__init__(DataSetCSV)
DateConverter= cl.DateConverter()
df=cl.DataToDF(DateConverter)
prepro=cl.DataPreprocess(df)
userVal=cl.addValues(prepro)
cl.Model_fitting()
cl.display()

#print(Clssifier.score(X,Y))
