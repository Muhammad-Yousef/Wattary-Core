from textblob.classifiers import NaiveBayesClassifier

train = [

# -------------------- Greeting ------------------------- #

    ('hello', 'greeting'),
    ('howdy', 'greeting'),
    ('hey', 'greeting'),
    ('hi', 'greeting'),

    ('how are you', 'status-inquiry'),
    ('how is it going', 'status-inquiry'),
    ('what\'s up', 'status-inquiry'),
    ('how is it going with you', 'status-inquiry'),

    ('what is your name', 'name-inquiry'),
    ('tell me your name', 'name-inquiry'),

    ('how old are you', 'age-inquiry'),
    ('what is your age', 'age-inquiry'),


# -------------------- Light ------------------------- #

    ('switch on the light', 'light-on'),
    ('turn on the light', 'light-on'),

    ('switch off the light', 'light-off'),
    ('turn off the light', 'light-off'),

    ('did you switch on the light', 'light-on-inquiry'),
    ('have you switched on the light', 'light-on-inquiry'),

    ('did you switch off the light', 'light-off-inquiry'),
    ('have you switched off the light', 'light-off-inquiry'),

# -------------------- Temperature ------------------------- #

    ('set the temperature to', 'temperature-update'),
    ('update the temperature to ', 'temperature-update'),

# -------------------- air conditioning ------------------------- #

    ('switch on the air conditioning', 'air-conditioning-on'),
    ('turn on the air conditioning', 'air-conditioning-on'),

    ('did you switch on the air conditioning', 'air-conditioning-on-inquiry'),
    ('have you switched on the air conditioning', 'air-conditioning-on-inquiry'),

    ('switch off the air conditioning', 'air-conditioning-off'),
    ('turn off the air conditioning', 'air-conditioning-off'),

    ('did you switch off the air conditioning', 'air-conditioning-off-inquiry'),
    ('have you switched off the air conditioning', 'air-conditioning-off-inquiry'),

# -------------------- TV ------------------------- #

    ('switch on the television', 'television-on'),
    ('turn on the television', 'television-on'),

    ('did you switch on the television', 'television-on-inquiry'),
    ('have you switched on the television', 'television-on-inquiry'),

    ('switch off the television', 'television-off'),
    ('turn off the television', 'television-off'),

    ('did you switch off the television', 'television-off-inquiry'),
    ('have you switched off the television', 'television-off-inquiry'),

# -------------------- Elevator ------------------------- #

    ('call the elevator', 'elevator-calling'),
    ('did you call the elevator', 'elevator-calling-inquiry'),
    ('have you called the elevator', 'elevator-calling-inquiry'),

# -------------------- Weather inquiry ------------------------- #

    ('what is the weather today in ', 'weather-inquiry')

]

C = NaiveBayesClassifier(train)

def classify(text):
    return C.classify(text)

