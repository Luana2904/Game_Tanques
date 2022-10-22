import curses
import ctypes
import random
from curses.textpad import Textbox, rectangle
from random import shuffle, randrange
import math

begin_x = 20
begin_y = 7
height = 20
width = 15

def colunas(stdscr):
    e = e


def boneco(stdscr):
    e=e

def entradas(stdscr):
    #-------------------------TEXTBOX---------------------------------
    entradas_win = curses.newwin(3, 18, 2, 2)
    entradas_box = Textbox(entradas_win)

    rectangle(stdscr, 1, 1, 5, 20)

    

def telacheia():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    SW_MAXIMIZE = 3
    hWnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(hWnd, SW_MAXIMIZE)

def main(stdscr):
    telacheia()

    curses.curs_set(0)
    stdscr.clear()

    sh, sw = stdscr.getmaxyx()
    box = [[3,3], [sh-3,sw-3]]
    win = curses.newwin(box[0][0], box[0][1], box[1][0], box[1][1])
    rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    
    #-------------------------COLUNAS E POSICAO INICIAL DA BOLA E PERSONAGEM---------------------------------
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    COR1 = curses.color_pair(1)
    text = 'O'

    # o x aumenta de 20 em 20 e o y é 49-valor da range
    posicao_y = random.randrange(10,25,5)
    posicao_x = 28

    #Define a posição da bolinha
    if (posicao_y == 10):
        bolinha = [[posicao_y+23, 15]] #10,20,15
    elif (posicao_y == 15):
        bolinha = [[posicao_y+13, 15]]
    elif (posicao_y == 20):
        bolinha = [[posicao_y+3, 15]]       
    
    
    stdscr.addstr(bolinha[0][0], bolinha[0][1], '0')
    stdscr.addstr(bolinha[0][0], bolinha[0][1]-9, "OOOOOOO") #+"\n"+"()"+"\n"+"| |"


    #Define a posição, altura e largura das colunas
    for i in range(8):
        for y in range(posicao_y):
            for x in range(posicao_x):
                c = int(25)*int(i)
                stdscr.addstr(y+46-posicao_y,x+4+c,text, COR1)
                #stdscr.addstr(y+47-posicao_y,x+25+c, '')
        posicao_y = random.randrange(10,25,5)

    #-------------------------------LANÇAMENTO----------------------------
    velocidade = 10
    angulo = 10
    gravidade = 9.8
    tempo = 1

    seno = math.sin(angulo)

    if seno < 0:
        seno = -math.sin(angulo)

    altura_maxima = math.ceil((velocidade*velocidade)/2*gravidade)
    alcance = math.ceil(((velocidade*velocidade)*seno*2)/gravidade)

    px= bolinha[0][1] # 15 + 1 // 16, 17, 18, 19
    py= bolinha[0][0] # 23 - 1 // 22,

    for y in range(alcance):
        stdscr.addstr(py-y, px+y, 'o')

    

    #--------------------------------------------------------------------
    direction = 0



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



    stdscr.getch()


curses.wrapper(main)