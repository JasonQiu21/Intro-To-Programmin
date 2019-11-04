import getpass
import string
import sys
from random_word import RandomWords
r = RandomWords()
#Welcome to... HANGMAN
print("welcome to...")
print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
""")
#ASCII art for hangman
states = ["""
 _________
 |/      |
 |       |
 |         
 |        
 |         
 |
_|___""",
"""
 _________
 |/      |
 |      (ツ)
 |         
 |        
 |         
 |
_|___""",
"""
 _________
 |/      |
 |      (ツ)
 |       | 
 |       |
 |         
 |
_|___""",
"""
 _________
 |/      |
 |      (ツ)
 |      /| 
 |       |
 |         
 |
_|___""",
"""
 _________
 |/      |
 |      (ツ)
 |      /|\\
 |       |
 |         
 |
_|___""",
"""
 _________
 |/      |
 |      (ツ)
 |      /|\\
 |       |
 |      /  
 |
_|___""",
"""
 _________
 |/      |
 |      (ツ)
 |      /|\\
 |       |
 |      / \\
 |
_|___"""]

win = False

def split(word):
    """split string into list"""
    return [char for char in word]

def check_ascii(word):
    """check if a word has only ascii letters"""
    for i in word:
        if i not in string.ascii_letters:
            return False
    return True

def get_secret_word():
    """Generate secret word"""
    custom_or_dictionary = str(input("custom word (1) or random word from dictionary (2)?     ")) # query to use a dictionary or secret word
    while custom_or_dictionary != '1' and custom_or_dictionary != '2': # make sure that input is 1 or 2
        custom_or_dictionary = str(input("type '1' or '2'"))
    if custom_or_dictionary == '1': #custom word (find a friend)
        secret_word = str(getpass.getpass('Get someone else to give you a word:     ')).lower()
        while check_ascii(secret_word) != True:
            secret_word = str(getpass.getpass('Make sure the secret word is only the 26 english letters:     ')).lower()
    elif custom_or_dictionary == '2': #random dictionary word
        secret_word = r.get_random_word().lower()
        while not check_ascii(secret_word): #if, for some reason, we have some sort of apostrophe or whatever in get_random_word()
            secret_word = r.get_random_word().lower()
    else:
        print('Impossible Error', file=sys.stderr) #debug - input should be filtered to just '1' and '2'
        sys.exit()
    return secret_word

def get_user_guess():
    """get player's guess, make sure is one letter"""
    guess = str(input("guess a letter:     ")).lower()
    while len(guess) != 1 or guess not in string.ascii_letters:
        guess = str(input("guess a SINGLE letter:     ")).lower()
    return guess



#Initial Conditions
a = 0 #determines which ascii art of hangman to use
i = 6 #used to check how many guesses you have left - a counts up, i counts down
wrong_guesses = []
current_state = states[a] #the actual art that gets printed
print(current_state)
secret = get_secret_word()
message = "_ "*len(secret) #begins as just all underscores, then those underscores get replaced
print(message)

def checkword(secret, guess):
    """Check if guess is secret word, replace the elements of message with the guess letter
        example: asdf in underscores (_ _ _ _) will become (a _ _ _) after guessing 'a' """
    global message
    s_list = split(secret)
    m_list = split(message)
    x = False #remains false if guess is not in secret word
    for i in range(len(s_list)): #replace all instances of guessed letter in the message
        if s_list[i] == guess:
            m_list.pop(i*2)
            m_list.insert(i*2,guess)
            message = ''.join(m_list)
            x = True
    return x

def score_count(secret):
    """Processes user guess to do the following:
        - check whether or not it's in the function
        - runs checkword
        - if wrong, 'draws' the next body part, as well as appending wrong_guesses
        - determines if you've met the win condition
        """
    #initial conditions - letters guessed wrong, variables used in computation, splitting the secret into an array (easier to work with)
    
    global wrong_guesses
    global a
    global i
    global current_state
    #guess prompt
    correct = False #whether or not your last guess was correct
    guess = get_user_guess()
    
    correct = checkword(secret, guess)

    #print the next round's stuff
    if correct == False: #If your guess is wrong
        wrong_guesses.append(guess)
        print(f'wrong guesses: {wrong_guesses}')
        a += 1
        i -= 1
        current_state = states[a]
        print(current_state)
        if a == 6: #if all guesses are used up (hangman is fully drawn)
            return False
        print(message)
    elif '_' in message and correct == True: #If your guess is right, and there are still letters to guess
        print(f'wrong guesses: {wrong_guesses}')
        print(current_state)
        print(message)
        correct = False
    else: #Win condition - last letter guessed is right, no empty spcaes.
        i = 0
        return True

while i > 0:
    win = score_count(secret)

#display final messag
if win == True:
    print(current_state)
    print(message)
    print('You Win!')
else:
    print('You Lose!')