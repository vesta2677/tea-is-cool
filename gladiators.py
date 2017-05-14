"welcom to gladeators"
import random
    
startingNumberMax = int(input("Starting number max: "))
list1 = []
for x in range(startingNumberMax):
    list1.append(x+1)
list2 = []
for x in range(startingNumberMax):
    list2.append(x+1)
player1 = str(input("Name? "))
player2 = str(input("Name? "))
if input()== 4:
    
    while (len(list1) != 0) and (len(list2) != 0):
        playerNumber1 = int(input("What is your number player 1? "))
        while playerNumber1 not in list1:
            playerNumber1 = int(input("What is your number player 1? "))
        playerNumber2 = int(input("What is your number player 2? "))
        while playerNumber2 not in list2:
            playerNumber2 = int(input("What is your number player 2? "))
        numberSum = playerNumber1 + playerNumber2
        x = playerNumber1
        y = playerNumber2
        lista = []
        listb = []
        for i in range(x):
            lista.append(i+1)
        for i in range(y):
            listb.append(x+i+1)
        z = random.randint(1, numberSum)
        list1.remove(playerNumber1)
        list2.remove(playerNumber2)
        if z in lista:
            list1.append(numberSum)
        if z in listb:
            list2.append(numberSum)
        print(list1)
        print(list2)
else:
    while (len(list1) != 0) and (len(list2) != 0):
        if len(list1) != 1:
            playerNumber1 = list1[random.randint(0, (len(list1))-1)]
        else:
            playerNumber1 = list1[0]
        if len(list2) != 1:
            playerNumber2 = list2[random.randint(0, (len(list2))-1)]
        else:
            playerNumber2 = list2[0]
        numberSum = playerNumber1 + playerNumber2
        x = playerNumber1
        y = playerNumber2
        lista = []
        listb = []
        for i in range(x):
            lista.append(i+1)
        for i in range(y):
            listb.append(x+i+1)
        z = random.randint(1, numberSum)
        list1.remove(playerNumber1)
        list2.remove(playerNumber2)
        if z in lista:
            list1.append(numberSum)
        if z in listb:
            list2.append(numberSum)
        print(str(list1)+ '    ' +str(list2))
        

