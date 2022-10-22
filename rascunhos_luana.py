import math
import curses

menu = ["Jogar", "Ranking", "Sair"]
'''
print(menu[1])


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
                x = w//2 
                y = h//2
                stdscr.addstr(y, x, 'Digite o nome do usuário1:')
                stdscr.addstr(y+1, x, 'Digite o nome do usuário2')
                stdscr.addstr(y+2, x, 'Digite o nível de dificuldade:')
            elif menu[current_row_idx] == "Sair": 
                h, w = stdscr.getmaxyx()
                x = w//2 
                y = h//2
                stdscr.addstr(y, x,'Digite o nome do usuário1:')
                stdscr.refresh()
                stdscr.getch()
            elif stdscr.addstr(0, 0, "You pressed {}".format(menu[current_row_idx])):
                stdscr.refresh()
                stdscr.getch()     
            #elif current_row_idx == len(menu)-1:
            #    break

        print_menu(stdscr, current_row_idx)
        #stdscr.refresh()

curses.wrapper(main)




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
