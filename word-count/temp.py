from re import sub

def word_count(phrase):
    words = [word for word in sub(r'[^a-z0-9\']', ' ', phrase.lower()).split()]
    #c = words.count(word)

    print ({word: words.count(word) for word in words})


word_count("31231dada:DAdas//\n\d d:ADA:D q qwewadd")