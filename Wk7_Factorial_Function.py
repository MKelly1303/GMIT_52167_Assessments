# Functions Excercise - 08/03/18 - Mark Kelly

n = int(input("Please enter an integer: "))

# defining a function called 'factorial' which will have the integer n passed into it and called num
def factorial(num):
  fact = num
  while num > 1:
    fact = fact*(num - 1)
    num = num -1
    # the variable fact takes on the value of num initially. It is then multiplied by (num-1)
    # the value is added to fact for each loop while the num is reduced by 1. When num reachs 1, the loop finishes
    # and returns the value of fact
  return fact

print(f'The factorial of {n} is: ', factorial(n))


#Export of the answers to 5, 7 and 10 are below

#C:\Users\Mark\Desktop\GMIT\S1\52167 P&S\Wk7>python Wk7_Exercise_Functions.py
#Please enter an integer: 5
#The factorial of 5 is:  120

#C:\Users\Mark\Desktop\GMIT\S1\52167 P&S\Wk7>python Wk7_Exercise_Functions.py
#Please enter an integer: 7
#The factorial of 7 is:  5040

#C:\Users\Mark\Desktop\GMIT\S1\52167 P&S\Wk7>python Wk7_Exercise_Functions.py
#Please enter an integer: 10
#The factorial of 10 is:  3628800

