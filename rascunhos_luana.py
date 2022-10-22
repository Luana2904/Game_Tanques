import math

velocidade = 5
angulo = 10
gravidade = 9.8
tempo = 1

seno = math.sin(angulo)

if seno < 0:
    seno = -math.sin(angulo)

altura_maxima = math.ceil((velocidade*velocidade)/2*gravidade)
alcance = math.ceil(((velocidade*velocidade)*seno*2)/gravidade)



print(altura_maxima)
print(alcance)
print(seno)

'''
def cw():
    c = int(0)

    c=int(c)+int(10)
    print(c)

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
'''
