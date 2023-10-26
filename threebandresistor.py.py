#! /usr/bin/python3

"""
This code is created by Missile-42069
this code is a three band resistor color coding calculator
"""

#define a function that checks the color input and assign them a number corresponds to the band color
def colors(text):
    if text == 'black':
        return 0
    if text == 'brown':
        return 1
    if text == 'red':
        return 2
    if text == 'orange':
        return 3
    if text == 'yellow':
        return 4
    if text == 'green':
        return 5
    if text == 'blue':
        return 6
    if text == 'violet':
        return 7
    if text == 'gray':
        return 8
    if text == 'white':
        return 9


#prompt the user to input the resistor band colors
first_band = input("input the first color band: ").lower()
second_band = input("input the second color band: ").lower()
multiplier_band = input("input the multiplier band: ").lower()

#combine the first band and the second band by converting them into string
concat = f"{colors(first_band)}{colors(second_band)}"

#convert the value of the combined band and multiplying by 10 raised to the number of the multiplier band
result = int(concat) * 10 ** colors(multiplier_band)

#output the result
print(f"The resistor is {result} ohms")