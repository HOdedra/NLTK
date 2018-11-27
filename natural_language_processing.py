import nltk

nltk.download()

#tokenize - grouping things
#word tokenize - separates by words
#sentence tokenize - separates by sentences

#lexicons and corporas
#corporas - body of text, medical journals, presidential speeches, english language
#lexicon - words and their means e.g. investors = 'bull' - someone who is positive about the market

from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello Mr.Smith, how are you doing today? The weather is great and python is awesome. The sky is pinkish-blue. You should not eat cardboard"

print(sent_tokenize(example_text))

print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)
