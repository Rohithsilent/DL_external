import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

# nltk.download('punkt_tab')

text = "machine learning is a branch of artificial intelligence"

tokens = word_tokenize(text)

n =2

n_grams_list = list(ngrams(tokens,n))

print(f"{n}-grams:")
for gram in n_grams_list:
    print(gram)