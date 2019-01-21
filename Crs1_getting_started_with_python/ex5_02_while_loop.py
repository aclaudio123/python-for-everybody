#
# Title:   Loops and Iteration
# Author: Claudio Asangong
#
#
# 5.2 Write a program that repeatedly prompts a user for integer numbers until
# the user enters 'done'. Once 'done' is entered, print out the largest and
# smallest of the numbers. If the user enters anything other than a valid
# number catch it with a try/except and put out an appropriate message and
# ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
#
# Desired Output:
# =-=-=-=-=-=-=-=
# Invalid input
# Maximum is 10
# Minimum is 2
#
# Concepts: While loop; break/continue

smallest = None
largest = None

while True:
    sValue = input("Enter a number: ")
    try:
        fValue = float(sValue)
        if smallest is None:
            smallest = fValue
            largest = smallest
            continue
        elif fValue < smallest:
            smallest = fValue
        elif fValue > largest:
            largest = fValue
        elif fValue == 'done':
            break
    except Exception e:
        if sValue != 'done':
            print('Invalid input')
            continue
        else:
            break
print("Maximum is", int(largest))
print("Minimum is", int(smallest))
