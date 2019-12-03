
import random
 
guessesTaken = 0
 
number = random.randint(30, 101)
print('Well, I am thinking of a number between 30 and 100.')
 
while guessesTaken < 6:
 print('Take a guess.') 
 guess = input()
 guess = int(guess)
 
 guessesTaken = guessesTaken + 1
 
 if guess < number:
   print('Your guess is too low.') 
 elif guess > number:
   print('Your guess is too high.')
 elif guess == number:
  print('Your guess is right')
 elif guess != number:
   number = str(number)
   print('The number i was thinking was ', number )
  
