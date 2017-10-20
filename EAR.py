# Wattary's Ear
# NOTE: this file requires NLTK & PyAudio & Python Speech Recognition Engine because it uses the Microphone class

#Importing the modules
import speech_recognition as sr
import nltk
from nltk.tokenize import regexp_tokenize
from nltk.corpus import wordnet
import re

class EAR:

    text = "I loooooove yooouuu"
    tokens = []

    # Speech-To-Text
    def Listen(self):
        # obtaining audio from the microphone
        with sr.Microphone() as source:
            print('Listening!')
            audio = sr.Recognizer().listen(source)

        # recognize speech using Google Speech Recognition
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")` instead of `r.recognize_google(audio)`

        try:
            # Saving recognized text into text variable
            self.text = sr.Recognizer().recognize_google(audio)
        except sr.UnknownValueError:
            print("I can't hear you, Could you repeat that please? ")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # Expanding Contractions
    def Expand(self):

        replacement_patterns = [
            (r'won\'t', 'will not'),
            (r'can\'t', 'can not'),
            (r'I\'m', 'I am'),
            (r'ain\'t', 'is not'),
            (r'(\w+)\'ll', '\g<1> will'),
            (r'(\w+)n\'t', '\g<1> not'),
            (r'(\w+)\'ve', '\g<1> have'),
            (r'(\w+)\'s', '\g<1> is'),
            (r'(\w+)\'re', '\g<1> are'),
            (r'(\w+)\'d', '\g<1> would')
        ]

        patterns = [(re.compile(regex), repl) for (regex, repl) in replacement_patterns]

        for (pattern, repl) in patterns:
            self.text = re.sub(pattern, repl, self.text)

    # Repeating eliminator
    def replace(self, word):
        repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        repl = r'\1\2\3'

        if wordnet.synsets(word):
            return word
        repl_word = repeat_regexp.sub(repl, word)
        if repl_word != word:
            return self.replace(repl_word)
        else:
            return repl_word

    def Eliminator(self):
        self.tokens = [self.replace(token) for token in self.tokens]

    # Performing word tokenization over the resulted text and save the result into a new list of tokens called tokens
    def tokenize(self):
        self.tokens = regexp_tokenize(self.text, pattern = "[\w']+")