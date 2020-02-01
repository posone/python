#new:
def check_card(number):
    number_ws = number.replace(" ", "")
    print("temp dlugosc: ", len(number_ws))
    print(number_ws)
    if len(number_ws) == 1 or number_ws.isdigit() is False:
        raise Exception("wrong value")
    final = [int(c) for c in number_ws]
    final = [final[i] if i%2==(len(final)+1)%2 else 2*final[i] for i in range(len(final))]
    final2 = [m if m < 10 else m-9 for m in final]

    print (final)
    print (final2)
    if sum(final2)%10 == 0:
        return print("This number is valid!")
    else:
        return print("This number is not valid")

check_card('8273 1232 7352 0569')


def check_card(number):
    number_ws = number.replace(" ", "")
    print("temp dlugosc: ", len(number_ws))
    if len(number_ws) == 1 or number_ws.isdigit() is False:
        raise Exception("wrong value")
    final = []
    for i in range(0, len(number_ws), 2):
        temp = number_ws[i]
        value = 2 * int(number_ws[i])
        if value > 9:
            value = value - 9
        print(temp, value)

        final.insert(i, value)
    for i in range (1, len(number_ws), 2):
        value2 = 1 * int(number_ws[i])
        final.insert(i, value2)
    print (sum(final))
    if sum(final)%10 == 0:
        print("This number is valid!")
    else:
        print("This number is not valid")

check_card('8273 1232 7352 0569')
