def  factorial(n):
      if n < 2:
          return 1
      else:
          return n * factorial(n-1)
    
num = int(input("Enter a number: "))
print (" Factorial of {} is: {}".format(num,factorial(num)))

-- Output --
Enter a number: 5
Factorial of 5 is: 120

