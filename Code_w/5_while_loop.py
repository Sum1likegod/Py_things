# using while loop

num = int(input('Enter a number you want to repeat '))
i = 1
while i <= 10:
    print(i, '. ', num)
    i = i+1
else:
    print('this is else clause no')

while True:
    num = int(input('Enter a Number '))
    if num % 2 == 0 and num != 0:
        continue
    elif num == 0:
        break
    else:
        print(num)
