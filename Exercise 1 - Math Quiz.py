import random

def decideOperation():
    operate = ["+","-"]
    toggle = random.choice(operate)
    return toggle

def IsCorrect(ans,guess):
    if ans == guess: return True
    else: return False

def randomInt(a):
    num1 = a[0]
    num2 = a[1]
    num = random.randint(num1,num2)
    return num

def displayResults(points):
    if points > 90: rank = "S"
    elif points <= 90 and points > 80: 
        rank = "A"
        print("Well done!")
    elif points <= 80 and points > 70: rank = "B"
    elif points <= 70 and points > 60: rank = "C"
    elif points <= 60 and points > 50: rank = "D"
    else: rank = "F"
    
    print(f"\n\nYour score is {points}/100,\nYou have gained a rank of {rank}!")
    if rank == "F":
        print("Yikes!")
        

diff = {"easy": (0,9),
        "medium":(10,99),
        "hard":(1000,9999)}

play = ""

while play != "N":
    print("Calculester: QUIZ EDITION")
    start = input("DIFFICULTY LEVEL \n1. Easy \n2. Moderate \n3. Advanced \n\n " ).lower()
    a = diff.get(start)
    points = 0
    for i in range(10):
        x = randomInt(a) 
        y = randomInt(a)
        op = decideOperation()
        ans = lambda x, y, op: x + y if op == "+" else x - y
        que = lambda op: "plus" if op == "+" else "minus"
        for tries in range(2):
            try: 
                guess = int(input(f"{i+1}) what is {x} {que(op)} {y}? ")) #question
                correct = IsCorrect(ans(x,y,op),guess) # sends it to correct function
                if correct == True and tries == 0: # if correct on first try
                    print("That's correct! you receive 10 points")
                    points += 10
                    break
                elif correct == True and tries == 1:#if correct on second try
                    print("That's correct! you receive 5 points")
                    points += 5
                    break
                elif correct == False and tries == 0: 
                    print("Oops! let's try that again")
                else: 
                    print(f"Oops! the answer is {ans(x,y,op)} better luck next time!")
                    break
            except ValueError: 
                print("Whoops that's not a number! ")
    displayResults(points)
    play = input("Wanna play again? [Y/N]\n\n").upper()
print("Goodbye!")



