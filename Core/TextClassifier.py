from textblob.classifiers import NaiveBayesClassifier

train = [

    ('switch on the light', 'light-on'),
    ('turn on the light', 'light-on'),
    ('switch off the light', 'light-off'),
    ('turn off the light', 'light-off'),

    ('switch on the air conditioning', 'air-conditioning-on'),
    ('turn on the air conditioning', 'air-conditioning-on'),
    ('switch off the air conditioning', 'air-conditioning-off'),
    ('turn off the air conditioning', 'air-conditioning-off'),

    ('switch on the television', 'television-on'),
    ('switch on the tv', 'television-on'),
    ('turn on the television', 'television-on'),
    ('turn on the tv', 'television-on'),
    ('switch off the television', 'television-off'),
    ('switch off the tv', 'television-off'),
    ('turn off the television', 'television-off'),
    ('turn off the tv', 'television-off'),

    ('set the temperature to', 'temperature-update'),
    ('update the temperature to ', 'temperature-update'),

    ('call the elevator', 'elevator-calling'),

    ('what is the weather today in ', 'weather-inquiry')

]

# Testing data suppose to be here [Untill I know its function]

C = NaiveBayesClassifier(train)

def classify(text):
    return C.classify(text)