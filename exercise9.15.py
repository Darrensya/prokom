from random import choice

lottery_pool = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E")


def draw_ticket(pool, size=4):
    ticket = []
    while len(ticket) < size:
        pulled_item = choice(pool)
        if pulled_item not in ticket:
            ticket.append(pulled_item)
    return ticket


my_ticket = [3, 7, "B", "E"]
print(f"Tiket ku: {my_ticket}")

attempts = 0
while True:
    attempts += 1
    winning_ticket = draw_ticket(lottery_pool)

    if sorted(map(str, winning_ticket)) == sorted(map(str, my_ticket)):
        break

print(f"tiket yang menang: {winning_ticket}")
print(f"Ini membutuhkan {attempts:,} kesempatan untuk menang.")