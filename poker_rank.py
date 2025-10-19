def poker_rank(cards):
    poker_ranks = {
        1: 'Royal Flush',
        2: 'Straight Flush',
        3: 'Four of a Kind',
        4: 'Full House',
        5: 'Flush',
        6: 'Straight',
        7: 'Three of a Kind',
        8: 'Two Pair',
        9: 'One Pair',
        10: 'High card'
    }
    num_cards = []
    suits = []
    possible_ranks = []

    for card in cards:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[:2]
            suit = card[2]
        if rank == "J":
            rank = 11
        elif rank == "Q":
            rank = 12
        elif rank == "K":
            rank = 13
        elif rank == "A":
            rank = 14
        num_cards.append(int(rank))
        suits.append(suit)

    sorted_num_cards, sorted_suits = zip(*sorted(zip(num_cards, suits), key= lambda x: x[0], reverse=True))
    #sort num cards descend and sort suits based on sorted_num_cards

    #flush, royal flush and straight flush
    if any(suits.count(suit) == 5 for suit in suits): #5  same suits in poker is flush
        if check_royal_flush(num_cards, suits):
            possible_ranks.append(1)
        if check_straight_flush(num_cards, suits):
            possible_ranks.append(2)
        else:
            possible_ranks.append(5)

    #straight (5 consecutive card_numbers)
    if check_straight(sorted_num_cards):
        possible_ranks.append(6)

    unique_num_cards = list(set(sorted_num_cards))

    # four of the kind -> unique num can be 4,3,2 (4/7)
    # full house -> unique num can be 4, 3 (/7)
    # three of the kind -> unique num can be 5 (/7)
    # two pairs -> unique can be 5, 4 (/7)
    # one pairs -> unique can be 6 (/7)
    if len(unique_num_cards) == 6:
        # 2 pairs : 2H 2D 9C 3H 7S QC AS => 2,9,3,7,12,14
        possible_ranks.append(9)

    if len(unique_num_cards) == 5:
        for num_card in sorted_num_cards:
            # three of the kind : 2H 2D 2C 9H 7S QC AS => 2,9,7,12,14
            if sorted_num_cards.count(num_card) == 3:
                possible_ranks.append(7)
            # 2 pairs : 2H 2D 9C 9H 7S QC AS => 2,9,7,12,14
            if sorted_num_cards.count(num_card) == 2:
                possible_ranks.append(8)

    if len(unique_num_cards) == 4:
        for num_card in sorted_num_cards:
            # four of the kind : 2H 2D 2C 9H 2S QC AS => 2,9,12,14
            if sorted_num_cards.count(num_card) == 4:
                possible_ranks.append(3)
            # full house: 2H 2D 2C 9H 9S QC AS => 2,9,12,14
            if sorted_num_cards.count(num_card) == 3:
                possible_ranks.append(4)
            # 2 pairs : 2H 2D 9C 9H 7S 7C AS => 2,9,7,14
            if sorted_num_cards.count(num_card) == 2:
                possible_ranks.append(8)

    if len(unique_num_cards) == 3:
        for num_card in sorted_num_cards:
            # four of the kind : 2H 2D 2C QH 2S QC AS => 2,12,14
            if sorted_num_cards.count(num_card) == 4:
                possible_ranks.append(3)
            # full house: 2H 2D 2C 9H 9S 9C AS => 2,9,14
            if sorted_num_cards.count(num_card) == 3:
                possible_ranks.append(4)

    if len(unique_num_cards) == 2:
        # four of the kind : 2H 2D 2C QH 2S QC QS => 2,12
        possible_ranks.append(3)

    if not possible_ranks:
        possible_ranks.append(10)

    result = poker_ranks[min(possible_ranks)]
    print(cards, result)
    return result


def check_royal_flush(num_cards, suits):
    suit_dict = {}
    for num, suit in zip(num_cards, suits):
        suit_dict.setdefault(suit, []).append(num)

    for suit, nums in suit_dict.items():
        if len(nums) >= 5:
            sort_nums = sorted(set(nums), reverse= True)
            if all(num in sort_nums for num in [14,13,12,11,10]):
                return True
    return False

def check_straight_flush(num_cards, suits):
    suit_dict = {}
    for num, suit in zip(num_cards, suits):
        suit_dict.setdefault(suit, []).append(num)

    for suit, nums in suit_dict.items():
        if check_straight(nums):
            return True
    return False

def check_straight(num_cards):
    sorted_num_cards = sorted(set(num_cards))
    if 14 in num_cards:
        sorted_num_cards.append(1)

    sorted_num_cards = sorted(sorted_num_cards)
    count = 1
    for i in range(len(sorted_num_cards) - 1):
        if sorted_num_cards[i + 1] ==  sorted_num_cards[i] + 1:
            count += 1
            if count >= 5:
                return True
        else:
            count = 1
    return False

if __name__ == '__main__':
    cards = ['AH', '10H', '3D', '6C', 'JH', 'QH', 'KH']
    cards2 = ['AC', '10H', '3D', '6H', 'JH', 'QH', 'KH']
    cards3 = ['AC', '2H', '3D', '4H', '5H', 'QS', 'KS']
    cards4 = ['2H', '2D', '2C', 'QH', '2S', 'QC', 'QS']
    poker_rank(cards)
    poker_rank(cards2)
    poker_rank(cards3)
    poker_rank(cards4)