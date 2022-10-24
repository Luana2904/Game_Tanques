import curses
import menu
import json


listobj= []

with open("informacao.json") as fp:
    listobj= json.load(fp)
    listobj.append({
        "nome": "claudia", #usuario, usuario2 //  loop do apend: lista JOGADOR, i in range o len(JOGADOR)
        "pontuacao": 38 #criar lista p pontuação? 
    })

with open("informacao.json", 'w') as json_file:
    json.dump(listobj, json_file, indent= 4) #linha onde o json se altera

<<<<<<< HEAD
with open("informacao.json", 'r'):
    for i in listobj:
        if listobj[i]['pontuacao'] > maior:
            maior = listobj[i]['nome']
            index = i

            
=======
#with open("informacao.json", 'r'):
    #for i in listobj:
        #if listobj[i]['pontuacao'] > maior:
            #maior = listobj[i]['nome']
            #index = i
        

>>>>>>> 7a3cfa75db113694cb5c72304261eb0990ac1950

        