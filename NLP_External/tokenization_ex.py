import nltk

nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize, sent_tokenize

text = "natural language processing is a branch in artificial intelligence"

sentences = sent_tokenize(text)
print("sentences tokenization:")

print(sentences)

words = word_tokenize(text)
print("Word tokenization")
print(words)


