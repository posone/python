def is_isogram(string):
    #todobyPawel
    string = string.lower().replace(' ', '').replace('-', '')
    print(len(set(string)))
    print(len(string))
    if len(set(string)) == len(string):
        return True
    else:
        return False
    pass
