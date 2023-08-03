list_items=[2,5,20,7]
print(f'{list_items}',end=' ')
print(list_items)



new_list=list(range(2,11))
print(new_list)
for i in new_list:
  print(i)


print(list_items[3])


print()

print(list_items[1:3])

print()

#use of append function
list_items.append(-1)
print(list_items)

print()

list_3=[]
list_3.append(4)
list_3.append(8)
list_3.append(21)
print(list_3,end='\n\n')


#use of insert function

list_4=[]
list_4.insert(0,23)
list_4.insert(1,78)
list_4.insert(2,92)
list_4.insert(3,2)
print("list 4 is ",list_4)


print()

list_items.insert(3,100)
print(list_items,end='\n\n')


#use of remove function
#list_4.remove(92)
#print("list 4 after removing 92",list_4,end='\n\n')


#pop function
list_2=list_items.pop(3)
print("1st list after popping is ",list_items)
print("Popped Element is ",list_2)     #pop has removed and returned the value in list_2
item_1=list_4.pop(2)
print(list_4)
print(item_1,end='\n\n')


#using len() function 
length=len(list_items)
print("length of list 1 is ",length)


list_6=['hello','how','r','u']
print(len(list_6))