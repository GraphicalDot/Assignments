#!/usr/bin/anv python

class Test1:
        
        def __init__(*args, **kwargs):
            pass

        def do_tokenize(self, *args, **kwargs):
            pass
        
        def break_on(self, *args, **kwargs):
            pass
        
        
        def method_one(self, *args, **kwargs):
            """
            use this method as a class method
            """
            pass
        

        def method_two(self, *args, **kwargs):
            """
            use this method as a class method
            """
            pass


if __name__ == "__main__":
        """
        pass a text("A paragraph")
        Pass a list of prepostions to this class, 
        
        do_tokenize : wil take the text and break the text in the list of the sentences and will make this 
        list as a class variable which will be accesible to the other class methods. name: tokenized_sentences
        
        break_on met: Will take the class variable tokenized_sentences and break the sentences on the basis of the 
        list or prepositions givent ot htis class.
        make it a class variable : on_prepositions_sentences


        sentiment_analysis:
        Analyse each sentence present in the on_prepositions_sentences class varibale and find out its sentiment.
        the output will be in the form 
        [(sentence, polarity), (sentence, polarity), ...........]


        decorator t_ime
        make a decorator t_ime and implement on every method to calculate the time taken by each class method to
        execute, print time in seconds


        """

        a = Test1(*args, **kwargs)
        print a





