import random
def play():
    user = input("What's your choice? 'st' for stone, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['st', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    if victory(user, computer):
        return 'You won!'

    return 'You lost!'

def victory(player, opponent):
   if (player == 'st' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'st' and opponent == 'st'):
        return True

print(play())