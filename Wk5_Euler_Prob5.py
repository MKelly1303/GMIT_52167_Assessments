# Mark Kelly - 20/02/2018 - Project Euler - Problem 5
# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the  
# numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

sum = int
# sum is an integer that will be used to add the modulos remainders together

i = 0
# i is being defined as an integer. It will be used to step through all values from 1 to 20

x = 1
# x is the integer that will be tested to see if it is divisible by all numbers in the range. It is stepped by + 1 for each iteration of the while loop. Starting at 1 as everything modulo 0 returns 0.

while sum != 0:
  sum = 0 # Setting the sum int to 0 at the start of each loop
  for i in range(1,21): # Steps through each value in the range
    sum = sum + (x % i)
    # sum will add up all the remainders. If sum is still equal to 0 at the end, the loop will finish
  x = x + 1 
  #increases the value of x for each iteration of the while loop
print("The smallest positive number that is evenly divible by all of the numbers from 1 to 20 is ", x-1)

# x-1 to remove the addition of 1 in the loop when the solution is achieved. Please note that this code takes 10 mins to run on my machine. The first number that is divisible by all numnbers from 1 to 20 is 232792560.