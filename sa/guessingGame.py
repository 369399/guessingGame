
import random
 
guessesTaken = 0
 
number = random.randint(1, 20)
print(number, " your number is")
print('Well, I am thinking of a number between 1 and 20.')
 
while guessesTaken < 6:
 print('Take a guess.') # There are four spaces in front of print.
 guess = input()
 guess = int(guess)
 
 guessesTaken = guessesTaken + 1
 
 