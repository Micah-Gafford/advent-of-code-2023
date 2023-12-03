### Part 1
import re

input_graph: list[list] = []
input_strs: list[str] = []
indexes: dict[int, list] = {}
pattern = "([0-9]*)"
i = 0
valid_sum = 0
symbols = "+_=@#$%&*/-"
invalid_symbols = "0123456789."

with open(file="input.txt", mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        matches = re.findall(pattern, line)
        indexes[i] = matches
        i += 1
        input_graph.append(list(line))
        input_strs.append(line)

    for i, matches in indexes.items():
        for match in matches:
            if match == "":
                continue

            print(match, i)
            s_i = input_strs[i].find(match)

            """
            467..114..  first check i = i + 1 -- check range = s_i + len(match), second check i = i -- check range = s_i+len(match) -- top left i = 0, s_i = 0
            ...*......  
            ..35..633.
            ......#...
            617*......
            .....+.58.
            ..592.....
            ......755.
            ...$.*....
            .664.598..

            special conditions are i = 0, s_i = 0 | i = 0 | s_i = 0 | i = len(line) - 1, s_i = 0,

                - top left => i = 0, s_i = 0
                - bottom left => i = index.len - 1, s_i = 0
                - top right => i = 0, s_i = 
                - bottom right
                - top
                - bottom
                - right
                - left
                - everything else 
            """

            right_i = s_i + len(match)
            left_i = s_i - 1
            # check left and right
            if (left_i >= 0 and input_strs[i][left_i] not in invalid_symbols) or (
                right_i < len(input_strs[i])
                and input_strs[i][right_i] not in invalid_symbols
            ):
                valid_sum += int(match)
                print("valid: ", valid_sum)
                continue

            # check corners
            top_i = i - 1
            bot_i = i + 1
            if (
                (
                    top_i >= 0
                    and left_i >= 0
                    and input_strs[top_i][left_i] not in invalid_symbols
                )
                or (
                    top_i >= 0
                    and right_i < len(input_strs[top_i])
                    and input_strs[top_i][right_i] not in invalid_symbols
                )
                or (
                    bot_i < len(input_strs)
                    and left_i >= 0
                    and input_strs[bot_i][left_i] not in invalid_symbols
                )
                or (
                    bot_i < len(input_strs)
                    and right_i < len(input_strs[top_i])
                    and input_strs[bot_i][right_i] not in invalid_symbols
                )
            ):
                valid_sum += int(match)
                print("valid: ", valid_sum)
                continue

            # check above if valid
            if top_i >= 0:
                above_str = input_strs[top_i][s_i:right_i]
                set1 = set(above_str)
                set2 = set(symbols)
                common = set1.intersection(set2)
                if len(common) > 0:
                    valid_sum += int(match)
                    print("valid: ", valid_sum)
                    continue

            # check below if valid
            if bot_i < len(input_strs):
                bot_str = input_strs[bot_i][s_i:right_i]
                set1 = set(bot_str)
                set2 = set(symbols)
                common = set1.intersection(set2)
                if len(common) > 0:
                    valid_sum += int(match)
                    print("valid: ", valid_sum)
                    continue

print(valid_sum)
