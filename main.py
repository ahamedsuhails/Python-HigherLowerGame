import game_data
import art
import random
import replit



#function to get two options from dict in game_data.py
def get_options():
  ran_num = random.randint(0, len(game_data.data)-1)
  return game_data.data[ran_num]


#function to compare the choices 
def compare(choice1, choice2, choice):
  if choice == 'a':
    if choice1['follower_count'] < choice2['follower_count']:
      return 0
    else:
      return 1
  else:
    if choice2['follower_count'] < choice1['follower_count']:
      return 0
    else:
      return 1

    




print(art.logo)
option1 = get_options()
option2 = get_options()
count = 0
game_on = True
if option1 == option2:
  option2 = get_options()
while game_on:
  print(f"Compare A: {option1['name']}, {option1['description']}, {option1['country']}")
  print(art.vs)
  print(f"Against B: {option2['name']}, {option2['description']}, {option2['country']}")
  user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  result = compare(option1, option2, user_choice)
  replit.clear()
  print(art.logo)
  if result == 0:    
    print(f"Sorry, that's wrong. Your score {count}")
    game_on = False
  else:
    count += 1
    option1 = option2
    option2 = get_options()
    print(f"You're right. Your score: {count}")