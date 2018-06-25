""" Wattary's Brain """

# Note: This file Require Numpy , Pandas and Sci-kit learn  Modules

# Importing the modules
import numpy as np
import pandas as pd
import sklearn
from sklearn.neighbors import NearestNeighbors
import random
'''

csv=pd.read_csv('DataSets/movies_metadata.csv',usecols=['genres'])
df=pd.DataFrame(csv)
print(df['genres'])

movieCSV= pd.read_csv('DataSets/movies_metadata.csv',usecols=['adult','id','genres','original_language','title','overview','release_date','runtime','vote_average'])
print(movieCSV.head(2))

'''

# ----------------------------------------------------- Recommender Class -----------------------------------#
class RECOMMENDER:
    def __init__(self, dataset, testValues=[]):
        """

        :param dataset: string: that has the path to the data set
        :param testValues:  list:  the values that we will recommend an item based on it

        initialize the path when creating the object
        and initialize the test values when crating the object without using a function
        """

        self.dataSet = dataset

        self.listOfValues = testValues
        self.items = []

    def Display(self):
        """ This method for Testing purpose only """

        print(self.dataSet.head())


    def SetValuesIndexes(self, testValues=[]):
        """ ToDo """

    def Model(self, valueList=[]):
        """

        :param valueList: list:  the values that we will recommend an item based on it
        :return: list:


        checking data in all rows for the columns 1,4 and 10,
        Fitting the Nearest Neighbors function to the data in our data set
        and Getting the nearest value to the desired values in the data set
        """

        self.Data = self.dataSet.ix[:, (9,25)].values

        self.Neighbors = NearestNeighbors(n_neighbors=25).fit(self.Data)

        self.Output = self.Neighbors.kneighbors([valueList])

        return self.Output




    def outPutHandling(self, output):
        """

        :param output: list:  that returned from Model()
        :return: recommenedItem: vector row or list: that has the recommended details

        cast the list given to String,
        remove the Brackets from the string
        and return the Recommended Item
        """
        self.OutPut = str(output[1])
        #print( self.OutPut)
        #self.newOutput = self.OutPut.strip("[]")

        self.OutPut = self.OutPut.replace("[[ ", "")
        self.OutPut = self.OutPut.replace("]]", "")
        self.OutPut = self.OutPut.replace(" ", ",")
        self.OutPut = self.OutPut.replace("[[", "")
        self.OutPut = self.OutPut.replace(",,", ",")
        self.OutPut = self.OutPut.replace("\n,,", ",")
        self.OutPut = self.OutPut.replace("\n", "")
        self.items.append(self.OutPut)
        x = self.items[0]
        x = x.replace(",", " ")
        y = x.split()
        #print(len(y))
        r = random.sample(range(0,24), 1)
        r = str(r).strip('[]')
        
        # cast it again to Integer
        self.Index = int(y[int(r)])
        #print(y[int(r)])
        self.recommendedItem = self.dataSet.iloc[self.Index,11]
        return self.recommendedItem


# --------------------------------------------------Just for Testing---------------------------------------#
# Cars = pd.read_csv('DataSets/mtcars.csv')
# x = RECOMMENDER(Cars, [21, 150, 4])
# out = x.Model(x.listOfValues)
# recomendedItem = x.outPutHandling(out)
# print(recomendedItem)z
#  Movies = pd.read_csv('./DataSets/convertcsv.csv')
#  A = RECOMMENDER(Movies, [8, 5])
#  opt = A.Model(A.listOfValues)
#  recomendedItem = A.outPutHandling(opt)
#  print(recomendedItem)
#  #print(opt)