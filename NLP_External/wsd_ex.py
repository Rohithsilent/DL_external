import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

nltk.download("punkt_tab")
nltk.download("wordnet")

text = "He went to bank to deposit money"

word = "bank"

tokens = word_tokenize(text)

sense = lesk(tokens,word)

print("disambiguation sense:",sense)
print("meaning",sense.definition())