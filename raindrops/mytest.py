def print_factors(x):
    l_string = ''
    temp_3 = 'Pling'
    temp_5 = 'Plang'
    temp_7 = 'Plong'
    new_string = ''
    print ("The factor of", x, "are:")
    for i in range(1, x+1):
        if x % i == 0:
            #print(i)
            str1 = str(i)
            l_string += str1
    print (l_string)
    for i in l_string:
        a = ''
        b = ''
        c = ''
        if i == '3':
            a += temp_3

        if i == '5':
            b += temp_5

        if i == '7':
            c += temp_7

        new_string = a + b + c
        print (new_string)
num=30
print_factors(num)





