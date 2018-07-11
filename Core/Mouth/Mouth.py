# The Mouth of Wattary

from nltk.parse.generate import generate
from Grammar import *
import random

class Mouth:

    def __init__(self):
        self.sentences = []
        self.respone = ''

    def generate(self, grammar):
        for sentence in generate(grammar, n = 20):
            self.sentences.append((' '.join(sentence)))

    def choose(self):
        self.respone = random.choice(self.sentences)

    def speak(self, intent, tense):
        if intent == 'greeting':
            self.generate(greeting)
        elif intent == 'status-query':
            self.generate(statusQuery)
        elif intent == 'name-query':
            self.generate(nameQuery)
        elif intent == 'light-on' and tense == 'imperative':
            self.generate(lightOn)
        elif intent == 'light-off' and tense == 'imperative':
            self.generate(lightOff)
        elif intent == 'temperature-update': # For Testing purposes
            self.generate(disability)
        elif intent == 'elevator-calling' and tense == 'imperative':
            self.generate(elevatorCalling)
        elif 'query' in intent and tense == 'past-simple':
            self.generate(pastSimpleQuery)
        elif 'query' in intent and tense == 'present-perfect':
            self.generate(presentPerfectQuery)
        else:
            self.generate(oneWord)
        self.choose()

        #testing
        self.sentences = []



# =========================================
# Just for testing purposes
