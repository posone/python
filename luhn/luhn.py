class Luhn:

    def valid(self, number):
        number_ws = number.replace(" ", "")
        #print("temp dlugosc: ", len(number_ws))
        if len(number_ws) == 1 or number_ws.isdigit() is False:
            raise Exception("wrong value")
        final = []
        for i in range(0, len(number_ws), 2):
            temp = number_ws[i]
            value = 2 * int(number_ws[i])
            if value > 9:
                value = value - 9
            #print(temp, value)

            final.insert(i, value)
        for i in range (1, len(number_ws), 2):
            value2 = 1 * int(number_ws[i])
            final.insert(i, value2)
        #print (sum(final))
        if sum(final)%10 == 0:
            return True
        else:
            return False

