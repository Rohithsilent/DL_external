import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt_tab")
nltk.download("stopwords")

text = "Natural Language Processing is fun and learning NLP is very useful and interesting."

tokens = word_tokenize(text)

tokens = [word.lower() for word in tokens]


stop_words = set(stopwords.words('english'))

filtered_words = [word for word in tokens if word not in stop_words]


print("tokens: ",tokens)
print("filtered words:",filtered_words)
