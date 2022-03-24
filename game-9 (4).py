#AMIRA BASSAM
#Kayles game.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
emp_lst=["-"for i in range (20)]
for i in range(0,len(lst)):
    while True:
        try:
            num_of_player1 = list(map(int, input(("player 1 Enter num: ")).split()))
            break
        except ValueError:
            print("input can't be string")
            continue
    # PLAYER 1
    # if player1 enter 2 NUM:
    if len(num_of_player1)>1:

        while num_of_player1[0] > 20 or num_of_player1[1] > 20 or num_of_player1[0] < 0 or num_of_player1[1]<0 or abs(num_of_player1[0]-num_of_player1[1]) != 1:
            print("invalid input")
            num_of_player1 = list(map(int, input(("player 1 Enter num: ")).split()))
            continue

        if num_of_player1[0] > 10 and num_of_player1[1] > 10 and num_of_player1[0] != 20 and num_of_player1[1] != 20:
                lst.reverse()
                num_of_player1[0] -= 10
                num_of_player1 [1] -= 10
                index = lst.index(num_of_player1[0])
                lst[index] = "-"
                index2 = lst.index(num_of_player1[1])
                lst[index2] = "-"
                lst.reverse()
                print(*lst)
        elif num_of_player1[0] > 10 and num_of_player1[1] < 10 and num_of_player1[0] != 20:
                lst.reverse()
                num_of_player1[0] -= 10
                index = lst.index(num_of_player1[0])
                lst[index] = "-"
                lst.reverse()
                index2 = lst.index(num_of_player1[1])
                lst[index2] = "-"
                print(*lst)
        elif num_of_player1[1] > 10 and num_of_player1[0] < 10 and num_of_player1[1] != 20:
                lst.reverse()
                num_of_player1[1] -= 10
                index = lst.index(num_of_player1[0])
                lst[index] = "-"
                lst.reverse()
                index2 = lst.index(num_of_player1[1])
                lst[index2] = "-"
                print(*lst)
        else:
            del lst[num_of_player1[0]-1]
            lst.insert(num_of_player1[0]-1,'-')
            del lst[num_of_player1[1] - 1]
            lst.insert(num_of_player1[1] - 1, '-')
            print(*lst)
        if lst == emp_lst:
            print("Player 1 won !")
            exit()
    else:

        if num_of_player1[0]<0 or num_of_player1[0] > 20:
            print("invalid number")
            num_of_player1 = list(map(int,input("player 1 please enter your number").split()))
            continue
        if num_of_player1[0] > 10 and num_of_player1[0] != 20:
            lst.reverse()
            num_of_player1[0] -= 10
            index =lst.index(num_of_player1[0])
            lst[index] = "-"
            lst.reverse()
            print(*lst)
        else:
            del lst[num_of_player1[0] - 1]
            lst.insert(num_of_player1[0] - 1, '-')
            print(*lst)
        if lst == emp_lst:
            print("player 1 won")
            exit()

        #PLAYER 2

    num_of_player2 = list(map(int,input("player 2 Enter num: ").split()))
    # if player2 enter 2 NUM:
    if len(num_of_player2) > 1:
        while num_of_player2[0] > 20 or num_of_player2[1] > 20 or num_of_player2[0] < 0 or num_of_player2[1] < 0 or abs(num_of_player2[0] - num_of_player2[1]) != 1:
            print("invalid input")
            num_of_player2 = list(map(int, input(("player 2 Enter nums : ")).split()))
            continue
        if num_of_player2[0] > 10 and num_of_player2[1] > 10 and num_of_player2[0] != 20 and num_of_player2[1] != 20:
            lst.reverse()
            num_of_player2[0] -= 10
            num_of_player2[1] -= 10
            index = lst.index(num_of_player2[0])
            lst[index] = "-"
            index2 = lst.index(num_of_player2[1])
            lst[index2] = "-"
            lst.reverse()
            print(*lst)
        elif num_of_player2[0] > 10 and num_of_player2[1] < 10 and num_of_player2[0] != 20:
            lst.reverse()
            num_of_player2[0] -= 10
            index = lst.index(num_of_player2[0])
            lst[index] = "-"
            lst.reverse()
            index2 = lst.index(num_of_player2[1])
            lst[index2] = "-"
            print(*lst)
        elif num_of_player2[1] > 10 and num_of_player2[0] < 10 and num_of_player2[1] != 20:
            lst.reverse()
            num_of_player2[1] -= 10
            index = lst.index(num_of_player2[0])
            lst[index] = "-"
            lst.reverse()
            index2 = lst.index(num_of_player2[1])
            lst[index2] = "-"
            print(*lst)
        else:
            del lst[num_of_player2[0] - 1]
            lst.insert(num_of_player2[0] - 1, '-')
            del lst[num_of_player2[1] - 1]
            lst.insert(num_of_player2[1] - 1, '-')
            print(*lst)
        if lst == emp_lst:
            print("player 2 won")
            exit()
    # if player2 enter 1 NUM
    else:
        if num_of_player2[0] > 10 and num_of_player2[0] != 20:
            lst.reverse()
            num_of_player2[0] -= 10
            index = lst.index(num_of_player2[0])
            lst[index] = "-"
            lst.reverse()
            print(*lst)
        else:
            del lst[num_of_player2[0] - 1]
            lst.insert(num_of_player2[0] - 1, '-')
            print(*lst)
        if lst == emp_lst:
            print("Player 2 won !")
            exit()


