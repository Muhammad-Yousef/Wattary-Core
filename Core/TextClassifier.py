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
        ('close the ligh', 'light_off'),
        ('is the light off?', 'light_off_inquirey'),
        ('did you turn off the light?', 'light_off_inquirey'),
        ('is the light on?', 'light_on_inquirey'),
        ('did you turn on the light?', 'light_on_inquirey'),
        ('is the light turned off?', 'light_off_inquirey'),
     
        
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
        ('switch the light off', 'light_off'),
        ('is the light off?', 'light_off_inquirey'),
        ('did you turn off the light?', 'light_off_inquirey'),
        ('is the light on?', 'light_on_inquirey'),
        ('did you turn on the light?', 'light_on_inquirey'),
        ('did you close the light?', 'light_off_inquirey'),
        ('is the light turned on?', 'light_on_inquirey'),
        ('did you open the light?', 'light_on_inquirey'),
        ('is the light opened?', 'light_on_inquirey'),
        ('is the light closed?', 'light_off_inquirey')
        

]

   
   
obj = NaiveBayesClassifier(testList)

   
def result(Te):
    """Return the Output of Text Classification"""
    
    return obj.classify(Te) 


print(result("is the light on "))
print(result("did you turned off the light"))
print(result("turn the light off"))
print(result("is the light open"))
print(result("did you close the light"))
