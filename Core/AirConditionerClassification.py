#importing some library for the model
import pandas as pd
import numpy as np
from sklearn.tree import  DecisionTreeClassifier
from sklearn.cross_validation import train_test_split

Air=np.asarray([(1,16,30,32,1),
                (2,16.30,29,32,1),
                (3,16.25,28,30,1),
                (4,17,29,31,1),
                (5,16.45,25,28,0),
                (6,16.55,25,28,0),
                (7,16.30,24,27,0),
                (8,16,30,32,1),
                (9,16.30,29,32,1),
                (10,16.25,28,30,1),
                (11,17,29,31,1),
                (12,16.45,25,28,0),
                (13,16.55,25,28,0),
                (14,16.30,24,27,0),
                (1, 16, 30, 32, 1),
                (2, 16.30, 29, 32, 1),
                (3, 16.25, 28, 30, 1),
                (4, 17, 29, 31, 1),
                (5, 16.45, 25, 28, 0),
                (6, 16.55, 25, 28, 0),
                (7, 16.30, 24, 27, 0),
                (8, 16, 30, 32, 1),
                (9, 16.30, 29, 32, 1),
                (10, 16.25, 28, 30, 1),
                (11, 17, 29, 31, 1),
                (12, 16.45, 25, 28, 0),
                (13, 16.55, 25, 28, 0),
                (14, 16.30, 24, 27, 0),
                (1,16,30,32,1),
                (2,16.30,29,32,1),
                (3,16.25,28,30,1),
                (4,17,29,31,1),
                (5,16.45,25,28,0),
                (6,16.55,25,28,0),
                (7,16.30,24,27,0),
                (8,16,30,32,1),
                (9,16.30,29,32,1),
                (10,16.25,28,30,1),
                (11,17,29,31,1),
                (12,16.45,25,28,0),
                (13,16.55,25,28,0),
                (14,16.30,24,27,0),
                (1, 16, 30, 32, 1),
                (2, 16.30, 29, 32, 1),
                (3, 16.25, 28, 30, 1),
                (4, 17, 29, 31, 1),
                (5, 16.45, 25, 28, 0),
                (6, 16.55, 25, 28, 0),
                (7, 16.30, 24, 27, 0),
                (8, 16, 30, 32, 1),
                (9, 16.30, 29, 32, 1),
                (10, 16.25, 28, 30, 1),
                (11, 17, 29, 31, 1),
                (12, 16.45, 25, 28, 0),
                (13, 16.55, 25, 28, 0),
                (14, 16.30, 24, 27, 0),
                ],
                 dtype=float)

#convert the array into Datafarme
df=pd.DataFrame(Air)

#adding the Columns name for the DataSet
df.columns=['day','date','interior val','exterior val','user_value']
#df.head(5)

#slicing the DataSet into X and Y
X,Y =df.iloc[:,0:4],df.iloc[:,4]
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=1,stratify=Y)

Clssifier=DecisionTreeClassifier(criterion='entropy',random_state=0)
#fitting the Classfier in DataSet
Clssifier.fit(X,Y)

print(str(Clssifier.predict(np.array([(8,16.35,25,32)],dtype=float))).strip("[]."))
print(Clssifier.score(X,Y)*10)
