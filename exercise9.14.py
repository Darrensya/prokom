from random import choice

lottery_pool = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E")

winning_ticket = []
while len(winning_ticket) < 4:
    pulled_item = choice(lottery_pool)
    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)

print("Pemenangnya ialah siapapun yang mendapatkan karakter:")
print(winning_ticket)