"""
--- Part Two ---
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""

example_game = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]

def split_index(line: str):
    """
    :param line: String formatted as "Game n: <tests>"
    :return: n, "<tests>"
    """
    buffer = line.split(": ")

    value_string = ''.join(filter(str.isdigit, buffer[0]))
    
    return int(value_string), buffer[1]

def get_cube_count(test: str) -> dict:
    """
    Looks over test, returns amount of each cube type as a dict
    :param test: Formatted as "x red, y green, z blue", does not need to be in that order or have all three colours
    :return: {red: x, green: y, blue: z}
    """
    return_dict = {
        "red": 0,
        "green": 0,
        "blue": 0
        }

    colour_strings = test.split(", ")
    for colour in colour_strings:
        if "red" in colour:
            value_string = ''.join(filter(str.isdigit, colour)) #Just learned how to use filter
            return_dict["red"] = int(value_string)
        if "green" in colour:
            value_string = ''.join(filter(str.isdigit, colour)) #Just learned how to use filter
            return_dict["green"] = int(value_string)
        if "blue" in colour:
            value_string = ''.join(filter(str.isdigit, colour)) #Just learned how to use filter
            return_dict["blue"] = int(value_string)
    
    return return_dict

total = 0

with open("C:/Users/ewatchorn/code/aoc23/Dec 2/input.txt") as data:
    for line in data:
# for line in example_game:
        current_index, tests = split_index(line)
        max_cubes = [0, 0, 0] #RGB

        for test in tests.split("; "):
            cubes = get_cube_count(test)
            if cubes["red"] > max_cubes[0]:
                max_cubes[0] = cubes["red"]
            if cubes["green"] > max_cubes[1]:
                max_cubes[1] = cubes["green"]
            if cubes["blue"] > max_cubes[2]:
                max_cubes[2] = cubes["blue"]
        print(f"Red: {max_cubes[0]}, Green: {max_cubes[1]}, Blue: {max_cubes[2]}")
        
        total += max_cubes[0] * max_cubes[1] * max_cubes[2]

print(f"Total is {total}")