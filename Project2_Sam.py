levels = [1, 2, 3, 4, 5]
coins = [5, 8, 3, 10, 7]
enemies = [2, 4, 1, 5, 3]
power_ups = ["Mushroom", "Star", "Flower", "Mushroom", "Star"]
print("===== LEVEL DETAILS =====")
for i in range(0, len(levels)):
    print(f"Level {levels[i]}:\n Coins available = {coins[i]}\n Enemies = {enemies[i]}\n Power-Up = {power_ups[i]}")
player_name = "Hero"
lives = 3
score = 0
total_coins = 0
print(f"===== PLAYER INFORMATION =====\n"
      f"Player Name: {player_name}\n"
      f"Lives: {lives}\n"
      f"Score: {score}\n"
      f"Total Coins: {total_coins}\n")
level_scores = []
print("===== LEVEL DETAILS =====")
for i in range(0, len(levels)):
    coin_points = coins[i] * 10
    enemy_points = enemies[i] * (-5)
    powerup_points = 25 if power_ups[i] == "Star" else 0
    current_level_score = coin_points + enemy_points + powerup_points

    level_scores.append(current_level_score)

    print(f"Level {levels[i]} Score: {current_level_score}")
print()
action_results = []
actions = [0, 1, 0, 2, 1]
print("===== ADVENTURE ACTIONS =====")
for i in range(0, len(levels)):
    action_code = actions[i]

    if action_code == 0:
        action_text = "Collect Coins"
    elif action_code == 1:
        action_text = "Fight Enemies"
    elif action_code == 2:
        action_text = "Power-Up"
    action_results.append(action_text)
    print(f"Level {levels[i]} Action: {action_text}")
print()
life_history = []
current_lives = lives

print("===== LIVES REMAINING PER LEVEL =====")
for i in range(len(levels)):
    if enemies[i] >= 4 and power_ups[i] != "Star":
        current_lives -= 1
    if current_lives < 0:
        current_lives = 0

    life_history.append(current_lives)
    print(f"After Level {levels[i]}, Lives Remaining: {current_lives}")
print()
total_coins = sum(coins)
bonus_coin_levels = [coin for coin in coins if coin >= 7]

print("===== COIN COLLECTION =====")
print(f"Coins collected: {total_coins}")
print(f"Bonus Coin Collected: {bonus_coin_levels}")
print()
inventory = ["Mushroom", "Star", "Flower"]
used_powerups = ["Mushroom", "Star"]
print(f"Starting Inventory: {inventory}")
print(f"Used Powerups: {used_powerups}")
for item in used_powerups:
    if item in inventory:
        idx = inventory.index(item)
        inventory.pop(idx)
print(f"Remaining Inventory: {inventory}")
print()
total_enemies = sum(enemies)
final_score = sum(level_scores)

total_coins = sum(coins)
max_coins = max(coins)
min_coins = min(coins)
avg_coins = total_coins / len(levels)

total_enemies = sum(enemies)
max_enemies = max(enemies)

print("=====LEVEL ANALYSIS=====\n"
      f" Total coins: {total_coins}\n"
      f" Most coins in one level: {max_coins}\n"
      f" Fewest coins in one level: {min_coins}\n"
      f" Average coins per level: {avg_coins:.1f}\n"
      f" Total enemies: {total_enemies}\n"
      f" Most enemies in one level: {max_enemies}\n")
high_scores = [score for score in level_scores if score >= 50]

print(f"===== HIGH SCORES=====\n"
      f"High Scores List: {high_scores}\n")
score_history = []
running_total = 0


first_two_scores = score_history[:2]
last_two_scores = score_history[-2:]

print(f"===== SCORES HISTORY =====")
for i in range(len(levels)):
    running_total += level_scores[i]
    score_history.append(running_total)

    print(f"After Level {levels[i]} Score: {running_total}")

first_two_scores = score_history[:2]
last_two_scores = score_history[-2:]
final_score = score_history[-1] if score_history[-1] >= 50 else 0
print(f"First Two Scores: {first_two_scores}")
print(f"Last Two Scores: {last_two_scores}")
print("===== FINAL STATUS =====")
if current_lives == 0:
    status = "Game Over"
elif final_score >= 250:
    status = "Adventure Champion"
elif final_score >= 150:
    status = "Great Adventure"
else:
    status = "Keep Practicing"
print(f"Status: {status}\n")
if current_lives == 0:
    rank = "UnRanked"
elif final_score >= 300:
    rank = "Legend"
elif final_score >= 200:
    rank = "Master"
else:
    rank = "Rookie"

print("===== ADVENTURE RANKING =====")
print(f"Final Score: {final_score}")
print(f"Final Lives: {current_lives}")
print(f"Rank: {rank}")