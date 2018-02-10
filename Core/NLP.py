# NOTE: this file requires NLTK

#Importing the modules
import re
import nltk
from nltk.tokenize import regexp_tokenize
from nltk.corpus import wordnet
from nltk.tree import Tree
import Core.spell

class NLP:

    def __init__(self):
        self.text = ""
        self.tokens = []
        self.tagged_tokens = []
        self.namedEnts = []
        self.info = []


    # 1. Expanding Contractions | Need to be improved - adding another contractions - and tested by all the possible commands contractions
    def Expand(self):

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
    def tokenize(self):
        self.tokens = regexp_tokenize(self.text, pattern = "[\w']+")

    # 3. Spelling Correction | Unfinished yet => The corpora needs to be reinforced by the rest commands
    def correct(self):
        self.tokens = [Core.spell.correction(token) for token in self.tokens]

    # Temporary : Untill I reach Stanford Core NLP Tagger
    # 4. Performing POS-Tagging over the resulted tokens and save the result into a new list of tagged tokens called tagged_tokens
    def tag(self):
        self.tagged_tokens = nltk.pos_tag(self.tokens)

    # 5. Extracting Recognized Named-Entities such as : Person, Organization
    def Recognize(self):
        NER = nltk.ne_chunk(self.tagged_tokens)

        for NE in NER:
            if hasattr(NE, 'label'):
                temp = NE.label(), ' '.join(N[0] for N in NE)
                self.namedEnts.append(temp)

    # 6. Information Extractor
    def Extract(self):
        chunkGram = r"""
        
            # Light off
            chunk:
            {<VB><RP><DT><NN>}
            }<VB>{
            }<DT>{
            
            # Light on
            
            # Temperature
            chunk:
            {<VB><DT><NN><TO><CD>}
            }<VB><DT>{
            }<TO>{
            
                    
        """

        chunkParser = nltk.RegexpParser(chunkGram)
        chunked = chunkParser.parse(self.tagged_tokens)

        chunked.draw()

        for element in chunked:
            if hasattr(element, 'label'):
                temp = ' '.join(e[0] for e in element)
                self.info.append(temp)