# using for loop to iterate over a dictionary

ram = {'a': 'she is a good girl',
        'age': 20, 'likes': ['film', 34, 'me']}

for her_likes in ram.values():
    print(her_likes)

for things, her_like in ram.items():
    print(f'{things}  :  {her_like}', end=' ----- ')

