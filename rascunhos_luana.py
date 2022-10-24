import curses
import ctypes
import random
from curses.textpad import Textbox, rectangle
from random import shuffle, randrange
import math
import time

    discos = [ { "img":"@1", "x":0, "y":0, "ativo": False, "traj": {"A":0, "B": 0, "C": 0} },
           { "img":"@2", "x":0, "y":0, "ativo": False, "traj": {"A":0, "B": 0, "C": 0} },
           { "img":"@3", "x":0, "y":0, "ativo": False, "traj": {"A":0, "B": 0, "C": 0} },
           { "img":"@4", "x":0, "y":0, "ativo": False, "traj": {"A":0, "B": 0, "C": 0} } ]
p = int(4)

for i in range(3):
    p = int(i)+int(p)
    print(p)

            if (randrange(15) % len(discos) == 0 and intervalo < 0):
            intervalo = len(discos) + randrange(10)
            j = 0
            for disco in discos:
                if (not disco["ativo"]):
                    disco["ativo"] = True
                    disco["x"] = 10
                    disco["y"] = 15
                    disco["traj"]["C"] = disco["y"]
                    disco["traj"]["A"] = (max(-15, 4 - disco["traj"]["C"])) / ((200/2) * (200/2 - 200)) # 2 = y min
                    disco["traj"]["B"] = - disco["traj"]["A"] * 200

                    traj = disco["traj"]
                    break
                j += 1

        # apaga, move e desenha discos
        j = 0
        for disco in discos:
            # Apaga o disco
            stdscr.addstr(disco["x"],disco["y"], ' ')
            #console.gotoxy(disco["x"], disco["y"])
            #print("  ", end='')
            
            # Mostra os discos ativos:
            if disco["ativo"]:
                traj = disco["traj"]

                # Muda as posições do disco
                disco["x"] += 1    # Disco se move para direita
                disco["y"] = int(traj["A"]*disco["x"] + traj["C"])

                if disco["x"] >= 200:
                    disco["ativo"] = False
                else:
                    stdscr.addstr(disco["x"],disco["y"], 'OO')
                    #console.gotoxy(disco["x"], disco["y"])
                    #print(disco["img"], end='') # ou print("@" + chr(ord('1')+j), end='')

            j += 1


'''
LISTA=[]

for i in range(6):
    larg = 20+i
    LISTA.insert(i, larg)

print(LISTA[0])

lu = 1
at = [12,23,45,42,12,442]
a = len(at)

for y in range(len(at)):
    atl = at[y]

    if lu == atl:
        print("certo")
    elif lu != atl:
        pass

def cw():
    print(c)

cw()



int main( int argc, char ** argv ){
    char mesg[]="Digite uma mensagem: ";
    char str[80];

    int row,col;

    initscr();


    getmaxyx(stdscr,row,col);


    mvprintw(row/2,(col-strlen(mesg))/2,"%s",mesg);
    getstr(str);
    mvprintw(LINES - 2, 0, "Você digitou: %s", str);
    getch();
    endwin();

    return 0;
}


    ncols, nlines = 8, 3
    uly, ulx = 3, 2

    win = curses.newwin(nlines, ncols, uly, ulx)
    rectangle(stdscr, uly-1, ulx-1, uly + nlines, ulx + ncols)
    stdscr.refresh()

    box = Textbox(win)
    contents = box.edit()
    stdscr.addstr(uly+ncols+2, 0, "Text entered in the box\n")
    stdscr.addstr(repr(contents))
    stdscr.addstr('\n')
    stdscr.addstr('Press any key')
    stdscr.getch()

velocidade = 10
angulo = 17
gravidade = 9.8
tempo = 1

seno = math.sin(angulo)

if seno < 0:
    seno = -math.sin(angulo)

altura_maxima = math.ceil((velocidade*velocidade*seno*seno)/2*gravidade)
alcance = math.ceil(((velocidade*velocidade*seno*2)/gravidade))

print(altura_maxima)
print(alcance)
print(seno)


cw()



    for y in range(10):
        for x in range(25):
            stdscr.addstr(y+36,x+4,text, COR1)

    for y in range(15):
        for x in range(25):
            stdscr.addstr(y+31,x+29,text, COR1)

    for y in range(20):
        for x in range(25):
            stdscr.addstr(y+26,x+49,text, COR1)

    for y in range(10):
        for x in range(25):
            stdscr.addstr(y+36,x+69,text, COR1)

    for y in range(10):
        for x in range(25):
            stdscr.addstr(y+36,x+89,text, COR1)

    for y in range(10):
        for x in range(25):
            stdscr.addstr(y+36,x+109,text, COR1)

    for y in range(20):
        for x in range(25):
            stdscr.addstr(y+26,x+129,text, COR1)

    for y in range(20):
        for x in range(25):
            stdscr.addstr(y+26,x+149,text, COR1)

    for y in range(25):
        for x in range(25):
            stdscr.addstr(y+21,x+169,text, COR1)

    # resto
    for y in range(25):
        for x in range(19):
            stdscr.addstr(y+21,x+189,text, COR1)

        while 1:
        key = stdscr.getch()
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            direction = key

        head = bolinha[0]

        if direction == curses.KEY_RIGHT:
            new_head = [head[0], head[1]+1]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1]-1]
        elif direction == curses.KEY_UP:
            new_head = [head[0]-1, head[1]]
        elif direction == curses.KEY_DOWN:
            new_head = [head[0]+1, head[1]]

        bolinha.insert(0, new_head)
        stdscr.addstr(new_head[0], new_head[1], 'O')

        stdscr.addstr(bolinha[-1][0], bolinha[-1][1], ' ')
        bolinha.pop()
        stdscr.refresh()
'''
