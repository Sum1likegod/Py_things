vowel_counts = {}

# Iterate over the words in the sentence and count the number of vowels in each word
sentence = "This is a sentence. i want to count more"
for word in sentence.split():
    vowel_count = 0
    for letter in word:
        if letter in ["a", "e", "i", "o", "u"]:
            vowel_count += 1
    vowel_counts[word] = vowel_count
print(vowel_counts)

dict_ex = {'stri': 'this is string in dictionary',
           'tup': ('this', 'is', 'tuple', '504'),
           23: 245}
print(type(dict_ex['stri']))
print(type(dict_ex['tup']))
print(type(dict_ex[23]))

print(dict_ex.get('str'))


dict_ex['ran']=range(12,45)
print(type(dict_ex['ran']))
print(dict_ex.items())      #returns the tuple in pair of keys and values
print(dict_ex.values())     #returns all the values of all the keys

dict_ex.update({23:'hwll'})
dict_ex.update({'rangee':(2,6)})

print(dict_ex)

new=dict(dict_ex)
#dict_ex.clear()
#del dict_ex            #permanentely deletes the entire dictionary
print('this is old one',dict_ex)
print('this is new one',new)