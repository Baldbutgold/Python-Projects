import random

playablePositions = [0,2,4,6,8,10,12,14,16]
gameMap = ['_','|','_','|','_','\n','_','|','_','|','_','\n',' ','|',' ','|',' ','\n']
def printMap():
    print(''.join(gameMap))

def startGame():
    print("""To Play the Game Pick a value from 1 to 9
Each value is represnted from left to right, up to bottom
Meaning 1 is top left corner, 2 is top middle and so on
Have Fun!!!""")
    printMap()
    isAlive = True
    playerTurn()

def isAlive():
    #checks if x or o are in any of the winning positions
    winningPositions = [[0,2,4],[6,8,10],[12,14,16],[0,6,12],[2,8,14],[4,10,16],[0,8,16],[4,8,12]]
    for i in winningPositions:
        x = ''
        for j in range(3):
            y = i[j]
            x += gameMap[y]
        if x == 'xxx': 
            print('First player WON!')
            return False
        if x == "ooo":
            print('Second player WON!')
            return False
    positions = ''
    for i in playablePositions:
        positions += str(i)
        if len(positions) == 9:
            if positions == 'n' * 9:
                print('Draw')
                return False
    return True
def gameRender(pos, sym):
    while isAlive() == True:
        gameMap[pos] = sym
        deletepos = int(pos)/2
        playablePositions[int(deletepos)] = 'n'
        printMap()
        break

def checker(Player):
    #checks for positions that are available if chosen a not avaialbe position repeat
    available = False
    while available == False and isAlive() == True:
        try:
            if Player == 'First player':
                symbol = 'x'
            elif Player == 'Second player':
                symbol = 'o'
            playedPosition = input('Pick a position from 1 to 9\n')
            position = (int(playedPosition)  - 1) * 2
            playedPosition = print(Player + ' Turn')
            if position in playablePositions:
               gameRender(position, symbol)   
               break
            else:
                print('That position is unplayable')
                pass
        except:
            print('Invalid Input')

def playerTurn():
    player = input('Press 1 to play against a friend, Press 2 to play against a basic bot\n')

    while isAlive() == True:
        if player == '1':
            #start playing against a friend
            checker('First player')
            checker('Second player')
        elif player == '2':
            #start playing against a bot
            checker('First player')
            basicBot()
        else:
            print('Invalid Input, try again')
            quit()

def basicBot(): 
    randomposition = random.choice(playablePositions)
    symbol = 'o'
    while randomposition == 'n':
        randomposition = random.choice(playablePositions)
    else:
        gameRender(randomposition , symbol)
        print("Bot's turn he played", (int(randomposition/2 + 1)))
            
startGame()


