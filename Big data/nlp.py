# -*- coding: utf-8 -*-
"""NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C1DWUz23VBaxI9pSxcB0XNRbxa4gJQ6Y
"""

import reprlib
import re
import nltk
from nltk import bigrams

RE_WORD = re.compile('\w+')

class Sentence :
    def __init__(self,text):
      self.text = text
      self.words = RE_WORD.findall(text)
      self.index = 0

    def __repr__(self):
      return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
      return Word(self.words)

    def get_next_bigrams(self):
      Bigrams = bigrams(self.text)
      return Bigrams

class Word :
    def __init__(self,words):
      self.words = words
      self.index = 0

    def __next__(self):
      try:
       word = self.words[self.index]
      except IndexError:
        raise StopIteration()
      self.index +=1
      return word

    def __iter__(self):
      return self