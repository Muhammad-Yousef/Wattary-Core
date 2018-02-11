import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

# Creating Data for The Light Values
Light = np.asarray([(1, 16, 1, 1),
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
df = pd.DataFrame(Light)

# Assign The Columns Of The Data Set
df.columns = ['day', 'time', 'room', 'user_value']

# Assign The TrainingExamples Columns And Target Columns
X, Y = df.iloc[:, 0:3], df.iloc[:, 3]

# Assign the Train Data and Test Data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=1, stratify=Y)

# Creating a Classifier With SuperVectorClustering Algorithm
Cls = SVC()
Cls2 = GaussianNB()

# Fit The Data
Cls.fit(X, Y)
Cls2.fit(X, Y)


# Predict with fixed values

# SVC Prediction
print("SVC : " + str(Cls.predict(np.array([(3, 14, 1)], dtype=np.float32))).strip("[]."))
print("SVC : " + str(Cls.predict(np.array([(4, 16.30, 1)], dtype=np.float32))).strip("[]."))
print("SVC : " + str(Cls.predict(np.array([(5, 15.30, 1)], dtype=np.float32))).strip("[]."))

# GaussianNB Prediction
print("GaussianNB : " + str(Cls2.predict(np.array([(3, 14, 1)], dtype=np.float32))).strip("[]."))
print("GaussianNB : " + str(Cls2.predict(np.array([(4, 16.30, 1)], dtype=np.float32))).strip("[]."))
print("GaussianNB : " + str(Cls2.predict(np.array([(5, 15.30, 1)], dtype=np.float32))).strip("[]."))

# Evaluate the accuracy of the model

# SVC Accuracy
print("SVC : ", (Cls.score(X, Y) * 100), '%')

# GaussianNB Accuracy
print("GaussianNB : ",  (Cls.score(X, Y) * 100), '%')