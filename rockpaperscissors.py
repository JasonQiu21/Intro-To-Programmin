import random
wins_to_win = 2 #best X out of X+1 (2 out of 3 for now)
options = ['rock', 'paper', 'scissors'] #valid options
options_string = ', '.join(options)
combinations = {
    'rock':{
        'paper':'lose',
        'scissors':'win',
    },
    'paper':{
        'scissors':'lose',
        'rock':'win'
    },
    'scissors':{
        'rock':'lose',
        'paper':'win'
    }
}

score = {'player':0, 'computer':0}

def user_input():
    """Get player input (i), make sure valid choice"""
    i = ''
    i = str(input("Rock, Paper, Scissors, Shoot!     ")).lower() #Allows for camelcase and other weird inputs that are still the same word.
    while i not in options:
        #while user hasn't picked rock, paper, scissors
        print()
        i = str(input(f"No, {i} is not an option. Options: {options_string}. Let's try again. Rock, Paper, Scissors, Shoot!     ")).lower()
    return i

def computer_input():
    """Get random computer input from our options"""
    return random.choice(options)

def outcome(p,c):
    """Get the outcome of a round of rock, paper, scissors
    from player input p and computer input c"""
    print(f"User chooses {p}, computer chooses {c}")
    if p == c:
        result = 'tie'
    else:
        result = combinations[p][c]
    return result

def score_counter(result):
    """Take win, loss, tie and figure out who gets a point"""
    global score
    if result == 'tie':
        print('Tie!')
    elif result == 'lose':
        print('You lose!')
        score['computer'] += 1
    elif result == 'win':
        print('You win!')
        score['player'] += 1
    print(f'Score: {score}')

def determine_win(score_dict):
    win_score = 0
    winner = ''
    for i, j in score.items():
        if j > win_score:
            winner = i
            win_score = j
    return winner
#play till best of however many is determined
while score['player'] <wins_to_win and score['computer'] <wins_to_win:
    score_counter(outcome(user_input(), computer_input()))

#get winnner
print(f"winner: {determine_win(score)}")