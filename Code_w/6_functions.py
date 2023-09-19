def first_func(num_f):
    print('this is to illustrate functions in python')
    print('Here is the number ', num_f)


num = int(input('enter a number to be print through the funtion '))
first_func(num)

name = input('Enter a string ')
print('This is the inputted string ' + name)


def mood(name_2, cur_mood, time):
    print(f'Hi,\nI am {name_2} and my current mood is {cur_mood} at the time {time}')


mood('Rohit', 'Learning', '12:30')


def ret_func(var):
    return var**3


no = int(input('Enter a Number you want the cube of '))
print('The cube of', no, 'is', ret_func(no), end=' ')
print(f'The Cube of {no} is {ret_func(no)}')


def addition(num_1, num_2):
    return num_1 + num_2


a = int(input('Enter a Number '))
b = int(input('Enter a Second Number '))
print(f'The Addition of {a} and {b} is {addition(a,b)}')

print('The addition of the numbers are', addition(int(input('Enter a number ')), int(input('Enter a Second Num '))))
