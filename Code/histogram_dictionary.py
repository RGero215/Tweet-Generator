import random
import re



def histogram(file_name):
    #.0 Declear an empty dictionary
    words = {}
    #.1 Open on read mode  
    file_object = open(file_name, "r", encoding="utf-8-sig")
    #.2 Assigned file read to a variable
    no_punctuation_file = file_object.read()
    #.3 Use regular expresion to remove puntuation
    no_punctuation_file = re.sub(r'[^\w\s]','',no_punctuation_file)
    #.4 Storage an array of words without puntuations
    word_count = no_punctuation_file.split()
    #.5 Itinirate the array of words
    for word in range(len(word_count)):
        #.6 if the word is in the list
        if word_count[word] in words:
            #.7 Increase the value by 1
            words[word_count[word]] += 1
        else:
            #.8 If not incluede the word as key an 1 as initial value
            words.update({word_count[word]: 1})
    # print(words)
    #.9 Return words dictionary
    return words
    


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
        
    #.4 return a message if the word is not in the histogram
    print("The word: {} is excluded in this histogram".format(word))
    return "The word: {} is excluded in this histogram".format(word)

# Define function that takes a histogram and output a random word not taking under account the distributions of the words
def random_word(histogram):
    #.0 Empty string to store the word
    word = random.choice(list(histogram.keys()))
    #.1 Ouput the sentence
    print(word)
    return word

# Define a weighted random function 
def weighted_random(histogram):
    my_list = []
    #.1 Itinirate the dictionary
    for key, value in histogram.items():
        my_list += [key] * value
    #.2 select a weighted random choice
    weighted_random_choice = random.choice(my_list)
    print(weighted_random_choice)
    #.3 return weighted random choice
    return weighted_random_choice








if __name__ == "__main__":
    # histogram("Frankenstein.txt")
    # unique_words(histogram("Frankenstein.txt"))
    frequency("the", histogram("Frankenstein.txt"))
    # random_word(histogram("Frankenstein.txt"))
    weighted_random(histogram("Frankenstein.txt")) 
    
