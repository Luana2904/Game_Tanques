import curses
import menu
import json

listobj= []

with open("informacao.json") as fp:
    listobj= json.load(fp)
    listobj.append({
        "nome": "claudio", #usuario, usuario2 //  loop do apend: lista JOGADOR, i in range o len(JOGADOR)
        "pontuacao": 36 #criar lista p pontuação? 
    })

with open("informacao.json", 'r+') as json_file:
    json.dump(listobj, json_file, indent= 4) #linha onde o json se altera

with open("informacao.json", 'r'):
    for i in listobj:
        if listobj[i]['pontuacao'] > maior:
            maior = listobj[i]['nome']
            index = i
        else:
            

        