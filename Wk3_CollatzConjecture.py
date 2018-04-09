# Mark Kelly 2018/02/09 - The Collatz Conjecture

n = int(input("Please enter an integer: "))

while n > 1:
    if n % 2 == 0:
        n = n / 2
     # If the remainder of the n integer divided by 2 is 0 (i.e an even number) , divide n by 2
    else:
        n = (n * 3) +1
     # If the remainder of the n integer divided by 2 is not 0 (i.e an odd number), multiply by 3 and add 1
    print (n)
    # n is printed for each loop in the while statement until n = 0
