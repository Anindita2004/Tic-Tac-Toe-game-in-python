x=set()
y=set()
b=[x,y]
win_con=({0,1,2},{3,4,5},{6,7,8},{0,4,8},{2,4,6},{0,3,6},{1,4,7},{2,5,8})
a=['']*10

def clear():
    for i in range(0,10):
        a[i]=i
        x.clear()
        y.clear()


def grid():
    for x in range(0,3):
        for y in range(0,3):
            if y==2:
                print(a[3*x+y],end='')
            else:
                 print(a[3*x+y],'|',end='')
        if x!=2:
            print('\n--+--+--')

def win():
    for i in range(0,2):
        if b[i] in win_con:
            return 1
    return 0

def play():
    i=0
    clear()
    while i<9:
        grid()
        t=int(input("\nPlayer 1 enters"))
        a[t]='X'
        x.add(t)
        if win()==1:
            print('Player 1 wins')
            break
        grid()
        t=int(input("\nPlayer 2 enters"))
        a[t]='0'
        y.add(t)
        if win()==1:
            print('Player 2 wins')
            break
        i+=2
    if win()==0:
        print("Tie")

    k=input('Play again?')
    if k=='y':
        play()

play()
