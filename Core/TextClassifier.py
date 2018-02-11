# Importing the textbolb Module
from textblob.classifiers import NaiveBayesClassifier

trainList = []
testList = []



trainList = [
        ('Switch on the light', 'light_on'),
        ('turn on the light', 'light_on'),
        ('open the light', 'light_on'),
        ('open up the light', 'light_on'),
        ('Switch off the light', 'light_off'),
        ('turn off the light', 'light_off'),
        ('close the ligh', 'light_off')
]




testList = [

        ('Switch on the light', 'light_on'),
        ('turn on the light', 'light_on'),
        ('open the light', 'light_on'),
        ('open up the light', 'light_on'),
        ('Switch off the light', 'light_off'),
        ('turn off the light', 'light_off'),
        ('close the ligh', 'light_off'),
        ('switch the light on', 'light_on'),
        ('switch the light off', 'light_off')
]

   
   
obj = NaiveBayesClassifier(testList)

   
def result(Te):
    """Return the Output of Text Classification"""
    
    return obj.classify(Te) 


print(result("switch on the light"))

print(result("turn the light off"))
