import pandas
import numpy
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def no_punc(row):
  no_punc_list = []
  '''This function is used to remove punctations from the data'''
  for letter in row:
    if letter not in string.punctuation:
      no_punc_list.append(letter)
  return ''.join(no_punc_list)


  