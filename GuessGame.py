#C-97 Project
#Guessing Numbers
import random
print("Challenge: Guess the number between 1 and 9 in 5 chances..")
number=random.randint(1,9)
#print(number)
chances=0
while(chances<=5):
  num=int(input("Guess the number:"))
  if(num==number):
    print("Congratulations.. you guessed it right...")
    break;
  elif(num>number):
    print("The number is lesser than what you have guessed. Take another chance.")
  else:
    print("The number is greater than what you have guessed. Take another chance.")
  chances=chances+1
if(chances >5):
  print("You lost all your chances.. Better luck next time..")
