#!/usr/bin/env python

import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
from pattern.en import sentiment
import itertools
import time

class Test1:

        def __init__(self, u):
            self.u = u


        def t_ime(f):
            def wrap(*args):
                time1 = time.time()
                ret = f(*args)
                time2 = time.time()
                print '\n%s function took %0.3f ms\n' % (f.func_name, (time2-time1)*1000.0)
                return ret
            return wrap


        @t_ime
        def do_tokenize(self):
            punkt_param = PunktParameters()                                                                                                              
            punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'ms', 'prof', 'inc', 'i.e'])                                                        
            sentiment_splitter = PunktSentenceTokenizer(punkt_param)                                                                                     
            self.tokenized_sentences = sentiment_splitter.tokenize(self.u)
            print '\nTokenized sentence\n'
            print self.tokenized_sentences

        @t_ime
        def break_on(self):                                                                                                                              
            L1 = self.tokenized_sentences                                                                                                                
            l = len(L1)                                                                                                                                  
            L2 = ['and', 'is']                                                                        
            yo = [self.tokenized_sentences[j].split(x) for j in range(l) for x in L2]                                                                    
            self.on_preposition_sentences = list(itertools.chain(*yo))
            print '\nBreak on preposition-\n'
            print  self.on_preposition_sentences


        @t_ime 
        def sent_anal(self):                                                                                                                             
            l1 = len(self.on_preposition_sentences)                                                                                                      
            yo1 = [sentiment(self.on_preposition_sentences[j]) for j in range(l1)]
            print '\nSentiment analysis\n'
            print yo1

if __name__ == "__main__":
        s = raw_input("Enter your review :")                                  
        print s
        a = Test1(s)
        a.do_tokenize()                                                                                                                                  
        a.break_on()                                                                                                                                     
        a.sent_anal()
