import curses
import ctypes
import random
from curses.textpad import Textbox, rectangle
from random import shuffle, randrange
import math
import time


SUPERFICIE_PREDIOS=[]

def main(stdscr):
    for i in range(1):
        POSICAO_Y3 = random.randrange(10,25,5)
        for y in range(POSICAO_Y3):
            for x in range(28):
                a = int(25)*int(i)+175
                alt = y+46-POSICAO_Y3
                larg = x+4+a
                stdscr.addstr(alt, larg ,"0")
        SUPERFICIE_PREDIOS.insert(y, [alt, larg])
        


curses.wrapper(main)

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
