from textblob.classifiers import NaiveBayesClassifier

train = [

    ('switch on the light', 'light-on'),
    ('turn on the light', 'light-on'),

    ('switch off the light', 'light-off'),
    ('turn off the light', 'light-off'),

    ('did you switched on the light', 'light-on-inquiry'),
    ('have you switched on the light', 'light-on-inquiry'),

    ('did you switched off the light', 'light-off-inquiry'),
    ('have you switched off the light', 'light-off-inquiry'),

    ('switch on the air conditioning', 'air-conditioning-on'),
    ('turn on the air conditioning', 'air-conditioning-on'),

    ('did you switched on the air conditioning', 'air-conditioning-on-inquiry'),
    ('have you switched on the air conditioning', 'air-conditioning-on-inquiry'),

    ('switch off the air conditioning', 'air-conditioning-off'),
    ('turn off the air conditioning', 'air-conditioning-off'),

    ('did you switched off the air conditioning', 'air-conditioning-off-inquiry'),
    ('have you switched off the air conditioning', 'air-conditioning-off-inquiry'),

    ('switch on the television', 'television-on'),
    ('switch on the tv', 'television-on'),
    ('turn on the television', 'television-on'),
    ('turn on the tv', 'television-on'),

    ('did you switched on the television', 'television-on-inquiry'),
    ('did you switched on the tv', 'television-on-inquiry'),
    ('have you switched on the television', 'television-on-inquiry'),
    ('have you switched on the tv', 'television-on-inquiry'),

    ('switch off the television', 'television-off'),
    ('switch off the tv', 'television-off'),
    ('turn off the television', 'television-off'),
    ('turn off the tv', 'television-off'),

    ('did you switched off the television', 'television-off-inquiry'),
    ('did you switched off the tv', 'television-off-inquiry'),
    ('have you switched off the television', 'television-off-inquiry'),
    ('have you switched off the tv', 'television-off-inquiry'),

    ('set the temperature to', 'temperature-update'),
    ('update the temperature to ', 'temperature-update'),

    ('call the elevator', 'elevator-calling'),
    ('did you call the elevator', 'elevator-calling-inquiry'),
    ('have you called the elevator', 'elevator-calling-inquiry'),

    ('what is the weather today in ', 'weather-inquiry')

]

C = NaiveBayesClassifier(train)

def classify(text):
    return C.classify(text)

