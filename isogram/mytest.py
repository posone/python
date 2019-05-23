string_a = 'ds'
print (len(set(string_a)))
print (len(string_a))
if len(set(string_a)) == len(string_a):
    print(string_a)
else:
    print("It's not! isogram")