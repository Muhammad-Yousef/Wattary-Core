# Importing the modules
import re
import nltk
from nltk.tokenize import regexp_tokenize
import sys
sys.path.append('../Core/NLP')
sys.path.append('../Core/Mouth')
import spell
import IntentClassifier
import TenseClassifier

from Testing import *
from Mouth import *


class NLP:

    def __init__(self):
        self.text = ''
        self.tokens = []
        self.corrected = []
        self.intent = ''
        self.tense = ''
        self.tagged_tokens = []
        self.info = []
        self.information = {}

    # 1. Expanding Contractions | Need to be improved - adding another contractions - and tested by all the possible commands contractions
    def expander(self):

        replacement_patterns = [
            (r'wanna', 'want to'),
            (r'gonna', 'going to'),
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

    # 2. Performing word tokenization over the resulted text and save the result into a new list of tokens called tokens
    def tokenizer(self):
        self.tokens = regexp_tokenize(self.text, pattern="[\w'\.]+")

    # 3. Spelling Correction | Unfinished yet => The corpus needs to be reinforced by the rest commands
    def corrector(self):
        self.corrected = [spell.correction(token) if not re.match('[0-9]', token) else token for token in self.tokens]

    # 4. Intent & Tense Detection
    def detector(self):
        self.intent = IntentClassifier.C.classify(' '.join(self.corrected))

        if self.intent in ('greeting', 'status-query', 'name-query', 'age-query', 'weather-query'):
            self.tense = ''
        elif 'inquiry' in self.intent:
            self.tense = 'inquiry'
        elif 'query' not in self.intent:
            self.tense = 'imperative'
        else:
            self.tense = TenseClassifier.C.classify(' '.join(self.corrected))

    # Temporary : Untill I reach Stanford Core NLP Tagger
    # 5. Performing POS-Tagging over the resulted tokens and save the result into a new list of tagged tokens called tagged_tokens
    def tagger(self):
        self.tagged_tokens = nltk.pos_tag(self.corrected)

    # 6. Information Extractor
    def extractor(self):

        if self.intent not in ('weather-inquiry', 'greeting', 'status-query', 'name-query', 'age-query', 'movie-recommendation', 'series-recommendation'):
            chunkGram = r"""

            chunk:
            {<DT><NN>+<VBG>|<DT><NN|NNS>+}
            }<DT>{

            chunk:
            {<NN><IN><DT>}
            }<NN>{
            }<DT>{

            chunk:
            {<VB|VBN><RP|IN>}
            }<VB>{
            }<VBN>{

            chunk:
            {<CD>}

        """

        elif self.intent == 'weather-inquiry':
            chunkGram = r"""

            chunk:
            {<WP><VBZ><DT><NN><NN><IN><NNP|NN>+}
            }<WP>{
            }<VBZ>{
            }<DT>{
            }<IN>{
            <NN>}{<NN>

        """

        elif 'recommendation' in self.intent:
            chunkGram = r"""

            chunk:
            {<JJ>?<NN>+}
            <JJ>}{<NN>
            <NN>}{<NN>

            """


        chunkParser = nltk.RegexpParser(chunkGram)
        chunked = chunkParser.parse(self.tagged_tokens)

        # Temporary: Should be deleted unless we are in presentation mode
        #chunked.draw()

        self.info = []

        for element in chunked:
            if hasattr(element, 'label'):
                temp = ' '.join(e[0] for e in element)
                self.info.append(temp)

    # 7. Organizer : Under construction
    def organizer(self):
        flag = 0
        for piece in self.info:
            if piece.isdigit():
                flag = 1

        if 'inquiry' in self.intent:
            self.information = {'Inquiry': self.info[0], 'Date': self.info[1], 'Location': self.info[2]}
        elif len(self.info) == 3 and flag == 0:
            if self.info[0] == 'up':
                self.info[0] = 'on'
            self.information = {'State':self.info[0], 'Appliance':self.info[1], 'Location':self.info[2]}
        elif len(self.info) == 3 and flag == 1:
            self.information = {'Appliance':self.info[0], 'Degree':self.info[1], 'Location':self.info[2]}
        elif len(self.info) == 2 and self.info[0] in ('on', 'off', 'up'):
            self.information = {'State':self.info[0], 'Appliance':self.info[1]}
        elif len(self.info) == 2 and self.info[0] not in ('on', 'off', 'up'):
            if 'recommendation' in self.intent:
                self.information = {'Category': self.info[0], 'Type': self.info[1]}
            elif 'on' in self.intent or 'up' in self.intent or 'opening' in self.intent:
                state = 'on'
                self.information = {'State': state, 'Appliance': self.info[0], 'Location': self.info[1]}
            elif 'off' in self.intent or 'closing' in self.intent:
                state = 'off'
                self.information = {'State': state, 'Appliance': self.info[0], 'Location': self.info[1]}

        elif len(self.info) == 1:
            if 'calling' in self.intent or 'opening' in self.intent:
                self.information = {'Appliance':self.info[0]}
            else:
                if 'on' in self.intent or 'up' in self.intent:
                    state = 'on'
                    self.information = {'State': state, 'Appliance': self.info[0]}
                elif 'off' in self.intent:
                    state = 'off'
                    self.information = {'State': state, 'Appliance': self.info[0]}



    # 8. Executor
    def execute(self, text):
        self.text = text
        self.expander()
        self.tokenizer()
        self.corrector()
        self.detector()

        if self.intent not in ('greeting', 'status-query', 'name-query', 'age-query'):
            self.tagger()
            self.extractor()
            self.organizer()


# Testing purposes

# A = NLP()
# B = Mouth()
# for command in commands:
#     A.execute(command)
#     print('Text = ', A.text)
#     print('Intent = ', A.intent)
#     print('Tense = ', A.tense)
#     print('Tokens = ', A.tokens)
#     print('Tagged Tokens = ', A.tagged_tokens)
#     print('Information = ', A.info)
#     print('Extracted information Dictionary = ', A.information)
#     print()
#     print('Wattary Response =', end = ' ')
#     B.speak(A.intent, A.tense)
#     print(B.respone)
