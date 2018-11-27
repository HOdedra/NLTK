#stemming
#root stem of the word. e.g. stem of writing is write. riding --> ride
#why stem? different variations of word based on stem. but meaning of word is unchanged. 
#i was taking a ride in the car
#i was riding in the car
#both mean the same thing

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

for w in example_words:
    print(ps.stem(w))

new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned have pythoned poorly at least once."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))