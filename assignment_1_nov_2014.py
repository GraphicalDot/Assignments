#!/usr/bin/env python


def Upto_you():
	"""
	Write the most fancier 10 if, else statements, Its upto you
	"""
	pass




def sort_list():
	"""
	1.Prepare a list of all alphabets
	2.Prepare a list by shuffling them and joining them without spaces
	3.From this list which will have 20 elements, prepare a list of dictionaries with key as 1 to 20 and values as the above mentioned randomly
	joined alphabets.
	4.sort this list in descending order according to the value


	Hint: Output is like [{1: 'afmeniyhqvkdxrlocswgjpbtu'}, {2: jdtprombhueifnygskvclwxqa'}, ....so on]
	"""

	pass


def another_sort_list():
	"""
	From the update of sort_list()
	Step2: Update every dictionary present in the list by removing last three elements from each value
	Hint [{1: 'afmeniyhqvkdxrlocswgjp'}, {2: jdtprombhueifnygskvclw'}, ....so on]


	{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 
	'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
	
	Then sum the values according to the above mentioned dictionary
	The above mentioned dictionary is just for your reference, dont copy that and make your own code

	Hint: Output is like [{1: 'afmeniyhqvkdxrlocswgjpbtu', "sum": "282"}, {2: jdtprombhueifnygskvclw', "sum": "283"}, ....so on]
	"""
        

        new_dict = dict()
        #Preparing the list like this   {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7 and so on
        [new_dict.update({element[1]:element[0]})for element in zip(range(1,27), map(chr,range(ord("a"),ord("z")+1)))]



        h = lambda x : sum([new_dict[element] for element in x ])

        
        [element.update({"sum": h(element.values()[0])}) for element in shivam_dict]



        return shivam_dict




def lambda__():
	"""
	should returns a output of a list which will not have prime numbers upto 1000
	"""

	pass



def and_or():
	"""
	returns a list which will not have any number divisible by [18, 19, 21, 99, 45] 
	Original list will have 1, 10000
	"""

	pass


def exception_handling():
	""" 
	Handle exception

	After handling this exception raise your own excpetion which should only print the error messege as the output
	"""
	pass


def open_file(file_path):
	"""
	Print the contents of the file ying on file_path

	Now opena new file in your home directory, Write something in that file and then mv that file into this current directory

	Hint: os or subprocess module
	"""



def convert_string_to_list(string):
	"""
	Convert this string into a list 
	string = "HEY_MAN_WHAT_the_fuck_is_going_on"
	output = ["Hey", "man", "what", "the", "fuck", "is"m "going", "on"]
	
	The convert this list into 
	string = "hey man what the fuck is going on""

	Sonvert this string into
	string = "hey man, everything is great"

	Everything what you have done shall be done in one line with the help of list comprehensions
	"""
	
	
	pass


if  __name__ == "__main__":

	


