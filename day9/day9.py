with open(file="input.txt", mode="r", encoding="utf-8") as file:
    histories = [line.strip("\n ").split() for line in file.readlines()]
    sum = 0
    sum_p2 = 0
    for history in histories:
        sequences = [[int(num) for num in history]]
        check = history
        while True:
            sequence = []
            for i in range(len(check) - 1):
                sequence.append(int(check[i + 1]) - int(check[i]))

            sequences.append(sequence)
            if set(sequence) == {0}:
                sequence.append(0)
                break
            else:
                check = sequence

        r_seq: list[list[int]] = []
        for seq in reversed(sequences):
            r_seq.append(seq)

        for i, sequence in enumerate(r_seq):
            if i < len(r_seq) - 1:
                r_seq[i + 1].append(r_seq[i + 1][-1] + r_seq[i][-1])
                r_seq[i + 1].insert(0, r_seq[i + 1][0] - r_seq[i][0])

        sum += r_seq[-1][-1]
        sum_p2 += r_seq[-1][0]
print(sum, sum_p2)
