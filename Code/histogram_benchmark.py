import timeit

def make_histogram(words):
    hgram = []                      #Create new list
    for word in words:              #For each word
        index = find(word, hgram)   #check if word in hgram
        if index == None:           #if not in hgram
            hgram.append((word, 1)) #add with count of 1
        else:                       #if word in hgram
            count = hgram[index][1] #find its current count
            new_pair = (word, count + 1) #make a new pair add one to the current count
            hgram[index] = new_pair #replace word-count pair
    return hgram                    #return the hgram

def find(item, hgram):
    for index, pair in enumerate(hgram):
        if pair[0] == item:
            return index
    return None

def list_of_words(length):
    dict_words = '/usr/share/dict/words'
    words_str = open(dict_words, 'r').read()
    all_words = words_str.split('\n')
    return all_words[0:length]

def count(word, hgram):
    index = find(word, hgram)
    if index:
        word_count_pair = hgram[index]
        return word_count_pair[1]
    else:
        return 0

if __name__ == "__main__":
    hundred_words       = list_of_words(100)
    ten_thousand_words  = list_of_words(10000)

    hundred_hgram       = make_histogram(hundred_words)
    ten_thousand_hgram  = make_histogram(ten_thousand_words)
    hundred_search      = hundred_words[-1]
    ten_thousand_search = ten_thousand_words[-1]
    stmt  = "count('{}', ten_thousand_hgram)".format(ten_thousand_search)
    setup = "from __main__ import count, ten_thousand_hgram"
    timer = timeit.Timer(stmt, setup=setup)
    iterations = 10000
    result = timer.timeit(number=iterations)
    print("count time for 100-word histogram: " + str(result))