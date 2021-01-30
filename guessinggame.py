#guessing game 

import random          #import random libary for taking random number
jacpot=random.randint(1,100)       #random number genarate in jackpot variable
guess=int(input("guess your number :"))     # for taking user guess in guess variable
counter=1
while guess!=jacpot:                         # loops use for taking multiple input when guess is wrong 
    if guess>jacpot:
        print("your guess is very high guess low..")
    else:
         print("your guess is very low guess haigh...")
    guess=int(input("re guess your number :"))      # taking user re guess number
    counter += 1
print("congratulation your guess is right and you taking",counter,"step")