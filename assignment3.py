#task1
def factorial(n):
    if n<2:
        return 1
    elif n>=2:
        return int(n)*factorial(n-1)
    

num =int(input("enter a number:"))
print(f"Factorial of {num} is : {factorial(num)}")

#task2
import math
a = int(input("enter a number:"))
print(f"Square root : {math.sqrt(a)}"
      f"Logarithm : {math.log(a)}"
      f"Sine : {math.sin(a)}")