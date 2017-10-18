""" Wattary's Brain """

# Note: This file Require Numpy , Pandas and Sci-kit learn  Modules

#Importing the modules
import numpy as np
import pandas as pd
import sklearn
from sklearn.neighbors import NearestNeighbors

#-----------------------------------------------------------------------------------------------------#



# using pandas library to read our Dataset file.csv
Cars = pd.read_csv('DataSets/mtcars.csv')

def Initlaize():

    # Define the Columns's names of the Dataset
    Cars.columns = ['carNames', 'Mpg', 'Cyl', 'disp', 'horsePower', 'drat', 'Wight', 'qsec', 'vs', 'am', 'Gear', 'carb']


def Display():
    """ This method for Testing purpose only  """

    print(Cars.head())


def SetTestValues (TestValues = []):
    """ This Method will take a Dict insted of list in the Future """
    listOfTValues = TestValues

    return listOfTValues

def Model(valueList = []):

    '''

    in this example  i choose  random values ,
    in the future this indxes will depend on the user's selction
    in this demo the user want us to recommedd a car with :
    1-Nummber of galons per mile   ,  2- the Horse Power
    3- Number of gears of the car

    '''
    Data = Cars.ix[:, (1, 4, 10)].values

    Neighbors = NearestNeighbors(n_neighbors=1).fit(Data)

    print(Neighbors.kneighbors([valueList]))






#--------------------------------------------Just For Testing----------------------------------------------#

Initlaize()
#Display()
Test = SetTestValues([21,150,4])
Model(Test)