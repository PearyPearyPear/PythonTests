import random

def scrambler(iterations):
    posFB = ['↷', '↶']
    posRL = ['↑', '↓']
    posDU = ['←', '→']
    posMoves = ['F', 'B', 'R', 'L', 'D', 'U']

    for i in range(iterations):
        randturn = random.randint(1, len(posMoves))

        print(posMoves[randturn - 1], end="")

        if randturn in [1, 2]:  
            print(random.choice(posFB), end="   ")
        elif randturn in [3, 4]:  
            print(random.choice(posRL), end="   ")
        elif randturn in [5, 6]:  
            print(random.choice(posDU), end="   ")
        else:  
            print("\nbro what did you do to the code fix pls")

a = int(input("Enter your number of turns: "))
scrambler(a)
