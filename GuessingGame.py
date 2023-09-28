import random

def guessing_game(guessLimit, number):
    random_number=random.randint(1, number)
    try:
        while guessLimit > 0:
            guess = int(input('what is your guess? : '))
            guessLimit-=1
            if guess==random_number:
                print("Congratulations, you got it right !")
                break
            elif guess > number:
                print("Your guess is out of range")
                print(f"You have {guessLimit} guess(es) left !")
            else:
                print("Sorry, That was wrong .")
                print(f"You have {guessLimit} guess(es) left !")
        print("Game Over")
        print(f"The Number Was : {random_number}")
    except ValueError:
        print("Only integers are allowed")
        

def easy():
    print("You get to guess a number between 1 and 10, you have 6 guesses")
    guessing_game(6,10)
    
def medium():
    print("You get to guess a number between 1 and 20, you have 4 guesses")
    guessing_game(4,20)
    
def hard():
    print("You get to guess a number between 1 and 50, you have 3 guesses")
    guessing_game(3,50)
    

def try_again():
    again = input("Do you want to play again ? Yes='Y' , No='N' : ")
    if again.upper()=="Y":
        welcome()
    elif again.upper()=="N":
        print("Thanks for playing")
    else :
        print("Wrong input")
        try_again()

def welcome():
    print("  Welcome to the number guessing game  ")
    difficulty=input("Chosse a difficulty between : Easy, Medium or Hard : ")
    if difficulty.upper()=="EASY":
        easy()
        try_again()
    elif difficulty.upper()=="MEDIUM":
        medium()
        try_again()
    elif difficulty.upper()=="HARD":
        hard()
        try_again()
    else :
        print("Wrong input")
        welcome()

welcome()




