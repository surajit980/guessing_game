#guessing game 
import os
import random          #import random libary for taking random number
jacpot=random.randint(1,100)       #random number genarate in jackpot variable
def guessing_game():
     guess=int(input("guess your number between 1 to 100 :"))     # for taking user guess in guess variable
     if guess<=100:
         os.system("cls")
         print("now you are in game")
         counter=1
         while guess!=jacpot:                         # loops use for taking multiple input when guess is wrong 
            if guess>jacpot:
                print("your guess is very high guess low..")
            else:
                print("your guess is very low guess haigh...")
            guess=int(input("re guess your number :"))      # taking user re guess number
            counter += 1
         print("congratulation your guess is right and you taking",counter,"step")
     else:
         print("you need to guess numbers between 1 to 100..sorry please try again......")
         guessing_game()
guessing_game()