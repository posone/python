class Luhn:
    def __init__(self, number):
        self.number = number

    def valid(self):
        number_ws = self.number.replace(" ", "")
        #print("temp dlugosc: ", len(number_ws))
        if len(number_ws) == 1 or number_ws.isdigit() is False:
            #raise Exception("wrong value")
            return False
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

