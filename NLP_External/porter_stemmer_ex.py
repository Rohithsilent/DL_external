import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


# nltk.download("punkt_tab")

ps = PorterStemmer()

text = "running easily healthy gone"

tokens = word_tokenize(text)

stemmed_words = [ps.stem(word) for word in tokens]

print(f"tokens: {tokens}")
print(f"stemmed words: {stemmed_words}")