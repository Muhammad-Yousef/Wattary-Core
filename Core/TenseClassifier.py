from textblob.classifiers import NaiveBayesClassifier

train = [


    ('did', 'past-simple'),
    ('have', 'present-perfect'),
    ('did you', 'past-simple'),
    ('have you', 'present-perfect')

]

C = NaiveBayesClassifier(train)

def classify(text):
    return C.classify(text)