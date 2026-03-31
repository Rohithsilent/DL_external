import nltk

nltk.download('punkt_tab')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "natural language processing is a branch in artificial intelligence"

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))

filtered_words =[word for word in words if word.lower() not in stop_words]

print(words)

print("AFter removing stopwords:")
print(filtered_words)