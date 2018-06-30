""" Wattary's Brain """

# Note: This file Require Numpy , Pandas and Sci-kit learn  Modules

# Importing the modules
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
import datetime
class Light:
    def __init__(self, data):
        """
        :param dataset: array: that has the data of the light.
        initialize the data when creating the object
        """
        self.dataSet = data
        self.score = 0.0

        # Creating a Classifier
        self.Cls = GaussianNB()

    def FitAndPredict(self, Date, Hour, Minutes, roomNum):
        """
        :param Date: the date of the day the classifier will predict from it.
        :param Hour: The hours in the time
        :param Minutes: The minutes in the time
        :param roomNum: The room number that we will predict on it
        :return: the score(Accuracy) of each classifier.
        """
        ################################# Fitting ######################################
        # Assign the data frame we will fit
        df = self.dataSet
        # Assign The TrainingExamples Columns And Target Columns
        X, Y = df.iloc[:, 0:4], df.iloc[:, 4]
        #print(X)
        #print(Y)
        # slicing the DataSet into Train and Test
        #X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.80, random_state=1, stratify=Y)
        # Fit The Data
        self.Cls.fit(X, Y)
        # Evaluate the accuracy of the model
        self.score = self.Cls.score(X, Y)
        ################################# Prediction ###################################
        """
         making the model Predict on the data by passing to it:
            1- Date of the day
            2- Hours
            3- minutes
            4- Room Number
        """
        testValues = np.array([(736834, Hour, Minutes, roomNum)], dtype=np.int32)
        # Prediction result
        result = str(self.Cls.predict(testValues)).strip("[].")
        result = int(result)
        if(result == 0):
            Result = False
        else:
            Result = True
        # GaussianNB Accuracy , Result
        return Result

######################################### Main #########################################


def test(roomNum, obj):
    Hour = 1
    Minutes = 0
    testRoom = {}
    while Hour <= 24:

        key = "Hour " + str(Hour)
        testRoom[key] = [obj.FitAndPredict(736834, Hour, Minutes, roomNum)]
        Hour += 1
    return testRoom


# Array of Date Time of 30 days to 3 rooms
DateTime = np.asarray([('2018-05-01T01:00'),
                    ('2018-05-02T02:00'),
                    ('2018-05-03T03:56'),
                    ('2018-05-04T04:56'),
                    ('2018-05-05T05:56'),
                    ('2018-05-06T06:00'),
                    ('2018-05-07T07:00'),
                    ('2018-05-08T08:00'),
                    ('2018-05-09T09:59'),
                    ('2018-05-10T10:00'),
                    ('2018-05-11T11:00'),
                    ('2018-05-12T12:00'),
                    ('2018-05-13T13:00'),
                    ('2018-05-14T14:00'),
                    ('2018-05-15T15:00'),
                    ('2018-05-16T16:00'),
                    ('2018-05-17T16:00'),
                    ('2018-05-18T17:00'),
                    ('2018-05-19T18:00'),
                    ('2018-05-20T19:00'),
                    ('2018-05-21T20:00'),
                    ('2018-05-22T21:56'),
                    ('2018-05-23T22:56'),
                    ('2018-05-24T23:56'),
                    ('2018-05-25T00:00'),
                    ('2018-05-26T01:00'),
                    ('2018-05-27T02:00'),
                    ('2018-05-28T03:56'),
                    ('2018-05-29T04:56'),
                    ('2018-05-30T05:56'),
                    ('2018-05-01T01:00'),
                    ('2018-05-02T02:00'),
                    ('2018-05-03T03:56'),
                    ('2018-05-04T04:56'),
                    ('2018-05-05T05:56'),
                    ('2018-05-06T06:00'),
                    ('2018-05-07T07:00'),
                    ('2018-05-08T08:00'),
                    ('2018-05-09T09:59'),
                    ('2018-05-10T10:00'),
                    ('2018-05-11T11:00'),
                    ('2018-05-12T12:00'),
                    ('2018-05-13T13:00'),
                    ('2018-05-14T14:00'),
                    ('2018-05-15T15:00'),
                    ('2018-05-16T16:00'),
                    ('2018-05-17T16:00'),
                    ('2018-05-18T17:00'),
                    ('2018-05-19T18:00'),
                    ('2018-05-20T19:00'),
                    ('2018-05-21T20:00'),
                    ('2018-05-22T21:56'),
                    ('2018-05-23T22:56'),
                    ('2018-05-24T23:56'),
                    ('2018-05-25T00:00'),
                    ('2018-05-26T01:00'),
                    ('2018-05-27T02:00'),
                    ('2018-05-28T03:56'),
                    ('2018-05-29T04:56'),
                    ('2018-05-30T05:56'),
                    ('2018-05-01T01:00'),
                    ('2018-05-02T02:00'),
                    ('2018-05-03T03:56'),
                    ('2018-05-04T04:56'),
                    ('2018-05-05T05:56'),
                    ('2018-05-06T06:00'),
                    ('2018-05-07T07:00'),
                    ('2018-05-08T08:00'),
                    ('2018-05-09T09:59'),
                    ('2018-05-10T10:00'),
                    ('2018-05-11T11:00'),
                    ('2018-05-12T12:00'),
                    ('2018-05-13T13:00'),
                    ('2018-05-14T14:00'),
                    ('2018-05-15T15:00'),
                    ('2018-05-16T16:00'),
                    ('2018-05-17T16:00'),
                    ('2018-05-18T17:00'),
                    ('2018-05-19T18:00'),
                    ('2018-05-20T19:00'),
                    ('2018-05-21T20:00'),
                    ('2018-05-22T21:56'),
                    ('2018-05-23T22:56'),
                    ('2018-05-24T23:56'),
                    ('2018-05-25T00:00'),
                    ('2018-05-26T01:00'),
                    ('2018-05-27T02:00'),
                    ('2018-05-28T03:56'),
                    ('2018-05-29T04:56'),
                    ('2018-05-30T05:56')
                    ], dtype='datetime64')
# Converting the arrat into data frame
DateTimeDF = pd.DataFrame(DateTime)
# Assign the columns of the data frame
DateTimeDF.columns = ['DateTime']
# comverting to timestamp and splitting the date form date time
DateTimeDF['Dates'] = pd.to_datetime(DateTimeDF['DateTime']).dt.date
# The following code will convert the date into numerical value:
DateTimeDF['Dates'] = DateTimeDF['Dates'].map(datetime.datetime.toordinal)
DateTimeDF = DateTimeDF.drop(['DateTime'],axis=1)
#print(DateTimeDF)
#DateTimeDF = DateTimeDF.reshape(DateTimeDF.size, 1)
# Array of training data with values of:
"""{ Hours, Minutes, RoomNumber, UserValue }"""
data = np.asarray([(1,0,1,0),
                   (2,0,1,0),
                   (3,0,1,0),
                   (4,0,1,0),
                   (5,0,1,1),
                   (6,0,1,1),
                   (7,0,1,0),
                   (8,0,1,0),
                   (9,0,1,0),
                   (10,0,1,0),
                   (11,0,1,0),
                   (12,0,1,0),
                   (13,0,1,0),
                   (14,0,1,0),
                   (15,0,1,0),
                   (16,0,1,0),
                   (17,0,1,0),
                   (18,0,1,1),
                   (19,0,1,1),
                   (20,0,1,1),
                   (21,0,1,1),
                   (22,0,1,1),
                   (23,0,1,1),
                   (24,0,1,0),
                   (22,0,1,1),
                   (1,0,1,0),
                   (2,0,1,0),
                   (3,0,1,0),
                   (4,0,1,0),
                   (5,0,1,0),
                   (1,0,2,0),
                   (2,0,2,0),
                   (3,0,2,0),
                   (4,0,2,0),
                   (5,0,2,1),
                   (6,0,2,1),
                   (7,0,2,0),
                   (8,0,2,0),
                   (9,0,2,0),
                   (10,0,2,0),
                   (11,0,2,0),
                   (12,0,2,0),
                   (13,0,2,0),
                   (14,0,2,0),
                   (15,0,2,0),
                   (16,0,2,0),
                   (17,0,2,0),
                   (18,0,2,1),
                   (19,0,2,1),
                   (20,0,2,1),
                   (21,0,2,1),
                   (22,0,2,1),
                   (23,0,2,1),
                   (24,0,2,0),
                   (22,0,2,1),
                   (1,0,2,0),
                   (2,0,2,0),
                   (3,0,2,0),
                   (4,0,2,0),
                   (5,0,2,0),
                   (1,0,3,0),
                   (2,0,3,0),
                   (3,0,3,0),
                   (4,0,3,0),
                   (5,0,3,1),
                   (6,0,3,1),
                   (7,0,3,0),
                   (8,0,3,0),
                   (9,0,3,0),
                   (10,0,3,0),
                   (11,0,3,0),
                   (12,0,3,0),
                   (13,0,3,0),
                   (14,0,3,0),
                   (15,0,3,0),
                   (16,0,3,0),
                   (17,0,3,0),
                   (18,0,3,1),
                   (19,0,3,1),
                   (20,0,3,1),
                   (21,0,3,1),
                   (22,0,3,1),
                   (23,0,3,1),
                   (24,0,3,0),
                   (22,0,3,1),
                   (1,0,3,0),
                   (2,0,3,0),
                   (3,0,3,0),
                   (4,0,3,0),
                   (5,0,3,0)
                   ],
                  dtype=np.int32)

# Convert the Data from array to DataFrame
dataDF = pd.DataFrame(data)
# Assign The Columns Of The Data Set
dataDF.columns = ['Hour', 'Minutes', 'RoomNum', 'User_Value']
#print(dataDF)

#this is combination between the DateTime and the other Values in data2DF
bigData = pd.concat([DateTimeDF, dataDF], axis=1)
#bigData = bigData.drop(['DateTime'], axis=1)
#print(bigData)
obj1 = Light(bigData)
RoomNum = 1
DateTime = datetime.datetime.now()
#obj.FitAndPredict(DateTime.date().toordinal(), DateTime.hour, DateTime.minute, RoomNum)

#################### Testing Cases ##################

# testRoom1 = test(1, obj)
# testRoom2 = test(2, obj)
# testRoom3 = test(3, obj)

# print(testRoom1.items())
# print(testRoom2.items())
# print(testRoom3.items())