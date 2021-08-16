# DICA: Comentário no PYTHON se usa "#"

#Importando a biblioteca JSON
import json

#Abri o json das cartas e salvei em JSON_CARTAS
#O problema com esse arquivo era o => encoding="utf8". 
#Por ser um arquivo que não está vindo de nenhuma API precisamos colocar isso pra funcionar!
json_cartas = open('cartas/cartas.json', encoding="utf8")

#cartas_tarot recebe o OBJETO do JSON, que tem o nhits (numero de cartas), e as cartas (cards)
cartas_tarot = json.load(json_cartas)

#usei um for para percorrer as cartas, o p é cada elemento que ele percorre.
for p in cartas_tarot['cards']:

    print('Tipo: ' + p['tipo'])
    print('Nome: ' + p['nome'])
    print('Descrição: ' + p['desc'])
    print('')

    #Repara que no python não usamos chaves;
    #Então é a identação é quem define se vc tá dentro ou fora de um contexto;
    #Nesse caso, esses prints estão dentro do for;
#---# <== Essa distância aqui define o print estar dentro do for ou não.   

#Aqui já saímos do for
print ("Saí do for")