import random

def dice_roll():
    return random.randint(1,6)

while True:
    user_input = input("press enter to roll the dice. (or type 'q' to quit.)")
    if user_input == 'q':
        print("thanks for playing. (Goodbye)")
        break
    result = dice_roll()
    print(f"you rolled : {result}")