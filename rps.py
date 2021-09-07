import random

def play():
    player = input("(r) for rock, (p) for paper, (s) for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    # s > p, p > r, r > s
    if player == computer:
        return "That's a tie"
    
    if is_win(player, computer):
        return "You won!"
    
    return "Computer chose " + computer + "\nYou lost!"
            
def is_win(player, computer):
    # returns true if player wins
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') \
        or (player == 'p' and computer == 'r'):
            return True 

print(play())
