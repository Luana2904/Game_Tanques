import estrutura
import curses

def main_jogo(stdscr):
    estrutura.main(stdscr)

curses.wrapper(main_jogo)