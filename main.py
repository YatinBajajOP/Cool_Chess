# 663300
# ffff99
# pawn = 1; bishop, knight = 3; rook = 5; queen = 9

import tkinter as tk
from PIL import ImageTk
import speech_recognition as sr
import pyttsx3
import numpy as np
import pywhatkit

root = tk.Tk()
root.title("Cool chess")

canvas = tk.Canvas(root, height=800, width=750)
canvas.pack()

frame = tk.Frame(canvas)
frame.place(relheight=1, relwidth=1, relx=0.1, rely=0.1)

king_black = kingb = ImageTk.PhotoImage(file="king.png")
queen_black = queenb = ImageTk.PhotoImage(file="queen.png")
rook_black = rookb = ImageTk.PhotoImage(file="rook.png")
pawn_black = pawnb = ImageTk.PhotoImage(file="pawn.png")
bishop_black = bishopb = ImageTk.PhotoImage(file="bishop.png")
knight_black = knightb = ImageTk.PhotoImage(file="knight.png")
king_white = kingw = ImageTk.PhotoImage(file="kingW.png")
queen_white = queenw = ImageTk.PhotoImage(file="queenW.png")
rook_white = rookw = ImageTk.PhotoImage(file="rookW.png")
pawn_white = pawnw = ImageTk.PhotoImage(file="pawnW.png")
bishop_white = bishopw = ImageTk.PhotoImage(file="bishopW.png")
knight_white = knightw = ImageTk.PhotoImage(file="knightW.png")

blackbg = ImageTk.PhotoImage(file="blackbg.png")
whitebg = ImageTk.PhotoImage(file="whitebg.png")

pieces_white = [pawn_white, knight_white, bishop_white, rook_white, queen_white]
pieces_black = [pawn_black, knight_black, bishop_black, rook_black, queen_black]

# handles in pos_handles
pos_handle = []
pos_handle = np.array(pos_handle)
for i in range(8):
    for j in range(8):
        pos_handle = np.append(pos_handle, whitebg)
pos_handle.resize(8, 8)
for i in range(8):
    for j in range(8):
        if i == 1:
            pos_handle[i][j] = pawnw
        elif i == 6:
            pos_handle[i][j] = pawnb
        elif i == 0 and (j == 0 or j == 7):
            pos_handle[i][j] = rookw
        elif i == 0 and (j == 1 or j == 6):
            pos_handle[i][j] = knightw
        elif i == 0 and (j == 2 or j == 5):
            pos_handle[i][j] = bishopw
        elif i == 0 and j == 3:
            pos_handle[i][j] = queenw
        elif i == 0 and j == 4:
            pos_handle[i][j] = kingw
        elif i == 7 and (j == 0 or j == 7):
            pos_handle[i][j] = rookb
        elif i == 7 and (j == 1 or j == 6):
            pos_handle[i][j] = knightb
        elif i == 7 and (j == 2 or j == 5):
            pos_handle[i][j] = bishopb
        elif i == 7 and j == 3:
            pos_handle[i][j] = queenb
        elif i == 7 and j == 4:
            pos_handle[i][j] = kingb
        elif i % 2 == 0:
            if j % 2 != 0:
                pos_handle[i][j] = blackbg
            else:
                pos_handle[i][j] = whitebg
        else:
            if j % 2 == 0:
                pos_handle[i][j] = blackbg
            else:
                pos_handle[i][j] = whitebg

frame_white = tk.Frame(canvas, bg="silver")
frame_white.place(relx=0.1, rely=0.014, relwidth=0.8, relheight=0.05)
entry_white = tk.Entry(frame_white)
entry_white.place(relx=0.01, rely=0.05, relwidth=0.2, relheight=00.9)
button_white = tk.Button(frame_white, text="Speak", command=lambda: white_move())
button_white.place(relx=0.25, rely=0.05, relwidth=0.2, relheight=0.9)
resign_white = tk.Button(frame_white, text="Resign")
resign_white.place(relx=0.5, rely=0.05, relwidth=0.2, relheight=0.9)
points_white = tk.Label(frame_white, text='0')
points_white.place(relx=0.8, rely=0.05, relwidth=0.195, relheight=0.9)

frame_black = tk.Frame(canvas, bg="silver")
frame_black.place(relx=0.1, rely=0.88, relwidth=0.8, relheight=0.05)
entry_black = tk.Entry(frame_black)
entry_black.place(relx=0.01, rely=0.05, relwidth=0.2, relheight=00.9)
button_black = tk.Button(frame_black, text="Speak", command=lambda: black_move())
button_black.place(relx=0.25, rely=0.05, relwidth=0.2, relheight=0.9)
resign_black = tk.Button(frame_black, text="Resign")
resign_black.place(relx=0.5, rely=0.05, relwidth=0.2, relheight=0.9)
points_black = tk.Label(frame_black, text='0')
points_black.place(relx=0.8, rely=0.05, relwidth=0.195, relheight=0.9)

frame_numbersL = tk.Frame(canvas)
frame_numbersL.place(relx=0.06, rely=0.1, relwidth=0.03, relheight=0.95)
frame_alphasT = tk.Frame(canvas)
frame_alphasT.place(relx=0.1, rely=0.065, relwidth=0.95, relheight=0.04)

frame_numbersR = tk.Frame(canvas)
frame_numbersR.place(relx=0.9, rely=0.1, relwidth=0.03, relheight=0.95)
frame_alphasB = tk.Frame(canvas)
frame_alphasB.place(relx=0.1, rely=0.835, relwidth=0.95, relheight=0.04)

for i in range(8):
    tk.Label(frame_numbersL, text=i + 1, height=3, width=2).grid(row=i, column=0, pady=4)

for i in range(8):
    tk.Label(frame_alphasT, text=chr(104 - i), height=2, width=8).grid(row=0, column=i, padx=2)

for i in range(8):
    tk.Label(frame_numbersR, text=i + 1, height=3, width=2).grid(row=i, column=0, pady=4)

for i in range(8):
    tk.Label(frame_alphasB, text=chr(104 - i), height=2, width=8).grid(row=0, column=i, padx=2)

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 != 0:
                tk.Label(frame, image=blackbg, height=70, width=70).grid(row=i, column=j)
            else:
                tk.Label(frame, image=whitebg, height=70, width=70).grid(row=i, column=j)
        else:
            if j % 2 == 0:
                tk.Label(frame, image=blackbg, height=70, width=70).grid(row=i, column=j)
            else:
                tk.Label(frame, image=whitebg, height=70, width=70).grid(row=i, column=j)

# setting up the chess pieces in the grid
for i in range(8):
    for j in range(8):
        if i == 1:
            tk.Label(frame, image=pawnw, relief='sunken').grid(row=i, column=j)
        elif i == 6:
            tk.Label(frame, image=pawnb, relief='sunken').grid(row=i, column=j)
        elif i == 0 and (j == 0 or j == 7):
            tk.Label(frame, image=rookw, relief='sunken').grid(row=i, column=j)
        elif i == 0 and (j == 1 or j == 6):
            tk.Label(frame, image=knightw, relief='sunken').grid(row=i, column=j)
        elif i == 0 and (j == 2 or j == 5):
            tk.Label(frame, image=bishopw, relief='sunken').grid(row=i, column=j)
        elif i == 0 and j == 3:
            tk.Label(frame, image=queenw, relief='sunken').grid(row=i, column=j)
        elif i == 0 and j == 4:
            tk.Label(frame, image=kingw, relief='sunken').grid(row=i, column=j)
        elif i == 7 and (j == 0 or j == 7):
            tk.Label(frame, image=rookb, relief='sunken').grid(row=i, column=j)
        elif i == 7 and (j == 1 or j == 6):
            tk.Label(frame, image=knightb, relief='sunken').grid(row=i, column=j)
        elif i == 7 and (j == 2 or j == 5):
            tk.Label(frame, image=bishopb, relief='sunken').grid(row=i, column=j)
        elif i == 7 and j == 3:
            tk.Label(frame, image=queenb, relief='sunken').grid(row=i, column=j)
        elif i == 7 and j == 4:
            tk.Label(frame, image=kingb, relief='sunken').grid(row=i, column=j)


# updating the pos_handle
def update_pos_handle(lst):
    ci, ri, cf, rf = [i for i in lst]
    if ri % 2 == 0:
        if ci % 2 != 0:
            piece2 = blackbg
        else:
            piece2 = whitebg
    else:
        if ci % 2 == 0:
            piece2 = blackbg
        else:
            piece2 = whitebg
    set_points(pos_handle[rf][cf])
    pos_handle[rf][cf] = pos_handle[ri][ci]
    pos_handle[ri][ci] = piece2
    return [pos_handle[rf][cf], pos_handle[ri][ci], ci, ri, cf, rf]


def points_b(target):
    point = int(points_black['text'])
    pts = [1, 3, 3, 5, 9]
    if target in pieces_white:
        point = pts[pieces_white.index(target)]
    return point


def points_w(target):
    point = int(points_white['text'])
    pts = [1, 3, 3, 5, 9]
    if target in pieces_black:
        point = pts[pieces_black.index(target)]
    return point


def set_points(target):
    value = points_w(target) - points_b(target)
    if value > 0:
        points_white['text'] = value
        points_black['text'] = 0
    elif value < 0:
        points_white['text'] = 0
        points_black['text'] = abs(value)


# Doing all the pawn promotion stuff

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Queen


def pawn_promotion(position):
    frame1 = tk.Frame(canvas)
    frame1.place(relheight=0.4, relwidth=0.4, relx=0.5, rely=0.1)

    pieces = [("Queen", 101),
              ("Rook", 102),
              ("Bishop", 103),
              ("Knight", 104)]

    tk.Label(frame1,
             text="What do you want to make your pawn:",
             justify=tk.LEFT,
             padx=20).pack()

    def setChoice():
        ci, ri, cf, rf = [i for i in position]

        choice = v.get()
        if rf == 0:
            if choice == 101:
                pos_handle[rf][cf] = queenb
            elif choice == 102:
                pos_handle[rf][cf] = rookb
            elif choice == 103:
                pos_handle[rf][cf] = bishopb
            elif choice == 104:
                pos_handle[rf][cf] = knightb
        else:
            if choice == 101:
                pos_handle[rf][cf] = queenw
            elif choice == 102:
                pos_handle[rf][cf] = rookw
            elif choice == 103:
                pos_handle[rf][cf] = bishopw
            elif choice == 104:
                pos_handle[rf][cf] = knightw
        tk.Label(frame, image=pos_handle[rf][cf], relief='sunken').grid(row=rf, column=cf)
        frame1.destroy()

    for piece, val in pieces:
        tk.Radiobutton(frame1,
                       text=piece,
                       padx=20,
                       variable=v,
                       command=setChoice,
                       value=val).pack(anchor=tk.W)


# def castling_check(position):
#     ci, ri, cf, rf = [i for i in position]
#     if


# move validation of pieces
def move_validators(position):
    ci, ri, cf, rf = [i for i in position]
    initial = pos_handle[ri][ci]
    target = pos_handle[rf][cf]
    flag = True

    # for avoiding out of range situation
    if (7 < ri or ri < 0) and (7 < rf or rf < 0) and (7 < ci or ci < 0) and (7 < cf or cf < 0):
        flag = False
    elif ci == cf and ri == rf:  # for avoiding not actually moving the target.
        flag = False
    elif initial == blackbg or initial == whitebg:
        flag = False

    # for not capturing their own pieces.
    elif (True in [initial == i for i in pieces_white]) and (True in [target == i for i in pieces_white]):
        flag = False
    elif (True in [initial == i for i in pieces_black]) and (True in [target == i for i in pieces_black]):
        flag = False

    # validator for white pawn
    elif initial == pawn_white:
        if target != blackbg and target != whitebg:
            if ((cf == ci + 1) or (cf == ci - 1) or (cf == ci)) and rf == 7:
                pawn_promotion(position)
                flag = True
            elif ((cf == ci + 1) or (cf == ci - 1) or (cf == ci)) and (
                    (ri == 1 and 1 <= rf <= ri + 2) or (ri != 1 and rf == ri + 1)):
                flag = True
            else:
                flag = False
        else:
            if (cf == ci) and rf == 7:
                pawn_promotion(position)
                flag = True
            elif (cf == ci) and ((ri == 1 and 1 <= rf <= ri + 2) or (ri != 1 and rf == ri + 1)):
                flag = True
            else:
                flag = False

    # validator for black pawn
    elif initial == pawn_black:
        if target != blackbg and target != whitebg:
            if ((cf == ci + 1) or (cf == ci - 1) or (cf == ci)) and rf == 0:
                pawn_promotion(position)
                flag = True
            elif ((cf == ci + 1) or (cf == ci - 1) or (cf == ci)) and ((ri == 6 and 4 <= rf < 7) or (
                    ri != 6 and rf == ri - 1)):
                flag = True
            else:
                flag = False
        else:
            if (cf == ci) and rf == 0:
                pawn_promotion(position)
                flag = True
            elif (cf == ci) and ((ri == 6 and 4 <= rf < 7) or (ri != 6 and rf == ri - 1)):
                flag = True
            else:
                flag = False

    # validator for black rook
    elif initial == rook_black or initial == rook_white:
        if cf == ci:
            if ri > rf:
                for i in range(ri - 1, rf, -1):
                    if pos_handle[i][ci] != blackbg and pos_handle[i][ci] != whitebg:
                        flag = False
            else:
                for i in range(ri + 1, rf):
                    if pos_handle[i][ci] != blackbg and pos_handle[i][ci] != whitebg:
                        flag = False
        elif rf == ri:
            if ci > cf:
                for i in range(ci - 1, cf, -1):
                    if pos_handle[ri][i] != blackbg and pos_handle[ri][i] != whitebg:
                        flag = False
            else:
                for i in range(ci + 1, cf):
                    if pos_handle[ri][i] != blackbg and pos_handle[ri][i] != whitebg:
                        flag = False
        else:
            flag = False

    # move validator for black bishop
    elif initial == bishop_black or initial == bishop_white:
        if cf == ci or rf == ri:
            flag = False
        j = ci
        if rf > ri:
            for i in range(ri + 1, rf):
                if cf > ci:
                    j = j + 1
                    if pos_handle[i][j] != blackbg and pos_handle[i][j] != whitebg:
                        flag = False
                else:
                    j = j - 1
                    if pos_handle[i][j] != blackbg and pos_handle[i][j] != whitebg:
                        flag = False
        else:
            for i in range(ri - 1, rf, -1):
                if cf > ci:
                    j = j + 1
                    if pos_handle[i][j] != blackbg and pos_handle[i][j] != whitebg:
                        flag = False
                else:
                    j = j - 1
                    if pos_handle[i][j] != blackbg and pos_handle[i][j] != whitebg:
                        flag = False

    # move validator for king
    elif initial == king_black or initial == king_white:
        if ci - 1 <= cf <= ci + 1 and ri - 1 <= rf <= ri + 1:
            flag = True
        else:
            flag = False

    # move validator for queen
    elif initial == queen_white or initial == queen_black:
        if cf == ci:
            if ri > rf:
                for i in range(ri - 1, rf, -1):
                    if pos_handle[i][ci] != blackbg and pos_handle[i][ci] != whitebg:
                        flag = False
            else:
                for i in range(ri + 1, rf):
                    if pos_handle[i][ci] != blackbg and pos_handle[i][ci] != whitebg:
                        flag = False
        elif rf == ri:
            if ci > cf:
                for i in range(ci - 1, cf, -1):
                    if pos_handle[ri][i] != blackbg and pos_handle[ri][i] != whitebg:
                        flag = False
            else:
                for i in range(ci + 1, cf):
                    if pos_handle[ri][i] != blackbg and pos_handle[ri][i] != whitebg:
                        flag = False
        else:
            j = ci
            if rf > ri:
                for i in range(ri + 1, rf):
                    if cf > ci:
                        j = j + 1
                        if pos_handle[i][j] != blackbg and pos_handle[i][j] != whitebg:
                            flag = False
                    else:
                        j = j - 1
                        if pos_handle[i][j] != blackbg and pos_handle[i][j] != whitebg:
                            flag = False
            else:
                for i in range(ri - 1, rf, -1):
                    if cf > ci:
                        j = j + 1
                        if pos_handle[i][j] != blackbg and pos_handle[i][j] != whitebg:
                            flag = False
                    else:
                        j = j - 1
                        if pos_handle[i][j] != blackbg and pos_handle[i][j] != whitebg:
                            flag = False

    # move validator for knight
    elif initial == knight_black or knight_white:
        if (cf == ci + 2 and (rf == ri - 1 or rf == ri + 1)) or (cf == ci - 2 and (rf == ri - 1 or rf == ri + 1)) or (
                rf == ri + 2 and (cf == ci - 1 or cf == ci + 1)) or (rf == ri - 2 and (cf == ci - 1 or cf == ci + 1)):
            flag = True
        else:
            flag = False
    if flag:
        move(position)
    else:
        invalid_move()
        print("Invalid move!")


# highlighting "invalid move" in front of the screen
def invalid_move():
    highlight_frame = tk.Frame(frame)
    highlight_frame.place(rely=0.4, relheight=0.15, relwidth=1)
    highlight_label = tk.Label(highlight_frame, text="Invalid Move!", font=40, bg='silver', fg='red')
    highlight_label.place(relheight=1, relwidth=1)
    highlight_frame.after(2000, highlight_frame.destroy)  # after 2 sec, destroy the frame.


def move(position):
    piece, piece2, ci, ri, cf, rf = [i for i in update_pos_handle(position)]
    tk.Label(frame, image=piece2).grid(row=ri, column=ci)
    tk.Label(frame, image=piece, relief='sunken').grid(row=rf, column=cf)
    print(piece, piece2)


listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk('listening...')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'move' in command:
                command = command.replace('move', '')
            elif 'mov' in command:
                command = command.replace('mov', '')
            elif 'moon' in command:
                command = command.replace('moon', '')
            elif 'moov' in command:
                command = command.replace('moov', '')
            elif 'moove' in command:
                command = command.replace('moove', '')
            elif 'more' in command:
                command = command.replace('more', '')
    except:
        pass
    return command.strip()


def set_move(command):
    lst = command.split(" ")
    print(lst)

    c1 = lst[0][:1]
    r1 = lst[1]
    c2 = lst[2][:1]
    r2 = lst[3]

    # setting value of r1
    if r1 == 'one':
        r1 = 0
    elif r1 == 'to' or r1 == 'tu' or r1 == 'two':
        r1 = 1
    elif r1 == 'three':
        r1 = 2
    elif r1 == 'for' or r1 == 'four' or r1 == 'fore':
        r1 = 3
    elif r1 == 'five' or r1 == 'v':
        r1 = 4
    elif r1 == 'six' or r1 == 'sex':
        r1 = 5
    elif r1 == 'seven':
        r1 = 6
    elif r1 == 'ate' or r1 == 'eat':
        r1 = 7
    else:
        r1 = int(r1) - 1

    # setting value of r2
    if r2 == 'one':
        r2 = 0
    elif r2 == 'to' or r2 == 'tu':
        r2 = 1
    elif r2 == 'three':
        r2 = 2
    elif r2 == 'for' or r2 == 'four' or r2 == 'fore':
        r2 = 3
    elif r2 == 'five' or r2 == 'v':
        r2 = 4
    elif r2 == 'six' or r2 == 'sex':
        r2 = 5
    elif r2 == 'seven':
        r2 = 6
    elif r2 == 'ate' or r2 == 'eat':
        r2 = 7
    else:
        r2 = int(r2) - 1

    # setting value of c1
    if c1 == 'a':
        c1 = 7
    elif c1 == 'b':
        c1 = 6
    elif c1 == 'c':
        c1 = 5
    elif c1 == 'd':
        c1 = 4
    elif c1 == 'e':
        c1 = 3
    elif c1 == 'f':
        c1 = 2
    elif c1 == 'g':
        c1 = 1
    elif c1 == 'h':
        c1 = 0

    # setting value of c2
    if c2 == 'a':
        c2 = 7
    elif c2 == 'b':
        c2 = 6
    elif c2 == 'c':
        c2 = 5
    elif c2 == 'd':
        c2 = 4
    elif c2 == 'e':
        c2 = 3
    elif c2 == 'f':
        c2 = 2
    elif c2 == 'g':
        c2 = 1
    elif c2 == 'h':
        c2 = 0
    return [c1, r1, c2, r2]


def black_move():
    talk("Black's move")
    cmd = take_command()
    print(cmd)
    lst = set_move(cmd)
    print(lst)
    move_validators(lst)


def white_move():
    talk("White's move")
    cmd = take_command()
    print(cmd)
    lst = set_move(cmd)
    print(lst)
    move_validators(lst)


# testing
# move([0, 6, 0, 1])
# move([0, 0, 3, 3])
# move_validators([0, 0, 0, 3])
# move_validators([0, 1, 0, 0])

root.mainloop()
