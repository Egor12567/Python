list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
half_of_list  = len(list_players) // 2

first_team = list_players[:half_of_list]
second_team = list_players[half_of_list:]

print(first_team)
print(second_team)
