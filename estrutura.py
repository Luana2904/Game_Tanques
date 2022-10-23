import curses
import ctypes
import random
from curses.textpad import Textbox, rectangle
from random import shuffle, randrange
import math
import time
import menu
import cenario
import game_over

def telacheia():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    SW_MAXIMIZE = 3
    hWnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(hWnd, SW_MAXIMIZE)

def main(stdscr):
    #--------------------------CORES----------------------------------
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_WHITE)
    COR = curses.color_pair(2)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    COR2 = curses.color_pair(3)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_RED)
    COR3 = curses.color_pair(4)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLUE)
    COR4 = curses.color_pair(5)
    #-----------------------------------------------------------------


    telacheia()
    usuario, usuario2, dificuldade, rodadas, gravidade = menu.main_menu(stdscr) 
    stdscr.clear()
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    #-------------------------COLUNAS E POSICAO INICIAL DA BOLA E PERSONAGEM---------------------------------

    PERSONAGEM_1_POSICAO, SUPERFICIE_PREDIOS, PERSONAGEM_2_POSICAO, BOLINHA, BOLINHA2 = cenario.main_cenario(stdscr) 

    #--------------------------------TEXTBOX------------------------------


    JOGADOR = [usuario, usuario2]
    CONTADOR = 0
    PERDEU = 0
    RODADA = int(0)
    PONTOS = 5
    PONTUACAO_U_1 = int(0)
    PONTUACAO_U_2 = int(0)
    
    stdscr.addstr(4, 4, JOGADOR[0], COR3)

    while True:
        stdscr.addstr(5, 4, "Velocidade:", COR2)
        stdscr.addstr(6, 4, "Angulo:", COR2)

        editwin = curses.newwin(1, 20, 5, 15)
        stdscr.refresh()

        boxedit = Textbox(editwin)
        boxedit.edit()

        editwin2 = curses.newwin(1, 20, 6, 11)
        stdscr.refresh()

        boxedit2 = Textbox(editwin2)
        boxedit2.edit()

        velocidade = int(boxedit.gather())
        angulo = int(boxedit2.gather())
        g = gravidade
        tempo = math.ceil((velocidade*velocidade)/2*g)

        seno = math.sin(angulo)

        if seno < 0:
            seno = -math.sin(angulo)

        altura_maxima = math.ceil((velocidade*velocidade)/2*g)
        alcance = math.ceil(((velocidade*velocidade*seno*2)/g))
        metade_alcance = math.ceil(alcance/2)

        px= BOLINHA[0][1] # 15 + 1 // 16, 17, 18, 19
        py= BOLINHA[0][0] # 23 - 1 // 22,

        px2= BOLINHA2[0][1]-9
        py2= BOLINHA2[0][0]

        if JOGADOR[CONTADOR] == JOGADOR[0]:
            PERDEU_P = 0
            for y in range(metade_alcance):
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
            for y in range(metade_alcance+40):
                alt = py+y-metade_alcance
                larg = px+y+metade_alcance
            
                if alt > 0:
                    if larg < box[1][1]:
                        stdscr.addstr(alt, larg, 'oo',COR)
                        stdscr.refresh()
                        time.sleep(0.1)
                        stdscr.addstr(alt, larg, '  ')
                elif alt <= 0:
                    if larg >= box[1][1]:
                        pass

                for c in range(len(SUPERFICIE_PREDIOS)):
                    ff = SUPERFICIE_PREDIOS[c]
                    if [alt, larg] == ff:
                        PERDEU_P = 1
                       

                for c in range(len(PERSONAGEM_2_POSICAO)):
                    a = PERSONAGEM_2_POSICAO[c]
                    if [alt, larg] == a:
                        PONTUACAO_U_1 = int(PONTUACAO_U_1)+int(PONTOS)
                        if RODADA < rodadas:
                            stdscr.clear()
                            cenario.main_cenario(stdscr) 
                            RODADA = int(RODADA)+int(1)
                        elif RODADA == rodadas:
                            game_over.main_game_over(stdscr)
                        stdscr.refresh()
                        PERDEU_P = 1

                if PERDEU_P == 1:
                    break

            stdscr.addstr(4, 4, JOGADOR[1], COR4)
            CONTADOR = 1

        elif JOGADOR[CONTADOR] == JOGADOR[1]:
            PERDEU = 0
            for y in range(metade_alcance):
                alt = py2-y
                larg = px2-y

                if alt > 0:
                    stdscr.addstr(alt, larg, 'oo', COR)
                    stdscr.refresh()
                    time.sleep(0.2)
                    stdscr.addstr(alt, larg, '  ')
                elif alt <= 0:
                    pass

                #for y in range(alcance):
                #    stdscr.addstr(py, px+y, 'F')
            for y in range(metade_alcance+40):
                alt = py2+y-metade_alcance
                larg = px2-y-metade_alcance
            
                if alt > 0:
                    if larg > box[0][1]:
                        stdscr.addstr(alt, larg, 'FF',COR)
                        stdscr.refresh()
                        time.sleep(0.1)
                        stdscr.addstr(alt, larg, '  ')
                elif alt <= 0:
                    if larg <= box[0][1]:
                        pass         

                for c in range(len(SUPERFICIE_PREDIOS)):
                    ff = SUPERFICIE_PREDIOS[c]
                    if [alt, larg] == ff:
                        PERDEU = 1
                       

                for c in range(len(PERSONAGEM_1_POSICAO)):
                    a = PERSONAGEM_1_POSICAO[c]
                    if [alt, larg] == a:
                        PONTUACAO_U_2 = int(PONTUACAO_U_2)+int(PONTOS) 
                        if RODADA < rodadas:
                            stdscr.clear()
                            cenario.main_cenario(stdscr) 
                            RODADA = int(RODADA)+int(1)
                        elif RODADA == rodadas:
                            game_over.main_game_over(stdscr)

                        stdscr.refresh()
                        PERDEU = 1

                if PERDEU == 1:
                    break

            stdscr.addstr(4, 4, JOGADOR[0], COR3)
            CONTADOR = 0

        

        stdscr.getch()
    stdscr.getch()

curses.wrapper(main)