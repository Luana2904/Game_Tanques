import curses
from curses.textpad import Textbox, rectangle



menu = ["Jogar", "Ranking", "Sair"]

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
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
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)

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
                stdscr.addstr(y, x, 'Digite o nome do usuário1:')
                USUARIO_1_WIN = curses.newwin(1, 20, y, x+27)
                stdscr.refresh()
                USUARIO_1_ENTRADA = Textbox(USUARIO_1_WIN)
                USUARIO_1_ENTRADA.edit()
                usuario1 = str(USUARIO_1_ENTRADA.gather())

                stdscr.addstr(y+1, x, 'Digite o nome do usuário2:')
                USUARIO_2_WIN = curses.newwin(1, 20, y+1, x+27)
                stdscr.refresh()
                USUARIO_2_ENTRADA = Textbox(USUARIO_2_WIN)
                USUARIO_2_ENTRADA.edit()
                usuario2 = str(USUARIO_2_ENTRADA.gather())

                stdscr.addstr(y+2, x, 'Digite o nível de dificuldade:')
                dificuldade_win = curses.newwin(1, 20, y+2, x+30)
                stdscr.refresh()
                dificuldade_entrada = Textbox(dificuldade_win)
                dificuldade_entrada.edit()
                dificuldade = str(dificuldade_entrada.gather())

                stdscr.refresh()
                stdscr.getch()
                return usuario1, usuario2, dificuldade
                break
                
            elif menu[current_row_idx] == "Sair":
                break
                
            #elif stdscr.addstr(0, 0, "You pressed {}".format(menu[current_row_idx])):
            #    stdscr.refresh()
            #    stdscr.getch()     
            #elif current_row_idx == len(menu)-1:
            #    break
            


        print_menu(stdscr, current_row_idx)
        
        stdscr.refresh()
