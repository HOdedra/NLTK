#stop words
#stop words. e.g. sarcastic words, words you dont care about. e.g. 'a','the' etc

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stop word filtration."
stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sentence)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)
