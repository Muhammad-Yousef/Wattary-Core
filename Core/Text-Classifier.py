# Importing the textbolb Module
from textblob.classifiers import NaiveBayesClassifier


# ----------------------------------------------------- TextClassifier Class -----------------------------------#

class TextClassifier:



    def __init__(self):
        """Initliazing some variables"""

        trainList = []
        testList = []
        TC = 'cl'

    def Train(self,trainList = []):
        """asigning the Training data to a List of Tupples"""

        self.trainList  = [
            ('Switch on the light', 'light_on'),
            ('turn on the light', 'light_on'),
            ('open the light', 'light_on'),
            ('open up the light', 'light_on'),
            ('Switch off the light', 'light_off'),
            ('turn off the light', 'light_off'),
            ('close the ligh', 'light_off')
        ]
        
        


    def Test(self,testList = []):
        """asigning the Testing data to a List of Tupples"""

        self.testList = [

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

   
   
    def TextClassify(self):
        """The Process of Text Classification"""

        '''
        Making an object of NaiveBayesClassifier
        and call the constructor Function and pass the train data as parameter        
        '''
        self.TC = NaiveBayesClassifier(self.testList)

   
   
    def result(self,Text):
        """Return the Output of Text Classification"""

        return self.TC.classify(Text)

 
 
# --------------------------------------------------Just for Testing---------------------------------------#

obj = TextClassifier()
obj.Train()
obj.Test()
obj.TextClassify()
print(obj.result("switch on the light"))
print(obj.result("turn off the light"))
print(obj.result("open the light"))
print(obj.result("turn the light off"))

