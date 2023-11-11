for num in range(0,9,2):
  print(num)
else:
  print("this is the end ")

my_life="Total shitt ."
for letters in  my_life:
  print (letters,end="*")




print("\n\n")
#printing even numbers from 1 to 20

print("The Even Numbers Between 0 to 20 are ")
for even_num in range(0,21):
  if even_num%2==0:
    print(even_num,end=' ')
else:
  print("\nThat's how Numbers are Print ")



print("\n\n")
  #using list to print numbers
strt=2
final=[]

print ("Using a list we can do this ")
while strt<=20:
  if strt%2==0:
    final.append(strt)
  strt+=1

print("Using a List\n",final)



print("\n\n")
#squares of the number from 1 to 10 

first=1
squ=[]

for i in range(1,11):
  squ.append(i**2)

print(f"Squares are {squ} ")


print("\n\n")
#printing fibonnaci series

fst=0
sec=1

for i in range(1,9):
  if i==1:
    print(f"Fibonacci Series upto 10th No. {fst} {sec} ",end='')
  thd=fst+sec
  print(thd,end=' ')
  fst, sec,thd=sec, thd, fst

print("\n\n")
    #printing series using ai logic
a,b=0,1
print("this is using ai")
for i in range(10):
  print(a,end=' ')
  a,b=b,a+b