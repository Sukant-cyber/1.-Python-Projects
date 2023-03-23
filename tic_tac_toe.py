#PLAYER CHOOSES X OR O
def player_choice():
    y='wrong'
    while y not in ['X','O']:
        y=input("Enter ur choice(X or O): ").upper()
        if y not in ['X','O']:
            print("Sorry! Invalid Input..")
    print("Player 1 is assigned '{}'".format(y))
    if y=='X':
        return 1
    else:
        return 2


#PRINT THE BOARD
def print_board(arr):
    # arr=[0,' ',' ',' ',' ',' ',' ',' ',' ',' ']
    # print('\n'*100)
    print('{}|{}|{}'.format(arr[7],arr[8],arr[9]))
    print('-----')
    print('{}|{}|{}'.format(arr[4],arr[5],arr[6]))
    print('-----')
    print('{}|{}|{}'.format(arr[1],arr[2],arr[3]))



#Defines whether the user wants to play further or not
def play_game():
    choice='Wrong'
    while choice not in ['Y','N']:
        choice=input("To start game press Y else N: ").upper()
        if choice not in ['Y','N']:
            print('Invalid Choice! ENter again...')
    return choice=='Y'



# game()
def main_game(arr):
    if [arr[4],arr[5],arr[6]]==['X','X','X']or[arr[1],arr[2],arr[3]]==['X','X','X']or[arr[7],arr[8],arr[9]]==['X','X','X']or[arr[1],arr[4],arr[7]]==['X','X','X']or[arr[2],arr[5],arr[8]]==['X','X','X']or[arr[3],arr[6],arr[9]]==['X','X','X']or[arr[7],arr[5],arr[3]]==['X','X','X']or[arr[1],arr[5],arr[9]]==['X','X','X']:
        x=1
        print("X Wins")
        return False
    elif  [arr[4],arr[5],arr[6]]==['O','O','O']or[arr[1],arr[2],arr[3]]==['O','O','O']or[arr[7],arr[8],arr[9]]==['O','O','O']or[arr[1],arr[4],arr[7]]==['O','O','O']or[arr[2],arr[5],arr[8]]==['O','O','O']or[arr[3],arr[6],arr[9]]==['O','O','O']or[arr[7],arr[5],arr[3]]==['O','O','O']or[arr[1],arr[5],arr[9]]==['O','O','O']:
        x=2
        print("O Wins")
        return False
    elif ' ' in arr:
        x=0
        return True
    else:
        x=3
        print('Its a Draw')
        return False
x=0

# arr=[0,' ',' ',' ',' ',' ',' ',' ',' ',' ']

#Start of the main part
print("Welcome to TIC TAC TOE Game!!")
while play_game()==True:
    arr=[0,' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print_board(arr)
    n=1
    if (player_choice()==1):


        while main_game(arr):
            loc=int(input("Enter the location:(1-9):"))
            if arr[loc]==' ':
                if not(1<=loc<=9):
                    print("Invalid Choice! Enter again...")
                elif n%2==1:
                    arr[loc]='X'
                    n+=1
                else:
                    arr[loc]='O'
                    n+=1
            else:
                print("This location was already taken! Enter another location!!")
                continue
            (print_board(arr))
    else:
        while main_game(arr):
            loc=int(input("Enter the location:(1-9): "))
            if not(1<=loc<=9):
                print("Invalid Choice! Enter again...")
            elif n%2==1:
                arr[loc]='O'
                n+=1
            else:
                arr[loc]='X'
                n+=1
            (print_board(arr))
else:
    print("Thanks for Playing!! ")



