import random as r

player_intput = [0,0,0]
RPS_game = [1,1,1] # rock = [0], paper = [1],sisers = [2]
wins = [1,1,1] # rock = [0], paper = [1],sisers = [2]
loses = [1,1,1]
NumberPicked = [0,0,0]
RPSpiced = [0,0,0]
def PickingMAth(base, win,lose,element1, element2, AmountPicked):
    elements = [0,1.0078,4.0026,22.990]
    Change_of_picking = (base * win)/lose + elements[r.randint(element1,element2)]
    return AmountPicked/Change_of_picking

def game():
    global RPS_game
    global NumberPicked
    global RPSpiced
    amountPicked = 1
    Rock1_number = PickingMAth(RPS_game[0],wins[0],loses[0],1,3,NumberPicked[0])
    paper_number = PickingMAth(RPS_game[1],wins[1],loses[1],1,3,NumberPicked[1])
    sissers_number = PickingMAth(RPS_game[2],wins[2],loses[2],1,3, NumberPicked[2])
    pickingList = [Rock1_number,paper_number,sissers_number]
    if max(pickingList) == Rock1_number:
        RPS_game[0] +=1
        RPS_game[1] -= 1
        RPS_game[2] -= 1
        NumberPicked[0] += amountPicked
        RPSpiced[1] == 0
        RPSpiced[2] == 0 
        rock_Picked = RPSpiced[0] = 1
        return  rock_Picked
    elif max(pickingList) == paper_number:
        RPS_game [1] += 1
        RPS_game[2] -= 1
        RPS_game[0] -= 1
        NumberPicked[1] += amountPicked
        RPSpiced[0] == 0
        RPSpiced[2] == 0
        paper_picked = RPSpiced[1] = 2
        return paper_picked
    elif max(pickingList) == sissers_number:
        RPS_game[2] += 1
        RPS_game[0] -= 1
        RPS_game[1] -= 1
        NumberPicked[2] += amountPicked
        RPSpiced[0] == 0
        RPSpiced[1] == 0 
        scissors_picked = RPSpiced[2] = 3
        return scissors_picked
def player(user_choice):
    global player_intput
    player_intput = [0, 0, 0] 
    choice = user_choice.lower()
    if choice in ['rock', 'r']:
        player_intput[0] = 1
    elif choice in ['paper', 'p']:
        player_intput[1] = 1
    elif choice in ['scissors', 's']:
        player_intput[2] = 1

for x in range(100):
    player_picking = player(input(' rock, paper or scissors'))
    AI_picking_number = game()
    
