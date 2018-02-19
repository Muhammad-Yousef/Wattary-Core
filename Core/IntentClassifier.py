from textblob.classifiers import NaiveBayesClassifier

train = [

# -------------------- Greeting ------------------------- #

    ('hello', 'greeting'),
    ('howdy', 'greeting'),
    ('hey', 'greeting'),
    ('hi', 'greeting'),

    ('how are you', 'status-query'),
    ('how is it going', 'status-query'),
    ('how is it going with you', 'status-query'),

    ('what is your name', 'name-query'),
    ('tell me your name', 'name-query'),

    ('how old', 'age-query'),
    ('how old are you', 'age-query'),
    ('what is your age', 'age-query'),

# -------------------- Light ------------------------- #

    ('switch on the light', 'light-on'),
    ('turn on the light', 'light-on'),
    ('open up the light', 'light-on'),

    ('switch off the light', 'light-off'),
    ('turn off the light', 'light-off'),
    ('close the light', 'light-off'),

    ('did you switch on the light', 'light-on-query'),
    ('have you switched on the light', 'light-on-query'),

    ('did you switch off the light', 'light-off-query'),
    ('have you switched off the light', 'light-off-query'),

# -------------------- Temperature ------------------------- #

    ('set the temperature to', 'temperature-update'),
    ('update the temperature to ', 'temperature-update'),

    ("did you set the temperature to", 'temperature-update-query'),
    ("did you set the air conditioner", 'temperature-update-query'),
    ("did you update the temperature to", "temperature-update-query"),

    ("have you set the temperature to", "temperature-update-query"),
    ("have you set the air conditioner to", "temperature-update-query"),
    ("have you updated the temperature to", "temperature-update-query"),

# -------------------- air conditioning ------------------------- #

    ('switch on the air conditioning', 'air-conditioning-on'),
    ('turn on the air conditioning', 'air-conditioning-on'),

    ('did you switch on the air conditioning', 'air-conditioning-on-query'),
    ('have you switched on the air conditioning', 'air-conditioning-on-query'),

    ('switch off the air conditioning', 'air-conditioning-off'),
    ('turn off the air conditioning', 'air-conditioning-off'),

    ('did you switch off the air conditioning', 'air-conditioning-off-query'),
    ('have you switched off the air conditioning', 'air-conditioning-off-query'),

# -------------------- TV ------------------------- #

    ('switch on the television', 'television-on'),
    ('turn on the television', 'television-on'),
    ('switch on the tv', 'television-on'),
    ('turn on the tv', 'television-on'),

    ('did you switch on the television', 'television-on-query'),
    ('have you switched on the television', 'television-on-query'),
    ('did you switch on the tv', 'television-on-query'),
    ('have you switched on the tv', 'television-on-query'),

    ('did you turn on the television', 'television-on-query'),
    ('have you turned on the television', 'television-on-query'),
    ('did you turn on the tv', 'television-on-query'),
    ('have you turned on the tv', 'television-on-query'),

    ('switch off the television', 'television-off'),
    ('turn off the television', 'television-off'),
    ('switch off the tv', 'television-off'),
    ('turn off the tv', 'television-off'),

    ('did you switch off the television', 'television-off-query'),
    ('have you switched off the television', 'television-off-query'),
    ('did you switch off the tv', 'television-off-query'),
    ('have you switched off the tv', 'television-off-query'),

    ('did you turn off the television', 'television-off-query'),
    ('have you turned off the television', 'television-off-query'),
    ('did you turn off the tv', 'television-off-query'),
    ('have you turned off the tv', 'television-off-query'),

# -------------------- Elevator ------------------------- #

    ('call the elevator', 'elevator-calling'),
    ('call the elevator', 'elevator-calling'),
    ('did you call the elevator', 'elevator-calling-query'),
    ('have you called the elevator', 'elevator-calling-query'),

# -------------------- Door ------------------------- #

    ('open the door', 'door-opening'),
    ('did you open the door', 'door-opening-query'),
    ('have you opened the door', 'door-opening-query'),

# -------------------- Car Engine ------------------------- #

    ('switch on the car engine', 'car-engine-on'),
    ('switch on the engine of the car', 'car-engine-on'),
    ('turn on the engine of the car', 'car-engine-on'),
    ('turn on the car engine', 'car-engine-on'),
    ('did you switch on the car engine', 'car-engine-on-query'),
    ('have you switched on the car engine', 'car-engine-on-query'),

    ('switch off the car engine', 'car-engine-off'),
    ('switch off the engine of the car', 'car-engine-off'),
    ('turn off the engine of the car', 'car-engine-off'),
    ('turn off the car engine', 'car-engine-off'),
    ('did you switch off the car engine', 'car-engine-off-query'),
    ('have you switched off the car engine', 'car-engine-off-query'),

# -------------------- Weather inquiry ------------------------- #

    ('what is the weather today in ', 'weather-query')

]

C = NaiveBayesClassifier(train)

def classify(text):
    return C.classify(text)

