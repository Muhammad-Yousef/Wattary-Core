""" Wattary's Brain """

# Note: This file Require Numpy , Pandas and Sci-kit learn  Modules

# Importing the modules
import numpy as np
import pandas as pd
import sklearn
from sklearn.neighbors import NearestNeighbors
<<<<<<< HEAD
from sklearn import preprocessing
=======
import random
'''
>>>>>>> b3e23a69d357152ba3ecbc248e5ba2eaea92325b

# Reading the CSV File and Convert it to Data Frame
movieCSV = pd.read_csv('DataSets/movie_metadata 1.1.csv', usecols=['num_critic_for_reviews', 'duration', 'gross',
                                                                'num_voted_users', 'cast_total_facebook_likes',
                                                                'num_user_for_reviews', 'title_year', 'imdb_score',
                                                                'movie_facebook_likes', 'genres', 'movie_title',
                                                                'director_name', 'actor_1_name', 'movie_imdb_link'])
movieDF = pd.DataFrame(movieCSV)

# ----------------------------------------------------- Recommender Class -----------------------------------#


class Recommender:
    def __init__(self, testValues):
        """

        :param dataset: string: that has the path to the data set
        :param testValues:  list:  the values that we will recommend an item based on it

        initialize the path when creating the object
        and initialize the test values when crating the object without using a function
        """

        self.movieDF = movieDF

<<<<<<< HEAD
        self.testValues = testValues
=======
        self.listOfValues = testValues
        self.items = []
>>>>>>> b3e23a69d357152ba3ecbc248e5ba2eaea92325b

    def encode(self):
        """ This method for Testing purpose only """
        le = preprocessing.LabelEncoder()
        le.fit(self.movieDF['genres'])
        self.movieDF['genres'] = le.transform(self.movieDF['genres'])
        print(self.movieDF.head())

    def FitAndPredict(self, valueList=[]):
        """
        :param valueList: list:  the values that we will recommend an item based on it
        :return: list:


        checking data in all rows for the columns 1,4 and 10,
        Fitting the Nearest Neighbors function to the data in our data set
        and Getting the nearest value to the desired values in the data set
        """

        tData = self.movieDF.iloc[:, 0:10]

<<<<<<< HEAD
        self.Neighbors = NearestNeighbors(n_neighbors=1).fit(tData)
=======
        self.Neighbors = NearestNeighbors(n_neighbors=25).fit(self.Data)
>>>>>>> b3e23a69d357152ba3ecbc248e5ba2eaea92325b

        self.Output = self.Neighbors.kneighbors([valueList])

        return self.Output

<<<<<<< HEAD
    # def outPutHandling(self, output):
    #     """
    #
    #     :param output: list:  that returned from Model()
    #     :return: recommenedItem: vector row or list: that has the recommended details
    #
    #     cast the list given to String,
    #     remove the Brackets from the string
    #     and return the Recommended Item
    #     """
    #     self.OutPut = str(output[1])
    #
    #     self.newOutput = self.OutPut.strip("[]")
    #
    #     # cast it again to Integer
    #     self.Index = int(self.newOutput)
    #
    #     self.recommendedItem = self.dataSet.iloc[self.Index, 11]
    #     return self.recommendedItem
=======



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

>>>>>>> b3e23a69d357152ba3ecbc248e5ba2eaea92325b

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