import random
print("welcome to rock, paper, and scissors game.")
options = ['rock','paper','scissors']
Useroptions = ['rock','paper','scissors','q']
userWin = 0
computerWin = 0
while True:
    print("1. rock, 2. scissors, 3. paper and Q to Quit.")       
    userInput = input("enter your choice: ").lower()
    if userInput == 'q':
        break
    if userInput not in Useroptions:
        continue
    computerChoice = options[random.randint(0,2)]     
    print("computer picked", computerChoice, ".")
    
    if userInput == 'rock' and computerChoice == 'scissors':
        print("You Won.")
        userWin += 1
        
    elif userInput == 'scissors' and computerChoice == 'paper':
        print("You Won.")
        userWin += 1
        
    elif userInput == 'paper' and computerChoice == 'rock':
        print("You Won.")
        userWin += 1        
        
    else:
        print("You lost.")
        computerWin += 1
        
print("You won", userWin, "times.")
print("The computer won", computerWin, "times.")
print("Goodbye!")        
