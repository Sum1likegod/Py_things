range_ex =range (2,20,3)
print(range_ex[3])   #8
print(range_ex[-4])
print(range_ex[3:6])
print(range_ex)
element =list(range_ex)
print (element)

print("Using for loops " )
for i in range_ex:
  print(i,end='')


print("delimiter")
for i in range_ex:
  print(f'{i}',end="\t")
print(" ")
for i in range_ex:
  print(f'{i}',end="")
print(" ")
for i in range_ex:
  print(f'{i}',end=",")



print("\n using list ")
Elements=tuple(range_ex)
print(Elements)


print("using enumerate")
for i, value in enumerate(range_ex):
  print(i,value)