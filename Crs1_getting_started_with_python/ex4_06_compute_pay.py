#
# Title:   Compute pay
# Author: Claudio Asangong
#
#
# 4.6 Write a program to prompt the user for hours and rate per hour using
# input to compute gross pay. Pay should be the normal rate for hours up to
# 40 and time-and-a-half for the hourly rate for all hours worked above 40
# hours. Put the logic to do the computation of time-and-a-half in a function
# called computepay() and use the function to do the computation. The function
# should return a value. Use 45 hours and a rate of 10.50 per hour to test the
# program (the pay should be 498.75). You should use input to read a string
# and float() to convert the string to a number. Do not worry about error
# checking the user input unless you want to - you can assume the user types
# numbers properly. Do not name your variable sum or use the sum() function.
#
# Concepts: function, try/except, if/else, input, print,


# input hours and rate
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

# convert hour/rate to float and error handling
try:
    hours = float(hours)
    rate = float(rate)
except e:
    print("Error, please enter numberic input")
    quit()


# compute pay logic
def computepay(h, r):
    if h <= 40:
        return h*r
    else:
        ot = (h - 40.0) * (r * 1.5)
        otp = (40.0 * r) + ot
        return otp


# test
p = computepay(hours, rate)
print("Pay", p)
