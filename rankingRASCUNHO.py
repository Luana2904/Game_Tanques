import curses
import menu
import json

listobj= []

#if path.isfile(filename) is False:
    #raise Exception("File not found")
    #with open('ranknovo.json', 'r+') as ranknovo:
        #json.dump(rank3, ranknovo)

with open("informacao.json", 'r+') as fp:
    listobj= json.load(fp)
    listobj.append({
        "nome": "claudio",
        "pontuacao": 36
    })
with open("informacao.json", 'r+') as json_file:
    json.dump(listobj, json_file, indent= 4)
ranking1 = {
    "nome": "b",
    "pontuacao": 4
}
ranking2 = {
    "nome": "a",
    "pontuacao": 3
}
listobj = []
players = [ranking1, ranking2]




#with open("informacao.json", 'w') as outfile:
   # json.dump(players, outfile)

#with open("informacao.json") as outfile:
   #data = json.load(outfile)
#print("\n Pont1: ", data[0]['pontuacao'])
#print("\n Pont2: ", data[1]['pontuacao'])
nome1= ranking1 ["nome"]

nome2= ranking2 ["nome"]

pont1= ranking1 ["pontuacao"]

pont2= ranking2 ["pontuacao"]

#if pont1 > pont2:
   # print(nome1 + " está em primeiro lugar" + '\n' + nome2 + " está em segundo lugar")
#else:
   # print(nome2 + " está em primeiro lugar" + '\n' + nome1 + " está em segundo lugar") 





    



# 'r' ler
# 'W' escrever
# 'r+' ler e escrever algo
# 'a' usado para acrescentar algo

#with open('ranking.txt', 'w') as arquivo:
 #   for valor in ranking:
#        arquivo.write(str(valor) + '\n')


    





    

