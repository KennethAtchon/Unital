# import nltk
# from nltk.corpus import wordnet
# from nltk.corpus import words

# nltk.download('wordnet')
# nltk.download('words')

# def generate_similar_words(word):
#     similar_words = []
    
#     # Get all English words
#     english_words = set(words.words())
    
#     # Find words with similar phonetics using Levenshtein distance
#     for english_word in english_words:
#         if len(english_word) > 1 and abs(len(word) - len(english_word)) <= 2:
#             distance = nltk.edit_distance(word, english_word)
#             if distance <= 2:
#                 similar_words.append(english_word)
    
#     return similar_words

# # Example usage:
# input_word = "red"
# similar_words = generate_similar_words(input_word)
# print(f"Words similar to '{input_word}': {similar_words}")

import nltk
from nltk.corpus import wordnet
from nltk.corpus import words

nltk.download('wordnet')
nltk.download('words')

def generate_similar_words(words1):
    synonyms = set()

    # Split the input into individual words
    input_words = words1.split(',')

    for input_word in input_words:
        for syn in wordnet.synsets(input_word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name().lower())

    # Filter out the original words and non-English words
    for input_word in input_words:
        synonyms.discard(input_word.lower())

    english_words = set(words.words())  # Fix here, change 'words' to 'word'
    synonyms = list(synonyms.intersection(english_words))

    return synonyms

# Example usage:
input_words = "red,yellow,orange"
similar_words = generate_similar_words(input_words)
print(f"Words similar to '{input_words}': {similar_words}")
