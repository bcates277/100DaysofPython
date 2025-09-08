import random
from game_data import data
from art import logo, vs

def normalize_data(account):
    account_name = account['name']
    account_country = account['country']
    account_follower = account['follower_count']
    account_description = account['description']
    return f"{account_name}, {account_description}, {account_country}"

def check_followers(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)
score = 0
play_game = True

while play_game:
    account_a = random.choice(data)
    account_b = random.choice(data)
    print(f"Compare A: {normalize_data(account_a)}")
    print(vs)
    print(f"Against B: {normalize_data(account_b)}")
    answer = input(f"Who has more followers? Type 'a' or 'b': ").lower()
    account_a_followers = account_a['follower_count']
    account_b_followers = account_b['follower_count']
    is_correct = check_followers(answer, account_a_followers, account_b_followers)
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        play_game = False
        print(f"Sorry, that's wrong. Final score: {score}")

