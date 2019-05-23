#second try!##

lista = {   1: ["first", "a Partridge in a Pear Tree."],
            2: ["second", "two Turtle Doves, and "],
            3: ["third", "three French Hens, "],
            4: ["fourth", "four Calling Birds, "],
            5: ["fifth", "five Gold Rings, "],
            6: ["sixth", "six Geese-a-Laying, "],
            7: ["seventh", "seven Swans-a-Swimming, "],
            8: ["eighth", "eight Maids-a-Milking, "],
            9: ["ninth", "nine Ladies Dancing, "],
            10: ["tenth", "ten Lords-a-Leaping, "],
            11: ["eleventh", "eleven Pipers Piping, "],
            12: ["twelfth", "twelve Drummers Drumming, "]
         }
text = 'On the {} day of Christmas my true love gave to me: {}'
#print (text.format(lista[2][0], ''.join([lista[2][1] for i in range (2, 0, -1)])))

def verse(n):
    return text.format(lista[n][0], ''.join([lista[i][1] for i in range(n, 0, -1)]))

def recite(start_verse, end_verse):
    return (verse(i) for i in range(start_verse, end_verse +1))

verse(4)
#def verse(n):
 #   return intro.format(items[n][0], ''.join([items[i][1] for i in range(n, 0, -1)]))


#first try
#start = 1
#end = 2
#days = ['zero','first ','second ','third ','fourth ','fifth ','sixth ','seventh ','eighth ','ninth ','tenth ','eleventh ','twelfth ']x==
#text = ['zerp','a Partridge in a Pear Tree','two Turtle Doves','three French Hens','four Calling Birds','five Gold Rings','six Geese-a-Laying','seven Swans-a-Swimming','eight Maids-a-Milking','nine Ladies Dancing','ten Lords-a-Leaping','eleven Pipers Piping','twelve Drummers Drumming']
#print ("".join("On the " + days[start] + "day of Christmas my true love gave to me: " + text[end] + text[end - 1]))

#print (text[:-1])
#On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.

#On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.

#On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

#On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

#On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

#On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

# the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

#On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

#On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds,f = three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

#On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

#On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

#On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.