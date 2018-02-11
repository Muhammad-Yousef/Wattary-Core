# Importing the textbolb Module
from textblob.classifiers import NaiveBayesClassifier

trainList = []
testList = []
TC = 'cl'


def Train(trainList=[]):
    """asigning the Training data to a List of Tupples"""

    trainList = [
        ('Switch on the light', 'light_on'),
        ('turn on the light', 'light_on'),
        ('open the light', 'light_on'),
        ('open up the light', 'light_on'),
        ('Switch off the light', 'light_off'),
        ('turn off the light', 'light_off'),
        ('close the ligh', 'light_off')
    ]


def Test(testList = []):
    """asigning the Testing data to a List of Tupples"""

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

   
   
def TextClassify():
    """The Process of Text Classification"""

    '''
    Making an object of NaiveBayesClassifier
    and call the constructor Function and pass the train data as parameter        
    '''
    TC = NaiveBayesClassifier(testList)

   
def result(Text):
    """Return the Output of Text Classification"""

    return TC.classify(Text)


Train()
Test()
TextClassify()
print(result("switch on the light"))


