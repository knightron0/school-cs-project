from random import randint

print("You are X. The computer is O")
gameboard = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
tempboard = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
def temp3(a, one, two, three):
    if a == tempboard[one] == tempboard[two] == tempboard[three]:
        return True;
def tempall(a):
    if temp3(a,0,3,6) == True:
        return True
    elif temp3(a,1,4,7) == True:
        return True
    elif temp3(a,2,5,8) == True:
        return True
    elif temp3(a,0,1,2) == True:
        return True
    elif temp3(a,3,4,5) == True:
        return True
    elif temp3(a,6,7,8) == True:
        return True
    elif temp3(a,0,4,8) == True:
        return True
    elif temp3(a,2,4,6) == True:
        return True
    else:
        return False
def checkO(freepos):
    for i in freepos:
        tempboard[i] = "O"
        if tempall("O") == True:
            return True
            break
        else:
            return False
            break
        tempboard[i] = " "
def printboard():
    print("-------------")
    print("|",gameboard[0], "|",gameboard[1], "|",gameboard[2], "|")
    print("-------------")
    print("|",gameboard[3], "|",gameboard[4], "|",gameboard[5], "|")
    print("-------------")
    print("|",gameboard[6], "|",gameboard[7], "|",gameboard[8], "|")
    print("-------------")
def check3(a, one, two, three):
    if a == gameboard[one] == gameboard[two] == gameboard[three]:
        return True;
printboard()
def checkall(a):
    if check3(a,0,3,6) == True:
        return True
    elif check3(a,1,4,7) == True:
        return True
    elif check3(a,2,5,8) == True:
        return True
    elif check3(a,0,1,2) == True:
        return True
    elif check3(a,3,4,5) == True:
        return True
    elif check3(a,6,7,8) == True:
        return True
    elif check3(a,0,4,8) == True:
        return True
    elif check3(a,2,4,6) == True:
        return True
    else:
        return False
tf = True
def aipos():
    freepos = []
    check = False
    check2 = False
    k = 0
    for i in range(0,9):
        if gameboard[i] != "X" and gameboard[i] != "O":
            freepos.append(i)
    for i in range(0,9):
        tempboard[i] = gameboard[i]
    for i in freepos:
        tempboard[i] = "X"
        if tempall("X") == True:
            k = i
            check = True
            check2 = True
            break
        else:
            check = False
        tempboard[i] = " "
    if check == False:
        for i in freepos:
            tempboard[i] = "O"
            if tempall("O") == True:
                return int(i)
                break
            else:
                return freepos[randint(0, (len(freepos) - 1))]
            break
        tempboard[i] = " "
    else:
        if checkO(freepos) == True:
            for i in freepos:
                tempboard[i] = "O"
                if tempall("O") == True:
                    return int(i)
                    break
                else:
                    return freepos[randint(0, (len(freepos) - 1))]
                break
                tempboard[i] = " "
        else:
            return int(k)
        
def checkdraw():
    freepos = []
    for i in range(0,9):
        if gameboard[i] != "X" and gameboard[i] != "O":
            freepos.append(i)
    if len(freepos) == 0 and checkall("O") == False and checkall("X") == False:
        return True
    else:
        return False
while  tf == True:
    uspos = int(input("Enter the position:"))
    if gameboard[uspos] != "X"and gameboard[uspos] != "O" and checkdraw() == False:
        gameboard[uspos] = "X"
        if checkall("X") == True:
            printboard()
            print("You win!!!")
            break
        elif checkall("O") == True:
            printboard()
            print("You lose!!f!")
            break
        if checkdraw() == False:
            oppos = aipos()
            gameboard[oppos] = "O"
            printboard()
            if checkall("X") == True:
                print("You win!!!")
                break
            elif checkall("O") == True:
                print("You lose!!!")
                break
        else:
            printboard()
            print("Draw! Good game :-)")
            break
    else:
        print("Sorry, that spot has already been taken. :-(")
    