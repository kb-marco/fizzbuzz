# Write a Python program which iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"

raw_a = input("beginning number")
raw_b = input("ending number")

a = int(raw_a)
b = int(raw_b)

for x in range(a, b):
    if x % 3 == 0 and x % 5 == 0:
        print ("fizzbuzz")
        continue
    elif x % 3 == 0: 
        print ("fizz")
        continue
    elif x % 5 == 0:
        print ("buzz")
        continue
