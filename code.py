import random
while True:
    p1 = int(input("Enter The Number 1 for stone 2 paper 3 scisor"))
    p2 = random.randint(1,4)
    if p1 == 1 and p2 == 2:
        print("Player 1 Stone Vs Player 2 Paper")
        print("Player 2 wins")
        break
    elif p1 == 1 and p2 == 3: 
        print("Player 1 Stone Vs Player 2 scisor")
        print("Player 1 wins")
        break
    elif p1 == 2 and p2 == 3: 
        print("Player 1 Paper Vs Player 2 scisor")
        print("Player 2 wins")
        break
    elif p1 == 2 and p2 == 1:
        print("Player 1 Paper Vs Player 2 Stone")
        print("Player 1 wins")
        break
    elif p1 == 3 and p2 == 1: 
        print("Player 1 scisor Vs Player 2 stone")
        print("Player 2 wins")
        break
    elif p1 == 3 and p2 == 2: 
        print("Player 1 scisor Vs Player 2 paper")
        print("Player 1 wins")
        break
    
    
    
  #1 stone 2 paper 3 scisor