try:
    i=int(input('Enter the number '))
    if i<0 or i>0:
        print(i,end=' ')
except Exception as e:
    print('Please enter a valid input')
    print(e)
else:
    print('- This is integer')
finally:
    print('Thanks for the Input')