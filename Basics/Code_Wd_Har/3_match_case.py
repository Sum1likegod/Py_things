# just like switch case in c++ here it is match case
case_opt=input('Enter any number ')

match case_opt:
    case 'sstring':
        print('this is string')
    case {34:'hell',2:12}:
        print('this is set')
    case [132,75,77,2,54]:
        print('this is list')
    case (234,'duhh',123.21):
        print('this is tuple')
    case _:
        print('unknown')


user_input = input("Enter the list elements separated by space: ")
list_of_strings = user_input.split()
list_of_integers = [int(i) for i in list_of_strings]

print(list_of_integers)

match list_of_integers:
    case [1, 2, 3]:
        print("This is a list.")
    case _:
        print("This is not a list.")
