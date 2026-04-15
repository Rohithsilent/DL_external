import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

nltk.download("punkt_tab")


text = "hello this is a program. this is used for tokenization"
tokens_sent = sent_tokenize(text)

print("sentence tokenization:",tokens_sent)
tokens = word_tokenize(text)

print("tokens:",tokens)