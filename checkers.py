import turtle
import time

wn=turtle.Screen()
wn.setup(height=600, width=600)
wn.tracer(0)

turn="black"

class Pen (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.shape("circle")
        self.color("black")
        self.speed(0)

w=Pen()
w.hideturtle()
pen=Pen()
pen.hideturtle()
marker=Pen()
marker.color("yellow")
marker.hideturtle()
marker.shapesize(stretch_wid=0.5, stretch_len=0.5)
bpen=Pen()
bpen.hideturtle()
wpen=Pen()
wpen.hideturtle()
wpen.color("blue")
bk=Pen()
bk.color("grey")
bk.hideturtle()
wk=Pen()
wk.color("lightblue")
wk.hideturtle()

y=300
for x in range (8):
    pen.penup()
    pen.goto(-300, y)
    pen.pendown()
    for j in range (8):
        for i in range (4):
            pen.forward(75)
            pen.right(90)
        pen.forward(75)
    y-=75




arr=[[0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]]

board=[[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0]]

def reverse_screen():
    global turn

    if turn=="black":
        turn="white"
    else:
        turn="black"
    board.reverse()
    for i in board:
        i.reverse()
    for i in board:
        print (i)
    update_screen()

def update_screen():
    over=True
    over2=True
    over1=True
    over12=True

    bpen.clear()
    for i in range (8):
        for j in range (8):
            if board[i][j]==1:
                bpen.goto((j-3.5)*75, ((i*-1)+3.5)*75)
                bpen.stamp()
                over=False
    
    wpen.clear()
    for i in range (8):
        for j in range (8):
            if board[i][j]==2:
                wpen.goto((j-3.5)*75, ((i*-1)+3.5)*75)
                wpen.stamp()
                over1=False
    bk.clear()
    for i in range (8):
        for j in range (8):
            if board[i][j]==3:
                bk.goto((j-3.5)*75, ((i*-1)+3.5)*75)
                bk.stamp()
                over2=False
    wk.clear()
    for i in range (8):
        for j in range (8):
            if board[i][j]==4:
                wk.goto((j-3.5)*75, ((i*-1)+3.5)*75)
                wk.stamp()
                over12=False

    if over==True and over2==True:
        winner("blues")

    elif over1==True and over12==True:
        winner("blacks")
    else:
        pass

def winner(team):
    w.goto(0, 0)
    w.write(f"{team} wins", align="center", font=("Calibri", 60))

    

update_screen()


def king_check():
    global turn
    if turn=="black":
        for i in range (8):
            if board[0][i]==1:
                board[0][i]=3

    elif turn=="white":
        for i in range (8):
            if board[0][i]==2:
                board[0][i]=4
    else:
        pass
    for i in board:
        print (i)
    update_screen()
    


def start(x, y):
    
    global row
    global col
    row=round((x/75)+3.5)
    col=round(((y*-1)/75)+3.5)
    marker.showturtle()
    marker.goto((row-3.5)*75, ((col*-1)+3.5)*75)
    wn.listen()
    wn.onscreenclick(get)
    


def get(x, y):
    global turn
    global row
    global col
    c_turn=0
    ck_turn=0
    if turn=="black":
        c_turn=1
        ck_turn=3
    elif turn=="white":
        c_turn=2
        ck_turn=4
    num=board[col][row]

    marker.hideturtle()
    row2=round((x/75)+3.5)
    col2=round(((y*-1)/75)+3.5)
    if num==1 or num==2:
        if col2==col-1 and (row+1==row2 or row-1==row2):#
            if board[col][row]==c_turn:#if they clicked their piece
                normal_move(col, row, col2, row2)
        elif col2==col-2 and (row+2==row2 or row-2==row2):
            if board[col][row]==c_turn:#if they clicked their piece
                take(col, row, col2, row2)

        else:
            pass

    elif num==3 or num==4:
        print ("3 or 4")
        if col2==col-1 and (row+1==row2 or row-1==row2) or (col2==col+1 and (row+1==row2 or row-1==row2)):
            if board[col][row]==ck_turn:
                k_normal(col, row, col2, row2)
        elif col2==col-2 and (row+2==row2 or row-2==row2) or col2==col+2 and (row+2==row2 or row-2==row2):
            if board[col][row]==ck_turn:#if they clicked their piece
                k_take(col, row, col2, row2)
            


    else:
        print ("not 1 or 2")

    


    
    
    lis()#waiting for another input from users
    
    
def normal_move(c, r, c2, r2):
    if board[c2][r2]==0:#if space is open
        board[c2][r2]=board[c][r]
        board[c][r]=0
        king_check()
        reverse_screen()
        
    else:
        lis()


def take(c, r, c2, r2):
    global turn
    if turn=="black":
        num1=2
        num2=4
    else:
        num1=1
        num2=3
    
    if board[int((c2+c)/2)][int((r+r2)/2)]==num1 or board[int((c2+c)/2)][int((r+r2)/2)]==num2:
        
        if board[c2][r2]==0:
            board[c2][r2]=board[c][r]
            board[c][r]=0
            board[int((c2+c)/2)][int((r+r2)/2)]=0
            c=c2
            r=r2
            rev=False
            try:
                if (board[c-2][r+2]==0 and (board[c-1][r+1]==num1)or(board[c-1][r+1]==num2)):
                    print ("tr")#if there is 2 takes in a row
                    rev=True

            except IndexError:
                pass
            try:
                if (board[c-2][r-2]==0 and (board[c-1][r-1]==num1 or board[c-1][r-1]==num2)):
                    print ("tl")
                    rev=True
                
            except IndexError:
                pass

            if c-2<0 or c-1<0:
                rev=False

            

                

            if rev==True:
                reverse_screen()
            king_check()
            reverse_screen()
    else:
        print ("f")
        
    
def k_normal(c, r, c2, r2):

    if board[c2][r2]==0:
        board[c2][r2]=board[c][r]
        board[c][r]=0
        reverse_screen()

def k_take(c, r, c2, r2):
    global turn
    if turn=="black":
        num1=2
        num2=4
    else:
        num1=1
        num2=3
    rev1=False
    rev2=False
    rev3=False
    rev4=False
    
        
    
    if board[int((c2+c)/2)][int((r+r2)/2)]==num1 or board[int((c2+c)/2)][int((r+r2)/2)]==num2:
        if board[c2][r2]==0:
            board[c2][r2]=board[c][r]
            board[c][r]=0
            board[int((c2+c)/2)][int((r+r2)/2)]=0
            c=c2
            r=r2
            print ("c", c, "r", r)
            try:
                if (board[c-2][r+2]==0 and (board[c-1][r+1]==num1) or (board[c-1][r+1]==num2)):
                    rev1=True
                    print("tr")
                    if c-2<0 or c-1<0:
                        rev1=False
                        
            except IndexError:
                pass

            try:
                if (board[c-2][r-2]==0 and (board[c-1][r-1]==num1) or (board[c-1][r-1]==num2)):
                    rev2=True
                    print ("tl")
                    if c-2<0 or c-1<0 or r-1<0 or r-2<0:
                        rev2=False
            except IndexError:
                pass

            try:
                if (board[c+2][r+2]==0 and (board[c+1][r+1]==num1) or (board[c+1][r+1]==num2)):
                    rev3=True
                    print ("br")
            except IndexError:
                pass

            try:
                if (board[c+2][r-2]==0 and (board[c+1][r-1]==num1) or (board[c+1][r-1]==num2)):
                    rev4=True
                    print ("bl")
                    if r-1<0 or r-2<0:
                        rev4=False
            except IndexError:
                pass

            if rev1==True or rev2==True or rev3==True or rev4==True:
                reverse_screen()
            

            

    reverse_screen()
        


def lis():
    wn.listen()
    wn.onscreenclick(start)
lis()

while True:
    wn.update()











