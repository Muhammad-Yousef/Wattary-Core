""" Wattary's Brain """

# Note: This file Require Numpy , Pandas and Sci-kit learn  Modules

# Importing the modules
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split


class Light:
    def __init__(self, data):
        """
        :param dataset: array: that has the data of the light.
        :param cols: dictionary: Contains the name of the columns of the data set.

        initialize the data when creating the object
        """
        self.dataSet = data

        # Creating a Classifier With SuperVectorClustering Algorithm
        self.Cls = SVC()
        self.Cls2 = GaussianNB()

    def fit(self, train, target):
        """
        :param train: the data that the classifier will learn from it.
        :param target: the output of the values in the train data.
        :return: the score(Accuracy) of each classifier.
        """
        # Fit The Data
        self.Cls.fit(train, target)
        self.Cls2.fit(train, target)

        # Evaluate the accuracy of the model

        # SVC Accuracy                              # GaussianNB Accuracy
        return self.Cls.score(train, target) * 100, self.Cls.score(train, target) * 100




    def predict(self, dayNum, time, roomNum):
        """
        I will print the output of this function for now until we connect to the Hardware brunch
        """
        testvalues = np.array([(dayNum, time, roomNum)], dtype=np.float32)
        # SVC Prediction                     # GaussianNB Prediction
        return self.Cls.predict(testvalues), self.Cls2.predict(testvalues)


# --------------------------------------------------Just for Testing---------------------------------------#

data = np.asarray([(1, 16, 1, 1),
                   (2, 16.30, 1, 1),
                   (3, 16.25, 1, 1),
                   (4, 17, 1, 1),
                   (5, 16.45, 1, 0),
                   (6, 16.55, 1, 0),
                   (7, 16.30, 1, 0),
                   # from here the addition of samples
                   (1, 16, 1, 1),
                   (2, 16.30, 1, 1),
                   (3, 16.25, 1, 1),
                   (4, 17.30, 1, 1),
                   (5, 15.30, 1, 1),
                   (6, 16.55, 1, 0),
                   (7, 16.30, 1, 0),
                   (1, 16, 1, 1),
                   (2, 16.30, 1, 1),
                   (3, 16.25, 1, 1),
                   (4, 17, 1, 1),
                   (5, 16.45, 1, 0),
                   (6, 16.55, 1, 0),
                   (7, 16.30, 1, 0),
                   (1, 16, 1, 1),
                   (2, 16.30, 1, 1),
                   (3, 16.25, 1, 1),
                   (4, 17, 1, 1),
                   (5, 16.45, 1, 0),
                   (6, 16.55, 1, 0),
                   (7, 16.30, 1, 0),
                   (1, 15, 1, 0),
                   (2, 16.30, 1, 1),
                   (3, 16.30, 1, 1),
                   (4, 17, 1, 1),
                   (5, 16.45, 1, 0),
                   (6, 16, 1, 0),
                   (7, 16.30, 1, 0),
                   (1, 15.30, 1, 0),
                   (2, 17, 1, 1),
                   (3, 15.30, 1, 0),
                   (4, 17, 1, 1),
                   (5, 15.30, 1, 1),
                   (6, 16.55, 1, 0),
                   (7, 17, 1, 1),
                   (1, 16, 1, 1),
                   (2, 16, 1, 0),
                   (3, 15.30, 1, 0),
                   (4, 16.30, 1, 0),
                   (5, 17, 1, 0),
                   (6, 17, 1, 1),
                   (7, 17, 1, 1),
                   (1, 16.25, 1, 1),
                   (2, 17, 1, 1),
                   (3, 16.30, 1, 1),
                   (4, 16.30, 1, 0),
                   (5, 17, 1, 0),
                   (6, 17, 1, 1),
                   (7, 16, 1, 0),
                   (1, 16, 1, 1),
                   (2, 16.30, 1, 1),
                   (3, 17.30, 1, 0),
                   (4, 18, 1, 1),
                   (5, 16.45, 1, 0),
                   (6, 16.55, 1, 0),
                   (7, 16, 1, 0),
                   (1, 15, 1, 1),
                   (2, 16.35, 1, 1),
                   (3, 14.5, 1, 0),
                   (4, 16, 1, 1),
                   (6, 16.20, 1, 0),
                   (7, 16.40, 1, 0),
                   (1, 16, 1, 1),
                   (2, 16.30, 1, 1),
                   (3, 14.30, 1, 0),
                   (4, 17, 1, 1),
                   (5, 16.45, 1, 0),
                   (6, 16.55, 1, 0),
                   (7, 16.30, 1, 0),
                   (1, 16, 1, 1),
                   (2, 16.30, 1, 1),
                   (3, 16.25, 1, 1),
                   (4, 17, 1, 1),
                   (5, 16.45, 1, 0),
                   (6, 16.55, 1, 0),
                   (7, 16.30, 1, 0),
                   (1, 16, 1, 1),
                   (2, 16.30, 1, 1),
                   (3, 16.25, 1, 1),
                   (4, 17, 1, 1),
                   (5, 16.45, 1, 0),
                   (6, 16.55, 1, 0),
                   (7, 16.30, 1, 0),
                   (1, 16.15, 1, 1),
                   (2, 16.20, 1, 1),
                   (3, 16.25, 1, 1),
                   (4, 17.10, 1, 1),
                   (5, 16.45, 1, 0),
                   (6, 16.55, 1, 0),
                   (7, 16.25, 1, 0),
                   (1, 16.5, 1, 1),
                   (2, 16.15, 1, 1),
                   (3, 16.30, 1, 1),
                   (4, 17.15, 1, 1),
                   (5, 16.55, 1, 0),
                   (6, 17.5, 1, 0),
                   (7, 17.30, 1, 0)
                   ],
                  dtype=np.float32)
# Convert the Data from array to DataFrame
df = pd.DataFrame(data)
# Assign The Columns Of The Data Set
df.columns = ['day', 'time', 'room', 'user_value']
# Assign The TrainingExamples Columns And Target Columns
x, y = df.iloc[:, 0:3], df.iloc[:, 3]

obj1 = Light(df)
obj1.fit(x, y)

print(obj1.predict(3, 14, 1))
print(obj1.predict(4, 16.30, 1))
print(obj1.predict(5, 15.30, 1))
