#
# Title:   String slicing
# Author: Claudio Asangong
#
# 6.5 Write code using find() and string slicing to extract
# the number at the end of the line below. Convert the extracted value to a
# floating point number and print it out.
#
# Concepts: string method find(), string slicing

text = "X-DSPAM-Confidence:    0.8475"
# find() finds the index of the substring passed
pos = text.find('0')
num = text[pos:]
print(float(num))
