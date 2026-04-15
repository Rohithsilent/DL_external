import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("omw-1.4")

lemmatizer = WordNetLemmatizer()

text = "The children are playing with the leaves and went to better schools."

tokens = word_tokenize(text)

lemmatized_word = [lemmatizer.lemmatize(word) for word in tokens]

print(f"lemmatized words: {lemmatized_word}")


