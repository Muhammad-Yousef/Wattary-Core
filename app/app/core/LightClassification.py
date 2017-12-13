import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# Creating Data for The Light Values
Light = np.asarray([(1, 16, 1, 1),
                    (2, 16.30, 1, 1),
                    (3, 16.25, 1, 1),
                    (4, 17, 1, 1),
                    (5, 16.45, 1, 0),
                    (6, 16.55, 1, 0),
                    (7, 16.30, 1, 0)],
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

# Fit The Data
Cls.fit(X, Y)

# Predict with manual values
print(str(Cls.predict(np.array([(3, 16.30, 1)], dtype=np.float32))).strip("[]."))

# Evaluate the accuracy of the model
print(int(Cls.score(X, Y) * 10),'%')