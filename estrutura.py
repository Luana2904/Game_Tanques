import curses
import ctypes
import random
from curses.textpad import Textbox, rectangle
from random import shuffle, randrange
import math
import time


# o x aumenta de 20 em 20 e o y é 49-valor da range
POSICAO_Y = random.randrange(10,25,5)
POSICAO_X = 28

#Define a posição da bolinha
if (POSICAO_Y == 10):
    BOLINHA = [[POSICAO_Y+23, 15]] #10,20,15
elif (POSICAO_Y == 15):
    BOLINHA = [[POSICAO_Y+13, 15]]
elif (POSICAO_Y == 20):
    BOLINHA = [[POSICAO_Y+3, 15]]

def telacheia():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    SW_MAXIMIZE = 3
    hWnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(hWnd, SW_MAXIMIZE)

def main(stdscr):
    telacheia()
    
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    box = [[3,3], [sh-3,sw-3]]
    win = curses.newwin(box[0][0], box[0][1], box[1][0], box[1][1])
    rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    
    #-------------------------COLUNAS E POSICAO INICIAL DA BOLA E PERSONAGEM---------------------------------

    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    COR1 = curses.color_pair(1)
    text = 'O'

    stdscr.addstr(BOLINHA[0][0], BOLINHA[0][1]-9, "OOOOOOO") #+"\n"+"()"+"\n"+"| |"

    SUPERFICIE_PREDIOS = []

    #Define a posição, altura e largura das colunas
    for i in range(1):
        for y in range(POSICAO_Y):
            for x in range(POSICAO_X):
                c = int(25)*int(i)
                alt = y+46-POSICAO_Y
                larg = x+4+c
                stdscr.addstr(alt, larg ,text ,COR1)
                SUPERFICIE_PREDIOS.insert(0, [alt, larg]) 

                #stdscr.addstr(y+47-posicao_y,x+25+c, '')
    
    for i in range(6):
        POSICAO_Y2 = random.randrange(10,25,5) 
        for y in range(POSICAO_Y2):
            for x in range(POSICAO_X):
                c = int(i)+1
                d = int(25)*int(i)+25
                alt = y+46-POSICAO_Y2
                larg = x+4+d
                stdscr.addstr(alt, larg, text, COR1)
                SUPERFICIE_PREDIOS.insert(c, larg)

                #stdscr.addstr(y+47-posicao_y,x+25+c, '')

    for i in range(1):
        POSICAO_Y3 = random.randrange(10,25,5)
        for y in range(POSICAO_Y3):
            for x in range(POSICAO_X):
                a = int(25)*int(i)+175
                alt = y+46-POSICAO_Y3
                larg = x+4+a
                stdscr.addstr(alt, larg ,text, COR1)
                SUPERFICIE_PREDIOS.insert(7, larg)

                #stdscr.addstr(y+47-posicao_y,x+25+c, '')

    if (POSICAO_Y3 == 10):
        BOLINHA2 = [[POSICAO_Y3+23, 200]] #10,20,15
    elif (POSICAO_Y3 == 15):
        BOLINHA2 = [[POSICAO_Y3+13, 200]]
    elif (POSICAO_Y3 == 20):
        BOLINHA2 = [[POSICAO_Y3+3, 200]]

    stdscr.addstr(BOLINHA2[0][0], BOLINHA2[0][1]-9, '0')
    stdscr.addstr(BOLINHA2[0][0], BOLINHA2[0][1]-5, "OOOOOOO")



    #--------------------------------TEXTBOX------------------------------
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_WHITE)
    COR = curses.color_pair(2)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    COR3 = curses.color_pair(3)

    while True:
        stdscr.addstr(1, 2, "Velocidade: ", COR3)
        stdscr.addstr(5, 2, "Angulo: ", COR3)

        editwin = curses.newwin(1, 20, 3, 3)
        stdscr.refresh()

        boxedit = Textbox(editwin)
        boxedit.edit()

        editwin2 = curses.newwin(1, 20, 8, 3)
        stdscr.refresh()

        boxedit2 = Textbox(editwin2)
        boxedit2.edit()

        velocidade = int(boxedit.gather())
        angulo = int(boxedit2.gather())
        gravidade = 9.8
        tempo = math.ceil((velocidade*velocidade)/2*gravidade)

        seno = math.sin(angulo)

        if seno < 0:
            seno = -math.sin(angulo)

        altura_maxima = math.ceil((velocidade*velocidade)/2*gravidade)
        alcance = math.ceil(((velocidade*velocidade*seno*2)/gravidade))
        aaa = math.ceil(alcance/2)

        px= BOLINHA[0][1] # 15 + 1 // 16, 17, 18, 19
        py= BOLINHA[0][0] # 23 - 1 // 22,

        for y in range(aaa):
            alt = py-y
            larg = px+y

            if alt > 0:
                stdscr.addstr(alt, larg, 'oo', COR)
                stdscr.refresh()
                time.sleep(0.2)
                stdscr.addstr(alt, larg, '  ')
            elif alt <= 0:
                pass

            #for y in range(alcance):
            #    stdscr.addstr(py, px+y, 'F')
        for y in range(aaa+1):
            alt = py+y-aaa
            larg = px+y+aaa
            
            if alt > 0:
                if larg < box[1][1]:
                    stdscr.addstr(alt-1, larg-1, '  ')
                    stdscr.addstr(alt, larg, 'FF',COR)
                    stdscr.refresh()
                    time.sleep(0.2)
            elif alt <= 0:
                if larg >= box[1][1]:
                    pass


        #----------------------------------------------------------------
        

        stdscr.getch()


    #--------------------------------------------------------------------
    stdscr.getch()



curses.wrapper(main)