# factorial of a number

num = int(input("Enter a number to find its factorial"))

result = 1
for i in range(1, num + 1):
  result *= i

print("The Factorial of {} is {}".format(str(num), result))
