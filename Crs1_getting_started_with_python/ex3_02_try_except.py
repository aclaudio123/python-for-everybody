#
# Title:   Using try/except
# Author: Claudio Asangong
#
#
#
# 3.2: Rewrite your pay program (exercise 3.1) using try and except so that the
# program handles non-numeric input gracefully by printing a message and
# exiting the program.
#
# Concepts: try/except, if/else, input, print

# input hours and rate
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
# error checking
try:
    hours = float(hours)
    rate = float(rate)
except Exception e:
    print("Error, please enter numberic input")
    quit()

if hours <= 40:
    pay = hours * rate
else:
    otp = (hours - 40.0) * (rate * 1.5)
    pay = (40.0 * rate) + otp
print("Pay is:", pay)
