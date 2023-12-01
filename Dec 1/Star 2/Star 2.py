"""
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
"""

from enum import IntEnum

class numbers(IntEnum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9

# Handles the values from each line the way 
def get_line_value(input_string: str):
    # Start by separating all the ints into their own string
    index = len(input_string)
    
    buffer = input_string
    for number in numbers:
        temp_index = input_string.find(str(number.name))
        if (temp_index < index) & (temp_index != -1):
            index = temp_index
            buffer = input_string.replace(str(number.name), str(number.value))
    
    input_string = buffer
    index = 0
    temp_index = 0
    for number in numbers:
        try:
            temp_index = input_string.rindex(str(number.name))
        except:
            pass
        if (temp_index > index) & (temp_index != -1):
            index = temp_index
            buffer = input_string.replace(str(number.name), str(number.value))

    value_string = ''.join(filter(str.isdigit, buffer)) #Just learned how to use filter

    # return the fucken values babyyyy
    if len(value_string) == 1:
        return int(value_string) * 11
    return 10*int(value_string[0]) + int(value_string[-1]) # Since strings are just arrays


total = 0
# TODO: Still not too familiar with os.path stuff... Gotta dig into that, this is a temporary solution
with open("C:/Users/ewatchorn/code/aoc23/Dec 1/Star 1/input.txt") as data:
    for line in data:
    # for line in input_stuff:
        data = line.rstrip('\n')

        line_val = get_line_value(data)
        # print(str(line_val) + " for string " + data)
        total += line_val

print("Total is " + str(total))

# 54727 is too low
# 54729 is too high
# Okey