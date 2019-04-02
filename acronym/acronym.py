def abbreviate(words):
    abb = ""
    w = words.replace('-', ' ').replace('_', ' ').split()
    for i in w:
        abb += i[0].upper()
    return abb




