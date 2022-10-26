import curses
from curses.textpad import Textbox, rectangle
import estrutura
import json
import time


menu = ["Jogar", "Ranking", "Sair"]


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    COR10 = curses.color_pair(6)
    h, w = stdscr.getmaxyx()
    x_ = w//2 - 3
    y_ = h//2 - 3
    stdscr.addstr(y_-2, x_, 'TANQUES', COR10)
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row) 
            stdscr.attroff(curses.color_pair(1))
        else:  
            stdscr.addstr(y, x, row) 

    stdscr.refresh()


def main_menu(stdscr):
    stdscr.clear()
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    COR9 = curses.color_pair(1)

    current_row_idx = 0
    
    print_menu(stdscr, current_row_idx)

    while 1:
        key = stdscr.getch()
        stdscr.clear()
        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu)-1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            if menu[current_row_idx] == "Jogar":
                h, w = stdscr.getmaxyx()
                x = w//2 - 3
                y = h//2 - 3
                stdscr.addstr(y, x-10, 'Digite o nome do usuário1:')
                USUARIO_1_WIN = curses.newwin(1, 20, y, x+27-10)
                stdscr.refresh()
                USUARIO_1_ENTRADA = Textbox(USUARIO_1_WIN)
                USUARIO_1_ENTRADA.edit()
                usuario1 = str(USUARIO_1_ENTRADA.gather())

                stdscr.addstr(y+1, x-10, 'Digite o nome do usuário2:')
                USUARIO_2_WIN = curses.newwin(1, 20, y+1, x+27-10)
                stdscr.refresh()
                USUARIO_2_ENTRADA = Textbox(USUARIO_2_WIN)
                USUARIO_2_ENTRADA.edit()
                usuario2 = str(USUARIO_2_ENTRADA.gather())

                stdscr.addstr(y+2, x-10, 'Digite o nível de dificuldade: facil ou dificil?')
                dificuldade_win = curses.newwin(1, 20, y+2, x+49-10)
                stdscr.refresh()
                dificuldade_entrada = Textbox(dificuldade_win)
                dificuldade_entrada.edit()
                dificuldade = str(dificuldade_entrada.gather())

                stdscr.addstr(y+3, x-10, 'Digite a quantidade de rodadas:')
                rodadas_win = curses.newwin(1, 20, y+3, x+32-10)
                stdscr.refresh()
                rodadas_entrada = Textbox(rodadas_win)
                rodadas_entrada.edit()
                rodadas = int(rodadas_entrada.gather())

                stdscr.addstr(y+4, x-10, 'Digite a gravidade:')
                gravidade_win = curses.newwin(1, 20, y+4, x+20-10)
                stdscr.refresh()
                gravidade_entrada = Textbox(gravidade_win)
                gravidade_entrada.edit()
                gravidade = float(gravidade_entrada.gather())

                stdscr.refresh()
                stdscr.getch()
                return usuario1, usuario2, dificuldade, rodadas, gravidade

                
            elif menu[current_row_idx] == "Ranking":
                stdscr.clear()
                h, w = stdscr.getmaxyx()
                x = w//2 - 3
                y = h//2 - 3                
                stdscr.addstr(y, x, "RANKING", COR9)
                stdscr.addstr(y+8, x-10, "AGUARDE PARA VOLTAR AO MENU", COR9)
                with open("informacao.json") as outfile:
                    data = json.load(outfile)
                if data[0]["pont"] > data[1]["pont"]:
                    stdscr.addstr(y+2 ,x-27, "Primeiro lugar: " + data[0]['nome'] + "com a pontuação: " + data[0]['pont'])
                    stdscr.addstr(y+3 ,x-27, "Segundo lugar: " + data[1]['nome'] + "com a pontuação: " + data[1]['pont'])
                if data[0]["pont"] < data[1]["pont"]:
                    stdscr.addstr(y+2 ,x-27, "Primeiro lugar: " + data[1]['nome'] + "com a pontuação: " + data[1]['pont'])
                    stdscr.addstr(y+3 ,x-27, "Segundo lugar: " + data[0]['nome'] + "com a pontuação: " + data[0]['pont'])
                if data[0]["pont"] == data[1]["pont"]:
                    stdscr.addstr(y+2 ,x-27, "Houve um empate entre: " + data[0]['nome'] + " e " + data[1]['nome'] + "com a pontuação: " + data[1]['pont'])
                stdscr.refresh()
                time.sleep(7)
                    
            elif menu[current_row_idx] == "Sair":
                break

        print_menu(stdscr, current_row_idx)
        
        stdscr.refresh()
