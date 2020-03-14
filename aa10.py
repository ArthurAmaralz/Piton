from random import randint
from time import sleep

rr = []
for c in range(4):
    r = randint(1,6)
    rr.append(r)


dados = {'nome': '', 'media':''}
sit = {'a':'Aprovado', 'r':'Reprovado'}
dados['nome'] = str(input('Nome: '))
dados['media'] = int(input('Media: '))
if dados['media'] >= 7:
    print(f'Parabens {dados["nome"]} você está {sit["a"]}')
else:
    print(f'Você está {sit["r"]}')



###TREINO###
estados = {}
brasil = []
for c in range(3):
    estados['uf'] = (input('Digite seu estado: '))
    estados['sg'] = str(input('Qual a sigla? '))
    brasil.append(estados.copy())
print(brasil)
for e in brasil:
    print(e['uf'])
for e in brasil:
    print(e)
    for i in e:
        print(i)


brasil = []
estado = {'uf':'rio de janeiro', 'sigla': 'Rj'}
estadoo = {'uf':'Paraiba', 'sigla':'PB'}
brasil.append(estado)
brasil.append(estadoo)
print(brasil)
print(brasil[1]['uf'])

pessoas = {'nome':'Arthur','sexo':'M', 'idade':26}
print(f'A pessoa {pessoas["nome"]} tem {pessoas["idade"]} anos')

filmes = {'Titulo' : 'Donnie Darko' ,
         'ano' : 2001 ,
         'Genero' : 'Scifi'
        }
print(filmes.values())
print(filmes.keys())
print(filmes.items())

for i,j in filmes.items():#Titulo : Donnie Darko / ano : 2001 / Genero : Scifi
    print(f'{i} : {j}')
for i in filmes.values():#Donnie Darko / 2001 / Scifi
    print(i)
for j in filmes.keys():#Titulo / ano / Genero
    print(j)


dicionario = {}
dados = {'nome' : 'Arthur', 'idade' : 26}
print(dados)
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados)
del dados['idade']
print(dados)