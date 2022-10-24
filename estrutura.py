import curses
import ctypes
import random
from curses.textpad import Textbox, rectangle
from random import shuffle, randrange
import math
import time
import menu
import cenarios

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
    niveil_dificuldade = ["facil ", "medio ", "dificil "]

    stdscr.clear()
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    #-------------------------COLUNAS E POSICAO INICIAL DA BOLA E PERSONAGEM---------------------------------

    if dificuldade == niveil_dificuldade[0]:
        PERSONAGEM_1_POSICAO, SUPERFICIE_PREDIOS, PERSONAGEM_2_POSICAO, BOLINHA, BOLINHA2, box = cenarios.main_cenario_facil(stdscr) 
    elif dificuldade == niveil_dificuldade[1]:
        PERSONAGEM_1_POSICAO, SUPERFICIE_PREDIOS, PERSONAGEM_2_POSICAO, BOLINHA, BOLINHA2, box = cenarios.main_cenario_medio(stdscr)
    elif dificuldade == niveil_dificuldade[2]:
        PERSONAGEM_1_POSICAO, SUPERFICIE_PREDIOS, PERSONAGEM_2_POSICAO, BOLINHA, BOLINHA2, box = cenarios.main_cenario_medio(stdscr)

    #----------------------------------------------------------------------------------------------------------

    JOGADOR = [usuario, usuario2]# fulano 1, fulaninho
    CONTADOR = 0
    PERDEU = 0
    RODADA = int(1)
    PONTOS = 5
    PONTUACAO_U_1 = int(0)
    PONTUACAO_U_2 = int(0)
    
    stdscr.addstr(4, 4, JOGADOR[0], COR3) 

    while True:
        stdscr.addstr(5, 4, "Velocidade:", COR2)
        stdscr.addstr(6, 4, "Angulo:", COR2)
        stdscr.addstr(7, 4, usuario + ": " + str(PONTUACAO_U_1), COR2)
        stdscr.addstr(8, 4, usuario2 + ": " + str(PONTUACAO_U_2), COR2)

        velocidade_win = curses.newwin(1, 20, 5, 15)
        stdscr.refresh()

        velocidade_entrada = Textbox(velocidade_win)
        velocidade_entrada.edit()

        angulo_win = curses.newwin(1, 20, 6, 11)
        stdscr.refresh()

        angulo_entrada = Textbox(angulo_win)
        angulo_entrada.edit()

        velocidade = int(velocidade_entrada.gather())
        angulo = int(angulo_entrada.gather())
        g = gravidade
        #tempo = math.ceil((velocidade*velocidade)/2*g)

        seno = math.sin(angulo)

        if seno < 0:
            seno = -math.sin(angulo)

        #altura_maxima = math.ceil((velocidade*velocidade)/2*g)
        alcance = math.ceil(((velocidade*velocidade*seno*2)/g))
        metade_alcance = math.ceil(alcance/2)

        #-------------------------------------------------------------

        px= BOLINHA[0][1]
        py= BOLINHA[0][0] 

        px2= BOLINHA2[0][1]-9
        py2= BOLINHA2[0][0]


        if JOGADOR[CONTADOR] == JOGADOR[0]:
            PERDEU_P = 0
            # SUBIDA JOGADOR 1 -------------------------------------------
            for y in range(metade_alcance):
                alt = py-y
                larg = px+y

                if dificuldade == niveil_dificuldade[0]:
                    if alt > 0:
                        stdscr.addstr(alt, larg, 'o', COR)
                        stdscr.addstr(alt, larg+1, 'o', COR)
                        stdscr.refresh()
                        time.sleep(0.1)
                        stdscr.addstr(alt, larg, '  ')
                    elif alt <= 0:
                        pass
                elif (dificuldade == niveil_dificuldade[2]) or (dificuldade == niveil_dificuldade[1]):
                    if alt > 0:
                        stdscr.addstr(alt, larg, 'o', COR)
                        stdscr.refresh()
                        time.sleep(0.1)
                        stdscr.addstr(alt, larg, ' ')
                    elif alt <= 0:
                        pass

            # DESCIDA JOGADOR 1 ----------------------------------------
            for y in range(metade_alcance+40):
                alt = py+y-metade_alcance
                larg = px+y+metade_alcance
                 
                if dificuldade == niveil_dificuldade[0]:
                    if alt > 0:
                        if larg < box[1][1]:
                            stdscr.addstr(alt, larg, 'o',COR)
                            stdscr.addstr(alt, larg+1, 'o', COR)
                            stdscr.refresh()
                            time.sleep(0.1)
                            stdscr.addstr(alt, larg, '  ')
                    elif alt <= 0:
                        if larg >= box[1][1]:
                            pass                      
                elif (dificuldade == niveil_dificuldade[2]) or (dificuldade == niveil_dificuldade[1]):
                    if alt > 0:
                        if larg < box[1][1]:
                            stdscr.addstr(alt, larg, 'o',COR)
                            stdscr.refresh()
                            time.sleep(0.1)
                            stdscr.addstr(alt, larg, ' ')
                    elif alt <= 0:
                        if larg >= box[1][1]:
                            pass  

                # COLISAO DA BOLINHA JOGADOR 1 COM A SUPERFICIE --------
                for c in range(len(SUPERFICIE_PREDIOS)):
                    superficie = SUPERFICIE_PREDIOS[c]
                    if dificuldade == niveil_dificuldade[0]:
                        if ([alt, larg] == superficie) or ([alt, larg+1] == superficie):
                            PERDEU_P = 1
                    elif (dificuldade == niveil_dificuldade[2]) or (dificuldade == niveil_dificuldade[1]):
                        if ([alt, larg] == superficie):
                            PERDEU_P = 1

                # COLISAO DA BOLINHA JOGADOR 1 COM O PERSONAGEM 2 --------
                for c in range(len(PERSONAGEM_2_POSICAO)):
                    posicao_jogador_2 = PERSONAGEM_2_POSICAO[c]
                    if [alt, larg] == posicao_jogador_2:
                        PONTUACAO_U_1 = int(PONTUACAO_U_1)+int(PONTOS)
                        if RODADA < rodadas:
                            if dificuldade == niveil_dificuldade[0]:
                                PERSONAGEM_1_POSICAO, SUPERFICIE_PREDIOS, PERSONAGEM_2_POSICAO, BOLINHA, BOLINHA2, box =cenarios.main_cenario_facil(stdscr) 
                                PERDEU_P = 1
                            elif dificuldade == niveil_dificuldade[1]:
                                PERSONAGEM_1_POSICAO, SUPERFICIE_PREDIOS, PERSONAGEM_2_POSICAO, BOLINHA, BOLINHA2, box =cenarios.main_cenario_medio(stdscr)
                                PERDEU_P = 1
                            elif dificuldade == niveil_dificuldade[2]:
                                PERSONAGEM_1_POSICAO, SUPERFICIE_PREDIOS, PERSONAGEM_2_POSICAO, BOLINHA, BOLINHA2, box =cenarios.main_cenario_medio(stdscr)
                                PERDEU_P = 1
                            RODADA = int(RODADA)+int(1)
                            break
                        elif RODADA == rodadas:
                            # QUANDO AS RODADAS ACABAREM
                            stdscr.clear()
                            sh, sw = stdscr.getmaxyx()
                            x_ = sw//2 
                            y_ = sh//2 
                            stdscr.addstr(y_, x_, str(usuario))
                            stdscr.addstr(y_+1, x_, "PONTUAÇÃO: ")
                            stdscr.addstr(y_+1, x_+11, str(PONTUACAO_U_1))
                            stdscr.addstr(y_+2, x_, str(usuario2))
                            stdscr.addstr(y_+3, x_, "PONTUAÇÃO: ")
                            stdscr.addstr(y_+3, x_+11, str(PONTUACAO_U_2))

                            key = stdscr.getch()
                            if key == curses.KEY_ENTER or key in [10, 13]:
                                stdscr.clear()
                                usuario, usuario2, dificuldade, rodadas, gravidade = menu.main_menu(stdscr) 
                                break
                        

                if PERDEU_P == 1:
                    break

            stdscr.addstr(4, 4, JOGADOR[1], COR4)
            CONTADOR = 1

        elif JOGADOR[CONTADOR] == JOGADOR[1]:
            PERDEU = 0
            # SUBIDA JOGADOR 2
            for y in range(metade_alcance):
                alt = py2-y
                larg = px2-y
                
                if dificuldade == niveil_dificuldade[0]:
                    if alt > 0:
                        stdscr.addstr(alt, larg, 'o', COR)
                        stdscr.addstr(alt, larg+1, 'o', COR)
                        stdscr.refresh()
                        time.sleep(0.1)
                        stdscr.addstr(alt, larg, '  ')
                    elif alt <= 0:
                        pass                
                elif (dificuldade == niveil_dificuldade[2]) or (dificuldade == niveil_dificuldade[1]):
                    if alt > 0:
                        stdscr.addstr(alt, larg, 'o', COR)
                        stdscr.refresh()
                        time.sleep(0.1)
                        stdscr.addstr(alt, larg, ' ')
                    elif alt <= 0:
                        pass                       

            # DESCIDA JOGADOR 2 ----------------------------------------
            for y in range(metade_alcance+40):
                alt = py2+y-metade_alcance
                larg = px2-y-metade_alcance

                if dificuldade == niveil_dificuldade[0]:
                    if alt > 0:
                        if larg > box[0][1]:
                            stdscr.addstr(alt, larg, 'o ',COR)
                            stdscr.addstr(alt, larg+1, 'o', COR)
                            stdscr.refresh()
                            time.sleep(0.1)
                            stdscr.addstr(alt, larg, '  ')
                    elif alt <= 0:
                        if larg <= box[0][1]:
                            pass 
                elif (dificuldade == niveil_dificuldade[2]) or (dificuldade == niveil_dificuldade[1]):
                    if alt > 0:
                        if larg > box[0][1]:
                            stdscr.addstr(alt, larg, 'o',COR)
                            stdscr.refresh()
                            time.sleep(0.1)
                            stdscr.addstr(alt, larg, ' ')
                        elif alt <= 0:
                            if larg <= box[0][1]:
                                pass 

                # COLISAO DA BOLINHA JOGADOR 2 COM A SUPERFICIE ----------------------------
                for c in range(len(SUPERFICIE_PREDIOS)):
                    superficie = SUPERFICIE_PREDIOS[c]
                    if dificuldade == niveil_dificuldade[0]:
                        if ([alt, larg] == superficie) or ([alt, larg+1] == superficie):
                            PERDEU = 1
                    elif (dificuldade == niveil_dificuldade[2]) or (dificuldade == niveil_dificuldade[1]):
                        if ([alt, larg] == superficie):
                            PERDEU = 1
                       
                # COLISAO DA BOLINHA JOGADOR 2 COM O PERSONAGEM 1 --------
                for c in range(len(PERSONAGEM_1_POSICAO)):
                    supercicie = PERSONAGEM_1_POSICAO[c]
                    if ([alt, larg] == supercicie):
                        PONTUACAO_U_2 = int(PONTUACAO_U_2)+int(PONTOS) 
                        if RODADA < rodadas:
                            stdscr.clear()
                            if dificuldade == niveil_dificuldade[0]:
                                PERSONAGEM_1_POSICAO, SUPERFICIE_PREDIOS, PERSONAGEM_2_POSICAO, BOLINHA, BOLINHA2, box =cenarios.main_cenario_facil(stdscr)
                                PERDEU = 1 
                            elif dificuldade == niveil_dificuldade[1]:
                                PERSONAGEM_1_POSICAO, SUPERFICIE_PREDIOS, PERSONAGEM_2_POSICAO, BOLINHA, BOLINHA2, box =cenarios.main_cenario_medio(stdscr)
                                PERDEU = 1
                            elif dificuldade == niveil_dificuldade[2]:
                                PERSONAGEM_1_POSICAO, SUPERFICIE_PREDIOS, PERSONAGEM_2_POSICAO, BOLINHA, BOLINHA2, box =cenarios.main_cenario_medio(stdscr)
                                PERDEU = 1
                            RODADA = int(RODADA)+int(1)
                            break
                        elif RODADA == rodadas:
                            # QUANDO AS RODADAS ACABAREM
                            stdscr.clear()
                            sh, sw = stdscr.getmaxyx()
                            x_ = sw//2 
                            y_ = sh//2 
                            stdscr.addstr(y_, x_, str(usuario))
                            stdscr.addstr(y_+1, x_, "PONTUAÇÃO: ")
                            stdscr.addstr(y_+1, x_+11, str(PONTUACAO_U_1))
                            stdscr.addstr(y_+2, x_, str(usuario2))
                            stdscr.addstr(y_+3, x_, "PONTUAÇÃO: ")
                            stdscr.addstr(y_+3, x_+11, str(PONTUACAO_U_2))

                            key = stdscr.getch()
                            if key == curses.KEY_ENTER or key in [10, 13]:
                                usuario, usuario2, dificuldade, rodadas, gravidade = menu.main_menu(stdscr) 
                                break
                        PERDEU = 1

                if PERDEU == 1:
                    break

            stdscr.addstr(4, 4, JOGADOR[0], COR3)
            CONTADOR = 0

        stdscr.getch()
    stdscr.getch()

curses.wrapper(main)