
def reverse_words(sentence):       # sentence here is an array of characters
  words = sentence.split(' ') 
  newsentence =' '.join(reversed(words))
  return newsentence
