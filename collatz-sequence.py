# Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.
#
# Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)
#
# Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.

# The output of this program could look something like this:
#
#
# Enter number:
# 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1

import sys
def collatz(number):
    if number % 2 == 0:
        return number/2
    return 3 * number + 1

def run():
    print('Enter a non zero positive number')
    input_num = 0
    try:
        input_num = int(input())
        if input_num <= 1:
            print('Invalid Input Entered')
            sys.exit()
        while True:
            input_num = collatz(input_num)
            print(int(input_num))
            if input_num == 1:
                print('You have reached 1.')
                break
    except ValueError:
        print('Invalid Input entered.')

run()
