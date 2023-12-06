### Part 1

with open(file="input.txt", mode="r", encoding="utf-8") as file:
    time, distance = [line.split(":")[1].split() for line in file.readlines()]
    num_ways_to_wim = 1

    for i in range(len(time)):
        allotted_time = int(time[i])
        record = int(distance[i])
        race_wins = 0

        for j in range(allotted_time):
            traveled = (allotted_time - j) * j
            if traveled > record:
                race_wins += 1

        if race_wins > 0:
            num_ways_to_wim *= race_wins

print(num_ways_to_wim)

### Part 2
with open(file="input.txt", mode="r", encoding="utf-8") as file:
    time, distance = [line.split(":")[1].split() for line in file.readlines()]
    time, distance = "".join(time), "".join(distance)
    num_ways_to_wim = 0

    allotted_time = int(time)

    for i in range(allotted_time):
        traveled = (allotted_time - i) * i
        if traveled > int(distance):
            num_ways_to_wim += 1

print(num_ways_to_wim)
