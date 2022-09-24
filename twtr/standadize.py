from nltk.stem import SnowballStemmer
snowball = SnowballStemmer('english')
# Creating a function to perform stemming

def stem(row):
  stem_list = []
  '''This function performs stemming'''
  split_row = row.split()
  for word in split_row:
    stem_list.append(snowball.stem(word))
  return ' '.join(stem_list)