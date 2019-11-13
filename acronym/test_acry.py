def abbreviate(words):
    abb = ""
    w = words.replace('-', ' ').replace('_', ' ').split()
    for i in w:
        abb += i[0].upper()
        #print (abb)
    return print (abb)

#work with Pawel
#work at cap 13.11.19



abbreviate ("TheRoad _Not_ Taken")
