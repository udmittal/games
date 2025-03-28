import random
import time

def userTurnToGuess():
    print ("Great! Let me choose a number between 1 to 100.")
    time.sleep(3)
    print ("I have chosen a number between 1 to 100. Now you have to guess that number.")
    randomNumber = random.randrange(1,100,1)
    userGuessCount = 0
    while True:
        isInputCorrect = True
        guess = input("Guess the number: ")
        try:
            guess = int(guess)
            if guess < 0 or guess > 100:
                print("You need to enter a number between 1 and 100")
                isInputCorrect = False
            if isInputCorrect:    
                userGuessCount = userGuessCount + 1
                if guess < randomNumber:
                    print("The number I have chosen is greater than " + str(guess))
                elif guess > randomNumber:
                    print("The number I have chosen is less than " + str(guess))
                else:
                    print(str(randomNumber) + " is the chosen number. You guessed it right.")
                    print("You guessed the number in " + str(userGuessCount)+ " " + {True:"guess.", False:"guesses."}[userGuessCount==1])
                    break
        except:
            print("You need to enter a number between 1 and 100")
            isInputCorrect = False
    return userGuessCount

def computerTurnToGuess():
    print ("Now its your turn to choose the number between 1 to 100. Please let me know when you have chosen the number.")
    time.sleep(3)
    numberChosen = input("Press enter to start the game...")
    lowerLimit = 1
    upperLimit = 100
    computerGuessCount = 0
    print("Great! Let me guess the number.")
    while True:
        time.sleep(1)    
        guessedNumber = random.randrange(lowerLimit, upperLimit,1)
        computerGuessCount = computerGuessCount + 1
        guessResult = input("Is your number " + str(guessedNumber) + " (y/n)? ")
        while guessResult.lower() != 'y' and guessResult.lower() != 'n':
            guessResult = input("I didn't quite get that. Is your number " + str(guessedNumber) + " (y/n)? ")
        if guessResult.lower() == 'n':
            guessResult = input("Is your number greater or less than " + str(guessedNumber) + " (g/l)? ")
            while guessResult.lower() != 'g' and guessResult.lower() != 'l':
                guessResult = input("I didn't quite get that. Is your number greater or less than " + str(guessedNumber) + " (g/l)? ")
            if guessResult.lower() == 'l':
                upperLimit = int(guessedNumber)
            if guessResult.lower() == 'g':
                lowerLimit = int(guessedNumber)
        else:
            print ("Awesome! I guessed your number in " + str(computerGuessCount) + " " + {True:"guess.", False:"guesses."}[computerGuessCount==1])
            break
    return computerGuessCount


playAgain = 'y'
userGuesses = 0
computerGuesses = 0
userGameWonCount = 0
tieGameCount = 0
computerGameWonCount = 0
name = input("What is your name? ")
playAgain = input("Hello " + name +"! Would you like to play a number guessing game (y/n)? ")
while playAgain.lower() != 'y' and playAgain.lower() != 'n':
    playAgain = input("I didn't quite get that. Would you like to play a number guessing game (y/n)? ")
while playAgain.lower() == 'y':
    gameStart = input ("Would you like to guess first (y/n)? ")
    while gameStart.lower() != 'y' and gameStart.lower() != 'n':
        gameStart = input("I didn't quite get that. Would you like to guess first (y/n)? ")
    if gameStart.lower() == 'y':
        userGuesses = userTurnToGuess()
        computerGuesses = computerTurnToGuess()
    elif gameStart.lower() == 'n':
        computerGuesses = computerTurnToGuess()
        userGuesses = userTurnToGuess()
    if userGuesses < computerGuesses:
        print ("You won the game. Keep it up!")
        userGameWonCount = userGameWonCount + 1
    elif userGuesses > computerGuesses:
        print ("Looks like I won. Better luck next time.")
        computerGameWonCount = computerGameWonCount + 1
    else:
        print ("We both guessed in " + str(computerGuesses) + " " + {True:"guess.", False:"guesses."}[computerGuesses==1]+ " The game is a tie. Well played.")
        tieGameCount = tieGameCount + 1
    print ("I really enjoyed playing with you.")
    playAgain = input("Do you want to play again (y/n)? ")
totalGamesPlayed = computerGameWonCount + userGameWonCount + tieGameCount
if tieGameCount > 0:
    print("We played " + str(totalGamesPlayed)  + " " + {True:"game.", False:"games."}[totalGamesPlayed==1] + "Out of these you won " + str(userGameWonCount) + " " + {True:"game.", False:"games."}[userGameWonCount==1]+ " I won " + str(computerGameWonCount)  + " " + {True:"game.", False:"games."}[computerGameWonCount==1] + str(tieGameCount) + " " + {True:"game.", False:"games."}[tieGameCount==1]+ " were tied.")
if tieGameCount == 0 and (userGameWonCount > 0 or computerGameWonCount > 0):
    print("We played " + str(totalGamesPlayed)  + " " + {True:"game.", False:"games."}[totalGamesPlayed==1] + "Out of these you won " + str(userGameWonCount) + " " + {True:"game.", False:"games."}[userGameWonCount==1]+ " I won " + str(computerGameWonCount)  + " " + {True:"game.", False:"games."}[computerGameWonCount==1])
if userGameWonCount > computerGameWonCount:
    print("Congratulations! You won the tournament. Let's play another one soon.")
elif userGameWonCount == computerGameWonCount:
    print("This tournament is a tie. Let's play another one soon.")
else:
    print("I enjoyed the tournament. Let's play another one soon.")

if tieGameCount == 0 and userGameWonCount == 0 and computerGameWonCount == 0 and playAgain.lower() == 'n':
    print("No problem. Come back whenever you want to play a number guessing game. I'll be here.")
