a,b,c=input().split(' ')
a = int(a)
b = int(b)
c = int(c)
for i in range(1, c + 1):
    if i % a == 0 and i % b == 0:
        print('FizzBuzz')
    if i % a == 0 and i % b != 0:
        print('Fizz')
    if i % b == 0 and i % a != 0:
        print('Buzz')
    if i % a != 0 and i % b != 0:
        print(i)