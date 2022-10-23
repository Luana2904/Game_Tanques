import curses
import ctypes
import random
from curses.textpad import Textbox, rectangle
from random import shuffle, randrange
import math
import time
import menu

opcao_pos_jogo = ["Retornar ao menu"]

def main_game_over(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    box = [[3,3], [sh-3,sw-3]]
    win = curses.newwin(box[0][0], box[0][1], box[1][0], box[1][1])
    rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    COR = curses.color_pair(3)

    x_ = sw//2 - 3
    y_ = sh//2 - 3

    stdscr.addstr(y_, x_, 'GAME OVER', COR)

    key = stdscr.getch()
    if key == curses.KEY_ENTER or key in [10, 13]:
        stdscr.clear()
        menu.main_menu(stdscr)