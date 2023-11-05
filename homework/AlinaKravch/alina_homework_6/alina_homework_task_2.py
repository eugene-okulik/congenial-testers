# Write a program that tries the sequence from 1 to 100. For numbers divisible by 3 it should write:
# "Fuzz" instead of printing the number, and for numbers divisible by 5 it should print "Buzz".
# For numbers that are multiples of both 3 and 5, it should print "FuzzBuzz". Otherwise, print the number.

for n in range(1, 101):
    if n % 3 == 0:
        print('Fuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif (n % 3 == 0) and (n % 5 == 0):
        print('FuzzBuzz')
    else:
        print(n)
        
