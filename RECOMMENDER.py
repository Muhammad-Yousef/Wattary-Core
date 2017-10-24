""" Wattary's Brain """

# Note: This file Require Numpy , Pandas and Sci-kit learn  Modules

# Importing the modules
import numpy as np
import pandas as pd
import sklearn
from sklearn.neighbors import NearestNeighbors


# ----------------------------------------------------- OOP Version -----------------------------------#
class RECOMMENDER:
    def __init__(self, dataset, testValues=[]):
        self.dataSet = dataset  # To initialize the path when creating the object
        self.listOfValues = testValues  # To initialize the test values when crating the object without using a function

    def Initialize(self):
        # Define the Columns's names of the Data set
        self.dataSet.coulmns = ['carNames', 'Mpg', 'Cyl', 'disp', 'horsePower', 'drat', 'Wight', 'qsec', 'vs', 'am',
                                'Gear', 'carb']

    def Display(self):
        # This method for Testing purpose only
        print(self.dataSet.head())

    """
    def SetTestValues(self, testValues=[]):
        # This Method will take a Dict instead of list in the Future    # Lines to Remove
        self.listOfValues = testValues

        return self.listOfValues
    """

    def Model(self, valueList=[]):
        """
            in this example  i choose  random values ,
            in the future this indexes will depend on the user's selection
            in this demo the user want us to recommend a car with :
            1- Number of galons per mile
            2- the Horse Power
            3- Number of gears of the car
        """
        '''
        :return array of 2 arrays 
        1st: the length between the beginning of the csv file  to the chosen value
        2nd: the chosen value that well be recommended to the user
        '''
        # checking data in all rows for the columns 1,4 and 10
        self.Data = self.dataSet.ix[:, (1, 4, 10)].values

        # Fitting the Nearest Neighbors function to the data in our data set
        self.Neighbors = NearestNeighbors(n_neighbors=1).fit(self.Data)

        # Getting the nearest value to the desired values in the data set
        self.Output = self.Neighbors.kneighbors([valueList])

        return self.Output

    def outPutHandling(self, output):
        #:return: Full Details for the Recommended Item

        # cast the list given to String
        self.OutPut = str(output[1])

        # remove the Brackets from the string
        self.newOutput = self.OutPut.strip("[]")

        # cast it again to Integer
        self.Index = int(self.newOutput)

        # Return the Recommended Item
        self.recommendedItem = self.dataSet.iloc[self.Index]
        return self.recommendedItem


# --------------------------------------------------Just for Testing---------------------------------------#
pathOfDataSet = pd.read_csv('DataSets/mtcars.csv')
x = RECOMMENDER(pathOfDataSet, [21, 150, 4])
x.Initialize()
# listV = x.SetTestValues([21, 150, 4]) # line to remove
out = x.Model(x.listOfValues)
recomendedItem = x.outPutHandling(out)
print(recomendedItem)
