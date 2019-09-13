def raindrops(number):
    str_list = ''
    if number % 3 == 0:
        str_list += 'Pling'
    if number % 5 == 0:
        str_list += 'Plang'
    if number % 7 == 0:
        str_list += 'Plong'
    if len(str_list) == 0:
        str_list += str(number)
    return print(str_list)
raindrops(9)

