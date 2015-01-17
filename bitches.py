#!/usr/bin/env python

import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
from pattern.en import sentiment
import itertools
import time

class Test1:
        def __init__(self,s):
            self.s = s

        def timing(f):
            def wrap(*args):
                time1 = time.time()
                ret = f(*args)
                time2 = time.time()
                print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
                return ret
            return wrap

        @timing
        def do_tokenize(self):
            punkt_param = PunktParameters()
            punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc', 'i.e'])
            sentence_splitter = PunktSentenceTokenizer(punkt_param)
            self.tokenized_sentences = sentence_splitter.tokenize(self.s)
            print self.tokenized_sentences

        @timing
        def break_on(self):
            L1 = self.tokenized_sentences
            l = len(L1)
            L2 = [' is',' and']
            yo = [self.tokenized_sentences[j].split(x) for j in range(l) for x in L2]
            self.on_prepositions_sentences = list (itertools.chain(*yo))
            print self.on_prepositions_sentences
    
        @timing
        def sent_anal(self):
            l1 = len(self.on_prepositions_sentences)
            yo1 = [sentiment(self.on_prepositions_sentences[j]) for j in range(l1)]
            print yo1


if __name__ == '__main__':
 
        h = raw_input("Enter review:")
        a = Test1(h)
        a.do_tokenize()
        a.break_on()
        a.sent_anal()
