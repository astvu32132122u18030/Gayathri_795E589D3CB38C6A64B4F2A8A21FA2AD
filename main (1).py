def factorial(n):
  if n == 1 or n==0:
    return 1
  else:
    return n * factorial(n - 1)
n = int(input("Enter a value:"))
res = factorial(n)
print("The Factorial of {}is{}.".format(n,res)) 