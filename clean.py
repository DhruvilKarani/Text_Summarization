'''
--- Basic Text Cleaning
    -remove non-ASCII chars
    -Remove punct
    -Lower Case
    -Remove Stopwords
    -Remove whitespaces like '\n'

'''

import os
import sys
import re
import string
import nltk
from collections import namedtuple
from nltk.corpus import stopwords
stopwords_list = stopwords.words('english')

def basic_cleaning(text_list, remove_stopwords):
    if not isinstance(text_list, list):
        raise TypeError("text_list should be a list of text not {0}".format(type(text_list)))
    if not isinstance(remove_stopwords, bool):
        raise TypeError("remove_stopwords should be a bool not {0}".format(type(remove_stopwords)))
    text = ' '.join(text_list)
    text = text.lower()
    text = text.replace("\n"," ")
    text = ''.join([char for char in text if ord(char)<128])
    text = text.translate(str.maketrans('', '', string.punctuation))
    if remove_stopwords:
        tokens = text.split()
        text = ' '.join([token for token in tokens if token not in stopwords_list])
    return text



if __name__ == '__main__':
    import read
    from read import Data
    PATH = 'C:/Users/Dhruvil/Desktop/Projects/text_summarization/data/BBC News Summary'
    DataObj = namedtuple('DataObj', 'text summary')
    read_data = Data(PATH)
    print(read_data.topics())
    data_gen = read_data.data_generator(delim = '.')
    data_obj = next(data_gen)
    print(basic_cleaning(data_obj.text,True))
    print(basic_cleaning(data_obj.summary,True))