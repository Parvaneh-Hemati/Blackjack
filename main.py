import random
from replit import clear

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card
  



def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.appened(11)
  return sum(cards)
  
def compare(user_score,computer_score):
  if computer_score==user_score:
    return "Draw"
  elif computer_score==21:
    return "compter win Black jak **"
  elif user_score==21:
    return "User win Black jak **" 
  elif user_score>21:
    return "User went over **" 
  elif computer_score>21:
    return "computer went over **"   
  elif user_score>computer_score:
    return "User win **"  
  else:
    return "computer win"

def play_game():
  user_cards = []
  computer_cards = []  
  is_game_over=False
  for _ in range(2):
    user_cards.append(deal_card())  
    computer_cards.append(deal_card())  
  
  while is_game_over !=True:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"user cards :{user_cards} , user score = {user_score}")
    print(f"computer cards : {computer_cards[0]}")
    if user_score==0 or computer_score==0 or user_score>21:
      is_game_over=True
    else:
       user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
       if user_should_deal == "y":
          user_cards.append(deal_card())
       else:
          is_game_over = True
  
    while computer_score<17 and computer_score!=0:
      computer_cards.append(deal_card())  
      computer_score=calculate_score(computer_cards)
      
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()

    