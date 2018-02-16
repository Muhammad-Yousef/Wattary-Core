# Importing the modules
import re
import nltk
from nltk.tokenize import regexp_tokenize
import Core.spell
import Core.IntentClassifier


class NLP:

    def __init__(self):
        self.text = input()
        self.tokens = []
        self.corrected = []
        self.intent = ''
        self.tagged_tokens = []
        self.info = []

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
        self.corrected = [Core.spell.correction(token) if not re.match('[0-9]', token) else token for token in self.tokens]

    # 4. Intent-Detector
    def detector(self):
        self.intent = Core.IntentClassifier.C.classify(' '.join(self.corrected))

    # Temporary : Untill I reach Stanford Core NLP Tagger
    # 5. Performing POS-Tagging over the resulted tokens and save the result into a new list of tagged tokens called tagged_tokens
    def tagger(self):
        self.tagged_tokens = nltk.pos_tag(self.corrected)

    # 6. Information Extractor
    def extractor(self):

        if self.intent in ('light-on', 'light-off', 'air-conditioning-on', 'air-conditioning-off',
                           'television-off', 'television-on'):
            chunkGram = r"""
               
               # A grammar for the pattern [Switch/Turn on/off the device in the place]
               
               chunk:
               {<DT><NN>+<VBG>|<DT><NN>+}
               }<DT>{
               
               chunk:
               {<NN><IN><DT>}
               }<NN>{
               }<DT>{
               
               chunk:
               {<RP>}
               
            """
        elif self.intent == 'temperature-update':
            chunkGram = r"""
            
                chunk:
                {<VB><DT><NN><TO><CD><IN><DT><NN>+}
                }<VB>{
                }<DT>{
                }<TO>{
                }<IN>{
            
            """

        elif self.intent == 'elevator-calling':
            chunkGram = r"""
            
                chunk:
                {<VB><DT><NN>}
                }<VB>{
                }<DT>{
            
            """

        elif self.intent == 'weather-inquiry':
            chunkGram = r"""
            
                chunk:
                {<WP><VBZ><DT><NN><NN><IN><NN>+}
                }<WP>{
                }<VBZ>{
                }<DT>{
                }<IN>{
                <NN>}{<NN>
            
            """


        chunkParser = nltk.RegexpParser(chunkGram)
        chunked = chunkParser.parse(self.tagged_tokens)

        # Temporary: Should be deleted unless we are in presentation mode
        chunked.draw()

        for element in chunked:
            if hasattr(element, 'label'):
                temp = ' '.join(e[0] for e in element)
                self.info.append(temp)

    # 7. Executor
    def executor(self):
        self.expander()
        self.tokenizer()
        self.corrector()
        self.detector()
        self.tagger()
        self.extractor()

# ====================================
# Temporal : For testing purposes

while True:
    A = NLP()
    A.executor()
    print('Intent =', A.intent)
    print('Text =', A.text)
    print('Tokens =', A.tokens)
    print('Corrected Tokens =', A.corrected)
    print('Tagged Tokens =', A.tagged_tokens)
    print('Extracted Information =', A.info)