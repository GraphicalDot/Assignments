#!/usr/bin/env python
import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
import time
class Vasu:

        def __init__(self, u):
            self.u = u

        def timer(fun):
            def wrap(*args):
                start = time.time()
                ret = fun(*args)
                end = time.time()
                print '%s function took %0.3f ms' % (fun.func_name, (end-start)*1000)
                return ret
            return wrap

        @timer
        def do_tokenize(self):
            punkt_param = PunktParameters()                                                                                                             
            punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc', 'i.e'])                                                             
            sentence_splitter = PunktSentenceTokenizer(punkt_param)                                                                                     
            tokenized_sentences = sentence_splitter.tokenize(self.u)
            print tokenized_sentences
    
if __name__ == '__main__':
        
        h = raw_input("Enter review:")
        b = Vasu(h)
        b.do_tokenize()
        ("""We ordered some kebabs and smoked cheeseballs. The latter was quite good. Even kebabs weren't that bad. Although the quantity is not worth the price even in a platter. Otherwise, it has an extensive menu with wide range of cuisines to choose from.""")
