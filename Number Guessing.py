import random as r
import sys
guess_num = 10
difficulty = ''
i = ''

#determine difficulty
while difficulty == '':
  try:
    difficulty = int(input('difficulty from 1 to 10     '))
    if not difficulty >= 1 and not difficulty <= 10: 
      print('I said 1 to 10.')
  except ValueError: print("It seems that you don't know what a number is, or maybe you just lack common sense. Here, let me help. Choose 1,2,3,4,5,6,7,8,9, or 10.")

def guess(l):
  """Guess a random number from 1 to 10*l"""
  print(f'starting guessing game at level {l}...')
  guesses = guess_num
  guess = ''
  
  if l >= 1 and l <= 10: #set max proportional to difficulty    
    max = int(10*l)
  
  secret = r.randint(1, max) #generate number to guess
  
  while guesses > 0:    
    #get input
    while guess == '': #check for if number is an int
      try:
        guess = int(input(f'Guess a whole number between 1 and {max}     ')) 
        #guess
      except ValueError:
        print('I said, guess a WHOLE NUMBER.')
    
    #logic for guessing
    if (guess < 1 or guess > max):
        print(f'I said, BETWEEN 1 AND {max}') #out of range
        guesses += 1
        guess = ''
    elif (guess < secret):
        print(f'Too low! Tries left: {guesses}') #too low
        guess = ''
    elif(guess > secret):
        print(f'Too high! Tries left: {guesses}') #too high
        guess = ''
    else:
        print('You win!') #win
        return True
    guesses -= 1
  return False

# round 1
win = guess(difficulty)

#next rounds
while difficulty <= 10:
  difficulty += 1
  if win == True and difficulty <=10: 
    #asks for next level, either exits with message ggs or reruns a round.
    new_lvl = str(input('Next level? [Y/n]          '))
    i = ''
    while i == '':
      if new_lvl == 'Y' or new_lvl == 'y':
        i = 'a'
        win = guess(difficulty)
      else:
        print('ok, ggs!') #NOTE: this is intentional. I could implement a check for Y or n, but I think that if this were a person operating the game, and when they asked you whether or not another game would be started, and you said "banana," they'd just be weirded out and leave, thus not starting another game.
        sys.exit()
  elif win == False:
    print('You lose, ggs though!')
    sys.exit() #lose
  else:
    print("Looks like we're out of levels, ggs!") #Should only come up on lvl 10 win