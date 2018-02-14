""" Wattary's Brain """

# Note: This file Require Numpy , Pandas and Sci-kit learn  Modules

# Importing the modules
import numpy as np
import pandas as pd
import sklearn
from sklearn.neighbors import NearestNeighbors


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

        self.Data = self.dataSet.ix[:, (1, 4, 10)].values

        self.Neighbors = NearestNeighbors(n_neighbors=1).fit(self.Data)

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

        self.newOutput = self.OutPut.strip("[]")

        # cast it again to Integer
        self.Index = int(self.newOutput)

        self.recommendedItem = self.dataSet.iloc[self.Index]
        return self.recommendedItem


# --------------------------------------------------Just for Testing---------------------------------------#
Cars = pd.read_csv('DataSets/mtcars.csv')
x = RECOMMENDER(Cars, [21, 150, 4])
out = x.Model(x.listOfValues)
recomendedItem = x.outPutHandling(out)
print(recomendedItem)
