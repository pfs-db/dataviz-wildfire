# Easy:
# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”. For numbers which
# are multiples of both three and five print “FizzBuzz”.


def fuc():
    num_list = range(1, 100)
    for num in num_list:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")


fuc()
