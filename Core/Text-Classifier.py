from textblob.classifiers import NaiveBayesClassifier

class TextClassifier:



    def __init__(self):

        trainList = []
        testList = []
        TC = 'cl'

    def Train(self,trainList = []):
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
        self.TC = NaiveBayesClassifier(self.testList)

   
   
    def result(self,Text):
        return self.TC.classify(Text)

 
 
   # def Setup(self):
    #    Train()
     #   Test()
      #  TextClassify()
        







obj = TextClassifier()
obj.Train()
obj.Test()
obj.TextClassify()
print(obj.result("switch on the light"))
print(obj.result("turn off the light"))
print(obj.result("open the light"))
print(obj.result("turn the light off"))

# Classify some text
#print(cl.classify("switch on the light"))  
#print(cl.classify("turn off the light"))   

#print(cl.classify("open the light"))  
#print(cl.classify("turn the light off"))  