from collections import Counter

### Part 1

# Cards: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
# A = Highest, 2 = Lowest
# Types, 5 of a kind, 4 of a kind, full house (3 same, 2 same), 3 of a kind (3 same), 2 pair, 1 pair, high card
# Tie breaker: go through each card and compare indexes
card_scores: dict[str, int] = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


def get_type(hand: tuple) -> int:
    if Counter(hand) == Counter((5,)):
        return 7
    elif Counter(hand) == Counter((4, 1)):
        return 6
    elif Counter(hand) == Counter((3, 2)):
        return 5
    elif Counter(hand) == Counter((3, 1, 1)):
        return 4
    elif Counter(hand) == Counter((2, 2, 1)):
        return 3
    elif Counter(hand) == Counter((2, 1, 1, 1)):
        return 2
    elif Counter(hand) == Counter((1, 1, 1, 1, 1)):
        return 1


def create_hand_tuple(hand: str) -> tuple:
    cards: dict[str, int] = {}
    for card in hand:
        if card not in cards:
            cards[card] = 1
        else:
            cards[card] += 1

    return tuple(cards.values())


def compare(hand1: str, hand2: str):
    hand1_tup, hand2_tup = create_hand_tuple(hand1), create_hand_tuple(hand2)
    hand1_score, hand2_score = get_type(hand1_tup), get_type(hand2_tup)
    hand1_greater = False

    if hand1_score > hand2_score:
        hand1_greater = True
    elif hand1_score == hand2_score:
        for i in range(5):
            if card_scores[hand1[i]] > card_scores[hand2[i]]:
                hand1_greater = True
                break
            elif card_scores[hand1[i]] < card_scores[hand2[i]]:
                break

    return hand1_greater


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # merge the two sorted halves
        while i < len(left) and j < len(right):
            if not compare(left[i][0], right[j][0]):  # check if left is less than right
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def main():
    sum = 0
    with open(file="input.txt", mode="r", encoding="utf-8") as file:
        hands: list[list[str, str]] = [line.split() for line in file.readlines()]

        merge_sort(hands)

        for i in range(len(hands)):
            sum += int(hands[i][1]) * (i + 1)

    print(sum)


if __name__ == "__main__":
    main()
