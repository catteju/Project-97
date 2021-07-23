import random

num = random.randint(1,9)

chances = 5

while(chances>0) : 
    guess = int(input("Enter Your Guess"))

    if(guess>num) : 
        print("Greater Than The Correct Value")
    
    elif(guess<num) : 
        print("Lesser Than The Correct Number")
    
    elif(guess == num) : 
        print("YOU WON !!")
    
    chances = chances-1

if(chances<=0) :
    print("You Lost")