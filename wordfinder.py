"""Word Finder: finds random words from a dictionary."""
from operator import truediv
from tokenize import String
import random

class WordFinder:
    """
    >>> wf = WordFinder("/Users/shanli/Desktop/python-oo-practice/words.txt")
    235886 words read    
    """

    def __init__(self,file):
        """make a new wordfinder obj with a path to any file, and list is created from the file's words omitting white space. Prints the number of words in file"""
        self.list_of_words = []
       
        with open(file,"r") as f:
            for line in f:
                #str.strip method removes empty white space before and after word
                self.list_of_words.append(str.strip(line))
        
        print (f"{len(self.list_of_words)} words read")

    def __repr__(self) -> str:
        #printable representation of the obj. %s = file 
        return 'WordFinder(file=%s)' % (self.list_of_words)
    
    def random(self):
        """print a random word from list_of_words list"""
        random_num = random.randint(0,len(self.list_of_words))
        print(self.list_of_words[random_num])


  
class RandomWordFinder(WordFinder):
    """
    >>> wfr = RandomWordFinder("/Users/shanli/Desktop/python-oo-practice/words2.txt")
    ['kale', 'parsnips', 'apple', 'mango']

    >>> wfr.random() in ['kale', 'parsnips', 'apple', 'mango']
    True
    """
    def __init__(self, file):
        
        f = open(file, "r")
        self.list_of_words = [word.strip() for word in f if word.strip() and not word.startswith("#")]

        print (self.list_of_words)


    
