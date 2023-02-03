cards_sequence = input().split()

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

terminate_message = "Game was terminated"

for card in cards_sequence:
    card_info = card.split("-")
    team = card_info[0]
    player = int(card_info[1])

    if len(team_a) < 7:
        break
    elif len(team_b) < 7:
        break

    if team == "A":
        if player in team_a:
            team_a.remove(player)
    elif team == "B":
        if player in team_b:
            team_b.remove(player)

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if len(team_a) < 7 or len(team_b) < 7:
    print(terminate_message)
