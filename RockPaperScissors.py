import random
compScore = 0
playerScore = 0

print("You are about rock paper scissors against the computer. After you see the word shoot, choose rock, paper, or scissors (or 1,2,3).")
print("______________________________________________________________________________________________________________________________________________________")
print("")

while playerScore < 3 or compScore< 3:
    print("Rock ")
    print("Paper ")
    print("Scissors ")
    compChoice = random.randint(1,3)
    playerChoice = input("Shoot ")
    while playerChoice != 1 or playerChoice != 2 or playerChoice !=3:
        if playerChoice == "Rock" or playerChoice == "rock" or playerChoice == "1":
            playerChoice = 1
            break
        elif playerChoice == "Paper" or playerChoice == "paper" or playerChoice == "2":
            playerChoice = 2
            break
        elif playerChoice == "Scissors" or playerChoice == "scissors" or playerChoice == "3":
            playerChoice = 3
            break
        else:
            print("not a valid input")
            break
        
    if compChoice == 1:
        print("Computer: Rock")
    elif compChoice ==2:
        print("Computer: Paper")
    elif compChoice == 3:
        print("Computer: Scissors")

    if compChoice == playerChoice:
        print("It's a tie")
    elif compChoice == 2 and playerChoice == 1 or compChoice==1 and playerChoice == 3 or compChoice == 3 and playerChoice == 2:
        print("Computer's Point!")
        compScore = compScore+1
    elif playerChoice == 2 and compChoice == 1 or playerChoice==1 and compChoice == 3 or playerChoice == 3 and compChoice == 2:
        print("Player's Point!")
        playerScore = playerScore +1

    if playerScore == 3:
        print("Player wins!")
        break
    elif compScore == 3:
        print("Computer wins!")
        break

                       
