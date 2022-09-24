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

def no_stopwords(row):
  no_stopwords_list = []
  '''This function returns the text column without the stopwords'''
  split_text = row.split()
  for word in split_text:
    if word not in stopwords.words('english'):
      no_stopwords_list.append(word)
  return ' '.join(no_stopwords_list)

  