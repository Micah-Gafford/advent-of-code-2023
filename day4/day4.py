with open(file="input.txt", mode="r", encoding="utf-8") as file:
    f = file.readlines()
    cards = [1 for _ in f]
    p1_sum = 0

    for i, line in enumerate(f):
        winners_str, contenders_str = line.split(":")[1].split("|")
        winners, contenders = winners_str.split(), contenders_str.split()
        matches = len(set(winners) & set(contenders))

        if matches > 0:
            p1_sum += pow(2, matches - 1)

        for j in range(matches):
            cards[i + j + 1] += cards[i]

print(p1_sum, sum(cards))
