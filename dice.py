import random as r

scoreCard = {"playerTwoScore": 10, "playerOneScore": 0}

def getPlayerOneScore():
    return scoreCard["playerOneScore"]

def getPlayerTwoScore():
    return scoreCard["playerTwoScore"]

def setPlayerOneScore(score):
    scoreCard["playerOneScore"] = score

def setPlayerTwoScore(score):
    scoreCard["playerTwoScore"] = score

def roll():
    return r.randint(1, 6)

currentPlayer = "ONE"

ix = 0
while getPlayerOneScore() < 100 and getPlayerTwoScore() < 100:
    print("Run: " + str(ix))
    ix += 1
    currentRoll = roll()
    print('Player ' + currentPlayer + ' rolled a ' + str(currentRoll) + '!')
    if currentPlayer == 'ONE':
        setPlayerOneScore(getPlayerOneScore() + currentRoll)
        print('Player ONE score: '+ str(getPlayerOneScore()))
        currentPlayer = 'TWO'
    elif currentPlayer == 'TWO':
        setPlayerTwoScore(getPlayerTwoScore() + currentRoll)
        print('Player TWO score: '+ str(getPlayerTwoScore()))
        currentPlayer = 'ONE'

if getPlayerOneScore() >= 100:
    print("Player 1 wins!")
    
if getPlayerTwoScore() >= 100:
    print("Player 2 wins!")