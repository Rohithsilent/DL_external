import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# nltk.download("punkt_tab")
nltk.download("stopwords")


text = " this is a program for removing stop words in a sentence"

tokens = word_tokenize(text)

stop_words =  set(stopwords.words('english'))

filtered_words = [word for word in tokens if word.lower() not in stop_words]

print(f"Tokens: {tokens}")
print(f"after removing stop words: {filtered_words}")