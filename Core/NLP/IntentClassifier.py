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

# -------------------- Light ------------------------- #

    ('switch on the light', 'light-on'),
    ('turn on the light', 'light-on'),
    ('open up the light', 'light-on'),

    ('switch off the light', 'light-off'),
    ('turn off the light', 'light-off'),
    ('close the light', 'light-off'),

    ('did you switch on the light', 'light-on-query'),
    ('have you switched on the light', 'light-on-query'),
    ('did you turn on the light', 'light-on-query'),
    ('have you turned on the light', 'light-on-query'),
    ('did you open up the light', 'light-on-query'),
    ('have you opened up the light', 'light-on-query'),

    ('did you switch off the light', 'light-off-query'),
    ('have you switched off the light', 'light-off-query'),
    ('did you turn off the light', 'light-off-query'),
    ('have you switched off the light', 'light-off-query'),
    ('did you close the light', 'light-off-query'),
    ('have you closed the light', 'light-off-query'),

# -------------------- Temperature ------------------------- #

    ('set the temperature to', 'temperature-update'),
    ('update the temperature to ', 'temperature-update'),
    ('set the air conditioning to', 'temperature-update'),
    ('update the air conditioning to ', 'temperature-update'),

    ("did you set the temperature to", 'temperature-update-query'),
    ("did you set the air conditioner", 'temperature-update-query'),
    ("did you update the temperature to", "temperature-update-query"),
    ("did you update the air conditioning to", "temperature-update-query"),

    ("have you set the temperature to", "temperature-update-query"),
    ("have you set the air conditioner to", "temperature-update-query"),
    ("have you updated the temperature to", "temperature-update-query"),
    ("have you updated the air conditioning to", "temperature-update-query"),

# -------------------- air conditioning ------------------------- #

    ('switch on the air conditioning', 'air-conditioning-on'),
    ('turn on the air conditioning', 'air-conditioning-on'),

    ('switch on the air conditioner', 'air-conditioning-on'),
    ('turn on the air conditioner', 'air-conditioning-on'),

    ('did you switch on the air conditioning', 'air-conditioning-on-query'),
    ('did you turn on the air conditioning', 'air-conditioning-on-query'),
    ('have you switched on the air conditioning', 'air-conditioning-on-query'),
    ('have you turned on the air conditioning', 'air-conditioning-on-query'),

    ('did you switch on the air conditioner', 'air-conditioning-on-query'),
    ('did you turn on the air conditioner', 'air-conditioning-on-query'),
    ('have you switched on the air conditioner', 'air-conditioning-on-query'),
    ('have you turned on the air conditioner', 'air-conditioning-on-query'),

    ('switch off the air conditioning', 'air-conditioning-off'),
    ('turn off the air conditioning', 'air-conditioning-off'),

    ('switch off the air conditioner', 'air-conditioning-off'),
    ('turn off the air conditioner', 'air-conditioning-off'),

    ('did you switch off the air conditioning', 'air-conditioning-off-query'),
    ('did you turn off the air conditioning', 'air-conditioning-off-query'),
    ('have you switched off the air conditioning', 'air-conditioning-off-query'),
    ('have you turned off the air conditioning', 'air-conditioning-off-query'),

    ('did you switch off the air conditioner', 'air-conditioning-off-query'),
    ('did you turn off the air conditioner', 'air-conditioning-off-query'),
    ('have you switched off the air conditioner', 'air-conditioning-off-query'),
    ('have you turned off the air conditioner', 'air-conditioning-off-query'),

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

# -------------------- Coffe Machine ------------------------- #

    ('switch on the coffee machine', 'coffee-machine-on'),
    ('turn on the coffee machine', 'coffee-machine-on'),
    ('open up the coffee machine', 'coffee-machine-on'),

    ('switch off the coffee machine', 'coffee-machine-off'),
    ('turn off the coffee machine', 'coffee-machine-off'),
    ('close the coffee machine', 'coffee-machine-off'),

    ('did you switch on the coffee machine', 'coffee-machine-on-query'),
    ('have you switched on the coffee machine', 'coffee-machine-on-query'),
    ('did you turn on the coffee machine', 'coffee-machine-on-query'),
    ('have you turned on the coffee machine', 'coffee-machine-on-query'),
    ('did you open up the coffee machine', 'coffee-machine-on-query'),
    ('have you opened up the coffee machine', 'coffee-machine-on-query'),

    ('did you switch off the coffee machine', 'coffee-machine-off-query'),
    ('have you switched off the coffee machine', 'coffee-machine-off-query'),
    ('did you turn off the coffee machine', 'coffee-machine-off-query'),
    ('have you switched off the coffee machine', 'coffee-machine-off-query'),
    ('did you close the coffee machine', 'coffee-machine-off-query'),
    ('have you closed the coffee machine', 'coffee-machine-off-query'),

# -------------------- Router ------------------------- #

    ('switch on the router', 'router-on'),
    ('turn on the router', 'router-on'),
    ('open up the router', 'router-on'),

    ('switch off the router', 'router-off'),
    ('turn off the router', 'router-off'),
    ('close the router', 'router-off'),

    ('did you switch on the router', 'router-on-query'),
    ('have you switched on the router', 'router-on-query'),
    ('did you turn on the router', 'router-on-query'),
    ('have you turned on the router', 'router-on-query'),
    ('did you open up the router', 'router-on-query'),
    ('have you opened up the router', 'router-on-query'),

    ('did you switch off the router', 'router-off-query'),
    ('have you switched off the router', 'router-off-query'),
    ('did you turn off the router', 'router-off-query'),
    ('have you switched off the router', 'router-off-query'),
    ('did you close the router', 'router-off-query'),
    ('have you closed the router', 'router-off-query'),

# -------------------- Water Tap ------------------------- #

    ('open the water tap', 'water-tap-on'),
    ('open the water tap', 'water-tap-on'),

    ('close the water tap', 'water-tap-off'),
    ('close the water tap', 'water-tap-off'),

    ('did you open the water tap', 'water-tap-on-query'),
    ('have you opened the water tap', 'water-tap-on-query'),

    ('did you close the water tap', 'water-tap-off-query'),
    ('have you closed the water tap', 'water-tap-off-query'),

# -------------------- Elevator ------------------------- #

    ('call the elevator', 'elevator-calling'),
    ('call the elevator', 'elevator-calling'),
    ('did you call the elevator', 'elevator-calling-query'),
    ('have you called the elevator', 'elevator-calling-query'),

# -------------------- Door ------------------------- #

    ('open the door', 'door-opening'),
    ('open the door', 'door-opening'),
    ('open the door', 'door-opening'),
    ('did you open the door', 'door-opening-query'),
    ('have you opened the door', 'door-opening-query'),
    ('have you opened the door', 'door-opening-query'),

# -------------------- Car Engine ------------------------- #

    ('switch on the car engine', 'car-engine-on'),
    ('switch on the engine of the car', 'car-engine-on'),
    ('switch on the engine of the car', 'car-engine-on'),
    ('turn on the engine of the car', 'car-engine-on'),
    ('turn on the car engine', 'car-engine-on'),
    ('did you switch on the car engine', 'car-engine-on-query'),
    ('have you switched on the car engine', 'car-engine-on-query'),
    ('have you switched on the car engine', 'car-engine-on-query'),

    ('switch off the car engine', 'car-engine-off'),
    ('switch off the engine of the car', 'car-engine-off'),
    ('switch off the engine of the car', 'car-engine-off'),
    ('turn off the engine of the car', 'car-engine-off'),
    ('turn off the car engine', 'car-engine-off'),
    ('did you switch off the car engine', 'car-engine-off-query'),
    ('have you switched off the car engine', 'car-engine-off-query'),
    ('have you switched off the car engine', 'car-engine-off-query'),

# -------------------- Car Door ------------------------- #

    ('open the car door', 'car-door-opening'),
    ('open the car door', 'car-door-opening'),
    ('open the door of the car', 'car-door-opening'),
    ('open the door of the car', 'car-door-opening'),

    ('close the car door', 'car-door-closing'),
    ('close the door of the car', 'car-door-closing'),

    ('did you open the car door', 'car-door-opening-query'),
    ('did you open the door of the car', 'car-door-opening-query'),

    ('have you opened the car door', 'car-door-opening-query'),
    ('have you opened door of the car', 'car-door-opening-query'),

    ('did you close the car door', 'car-door-closing-query'),
    ('did you close the door of the car', 'car-door-closing-query'),
    ('have you closed the car door', 'car-door-closing-query'),
    ('have you closed door of the car', 'car-door-closing-query'),

# -------------------- Weather inquiry ------------------------- #

    ('what is the weather today in ', 'weather-inquiry'),
    ('what is the weather tomorrow in ', 'weather-inquiry'),
    ('what is the weather', 'weather-inquiry'),

# -------------------- visitor inquiry ------------------------- #

    ('who is that', 'visitor-query'),

# -------------------- Movies Recommendation ------------------------- #

    ('recommend me a movie', 'movie-recommendation'),
    ('recommend me a movie', 'movie-recommendation'),
    ('recommend me a movie', 'movie-recommendation'),
    ('recommend me a movie', 'movie-recommendation'),
    ('recommend me a movie', 'movie-recommendation'),

    ('recommend me a series', 'series-recommendation'),
    ('recommend me a series', 'series-recommendation'),
    ('recommend me a series', 'series-recommendation'),
    ('recommend me a series', 'series-recommendation'),
    ('recommend me a series', 'series-recommendation'),

]

C = NaiveBayesClassifier(train)

def classify(text):
    return C.classify(text)

