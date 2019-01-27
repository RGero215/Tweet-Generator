import random
from collections import Counter
import re

# Define function that takes a number of words and output a sentence with those words
def histogram(file_name):
    #.1 Open and read file words 
    file_object = open(file_name, "r", encoding="utf-8-sig")
    #.2 Words without punctuations
    no_punctuation_file = file_object.read()
    no_punctuation_file = re.sub(r'[^\w\s]','',no_punctuation_file)
    #.3 Storage word count
    word_count = Counter(no_punctuation_file.split())
    #.3 Return word_count
    return word_count


# Define function that takes and histogram and return a unique word's count
def unique_words(histogram):
    #.1 Empty list to count the len
    number_of_unique_words = []
    #.2 Itinirate the dictionary
    for key, value in histogram.items():
        #.3 Words with value 1 or unique words
        if value == 1:
            #.4 Append unique words to the list
            number_of_unique_words.append(key)
    #.5 Return unique word's count
    print("Unique Words", len(number_of_unique_words))
    return len(number_of_unique_words)
    

# Define a function that takes a word and an histogram and return the frequency of the word
def frequency(word, histogram):
    #.1 Itinirate the dictionary
    for key, value in histogram.items():
        #.2 compare the word input to key
        if key == word:
            #.3 return the value or the frequency total
            print(value)
            return value
        else:
            #.4 return a message if the word is not in the histogram
            print("The word: {} is excluded in this histogram".format(word))
            return "The word: {} is excluded in this histogram".format(word)







if __name__ == "__main__":
    frequency("Melaza", histogram("Frankenstein.txt"))