import random
number = random.randint(50,60)
print("GUESS A NUMBER BETWEEN 50 AND 60")
#print("YOU HAVE 5 CHANCES TO GUESS THE NUMBER")
guess = input("ENTER YOUR GUESS : ")

if(guess==number):
    print("YOU MADE IT! :)")
 
if (guess!=number):
    print("YOU LOOSE :( THE NUMBER IS : ",number)