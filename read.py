'''
--- Read data from data directory
---Data Structure:
    -data
        -BBC News Summary
            -News Articles
                -business
                    -001.txt
                    -002.txt
                    ...
                -politics
                ...
            -Summary
                -business
                    -001.txt
                    -002.txt
                -politics
                ...

'''

import string
import re
import sys
import os
from collections import namedtuple

class Data:
    def __init__(self,path):
        self._path = path


    @property
    def path(self):
        return self._path


    @path.setter
    def path(self,value):
        if not os.path.exists(value):
            raise OSError("directory does not exist")
        else:
            self._path = value


    @staticmethod
    def get_sentences(file_path,filename, delim):
        with open(os.path.join(file_path,filename),'r') as _file:
            lines = _file.readlines()
            lines = ''.join(lines)
            _file.close
        return lines.split(delim)        


    def topics(self):
        master = os.listdir(self.path)
        topics = []
        for _dir in master:
            dir_path = os.path.join(self.path,_dir)
            topics.extend(os.listdir(dir_path))
        return set(topics)


    def data_generator(self, delim,
                        articles_dir = "news_articles", summaries_dir = "summaries",
                        topics = [] ):
        DataObj = namedtuple('DataObj', 'text summary')
        TEXT_PATH = os.path.join(self.path,articles_dir)
        SUMM_PATH = os.path.join(self.path,summaries_dir)
        if topics == []:
            topics = self.topics()
        for topic in topics:
            topic_text_path = os.path.join(TEXT_PATH,topic)
            topic_summ_path = os.path.join(SUMM_PATH,topic)
            file_names = os.listdir(topic_text_path)
            assert sorted(file_names) == sorted(os.listdir(topic_summ_path)), "Check filenames in topic folder: {}".format(topic)
            for f_name in file_names:
                text_lines = self.get_sentences(topic_text_path,f_name,delim)
                summ_lines = self.get_sentences(topic_summ_path, f_name,delim)
                yield DataObj(text_lines,summ_lines)


if __name__ == '__main__':
    PATH = 'C:/Users/Dhruvil/Desktop/Projects/text_summarization/data/BBC News Summary'
    read_data = Data(PATH)
    print(read_data.topics())
    data_gen = read_data.data_generator(delim = '.')
    data_obj = next(data_gen)
    print("\nText: ",data_obj.text)
    print("\n\nSummary: ",data_obj.summary)
        


