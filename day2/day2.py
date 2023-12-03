import re

### Part 1

index_pattern = "Game ([0-9]*):"
color_patterns = "([0-9]*) red|([0-9]*) green|([0-9]*) blue"
possible_sum = 0
with open("input.txt", "r") as file:
    for line in file.readlines():
        valid = True
        match = re.search(index_pattern, line)
        index = int(match.group(1))

        matches: list = re.findall(color_patterns, line)

        for match in matches:
            if match[0] != "" and int(match[0]) > 12:
                valid = False
                break

            if match[1] != "" and int(match[1]) > 13:
                valid = False
                break

            if match[2] != "" and int(match[2]) > 14:
                valid = False
                break

        if valid:
            possible_sum += index

print(possible_sum)


### Part 2

color_patterns = "([0-9]*) red|([0-9]*) green|([0-9]*) blue"
power_sum = 0
with open("input.txt", "r") as file:
    for line in file.readlines():
        lowest_nums = {"red": -1, "green": -1, "blue": -1}

        matches: list = re.findall(color_patterns, line)

        for match in matches:
            if match[0] != "" and int(match[0]) > lowest_nums["red"]:
                lowest_nums["red"] = int(match[0])

            if match[1] != "" and int(match[1]) > lowest_nums["green"]:
                lowest_nums["green"] = int(match[1])

            if match[2] != "" and int(match[2]) > lowest_nums["blue"]:
                lowest_nums["blue"] = int(match[2])

        power = 1
        for num in lowest_nums.values():
            if num != -1:
                power = power * num

        power_sum += power


print(power_sum)
