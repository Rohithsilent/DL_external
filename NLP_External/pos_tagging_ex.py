import nltk
from nltk import pos_tag

# Download required data (run once)
nltk.download('averaged_perceptron_tagger_eng')

# Sample list of words
words = ["Rohith", "is", "learning", "Python", "and", "building", "AI", "projects", "very", "efficiently"]

# Perform POS tagging
pos_tags = pos_tag(words)

# Print result
print("POS Tags:")
for word, tag in pos_tags:
    print(word, "->", tag) 