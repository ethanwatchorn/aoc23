"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""

example_data = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

data = []
with open("C:/Users/ewatchorn/code/aoc23/Dec 3/input.txt") as file:
    for line in file:
        data.append(line)

# x_len = len(example_data[0])
# y_len = len(example_data)
x_len = len(data[0])
y_len = len(data)

def is_symbol(input_str: str) -> bool:
    if (not input_str.isdigit()) and (input_str != "."):
        return True
    return False

def get_full_num(line: str, index: int):
    # Should also return the modified string with the number fully removed
    number = 0
    new_line = line
    # search for first index of number
    search_ind = index
    while (search_ind >= 0) and (line[search_ind].isdigit()):
        search_ind -= 1
    search_ind += 1
    first_ind = search_ind
    search_ind = index
    while (search_ind < len(line)) and (line[search_ind].isdigit()):
        search_ind += 1
    search_ind -= 1

    length = (search_ind + 1) - first_ind
    replace_str = ""
    for i in range(length):
        replace_str = replace_str + "."

    # print(replace_str)

    # print(f"first: {first_ind}, last: {search_ind}")
    # print(line[first_ind: search_ind + 1])
    number = int(line[first_ind : search_ind+1]) #???
    new_line = new_line[:first_ind] + replace_str + new_line[search_ind+1:]
    # print(f"{new_line[:first_ind]} + {replace_str} + {new_line[search_ind+1:]}")
    # print(f"{number} extracted from {line}, returning {new_line}")

    return new_line, number

total = 0

for x in range(x_len):
    for y in range(y_len):
        # if is_symbol(example_data[y][x]):
        #     print(f"{example_data[y][x]} is at ({x}, {y})")
        if is_symbol(data[y][x]):

            x_limits = [x-1, x+1]
            y_limits = [y-1, y+1]

            if x_limits[0] < 0:
                x_limits[0] = 0
            if y_limits[0] < 0:
                y_limits[0] = 0
            if x_limits[1] >= x_len:
                x_limits[1] = x_len-1
            if y_limits[1] >= y_len:
                y_limits[1] = y_len-1

            # Get adjacent
            for x_search in range(x_limits[0], x_limits[1]+1):
                for y_search in range(y_limits[0], y_limits[1]+1):
                    if data[y_search][x_search].isdigit():
                        # print(f"adjacent number: {example_data[y_search][x_search]}")
                        # example_data[y_search], number = get_full_num(example_data[y_search], x_search)
                        data[y_search], number = get_full_num(data[y_search], x_search)
                        # print(f"{data[y_search]}  -  {number}")
                        total += number
                        
print(total)

# 549607 too high