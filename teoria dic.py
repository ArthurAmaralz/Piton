estado = dict()  # Cria um novo dicionário vazio "estado"
brasil = list()  # Cria uma nova lista vazia "brasil"


MÉTODO 1: Errado. Desse jeito, apenas os últimos valores digitados serão adicionados à lista repetidamente.
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado)
print(brasil)
MÉTODO 2: Errado. Desse jeito, o Python apresentará o erro "TypeError: unhashable type: 'slice'".
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado[:])
print(brasil)
MÉTODO 3: Correto. Desse jeito, o Python adicionará uma cópia do dicionário "estado" atual ao final da lista "brasil".
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)


for c in range(0, 3):  # Para cada número "c" de 0 a 2...
    estado['uf'] = str(input('Unidade Federativa: '))  # Atribui à chave 'uf' do dicionário "estado" o valor digitado
    estado['sigla'] = str(input('Sigla do Estado: '))  # Atribui à chave 'sigla' do dicionário "estado" o valor digitado
    brasil.append(estado.copy())  # Adiciona uma cópia do atual dicionário "estado" ao final da lista "brasil"
print(brasil)  # Exibe a lista "brasil" já preenchida com os estados

for e in brasil:  # Para cada dicionário "e" na lista "brasil"...
    print(e)  # Exibe o dicionário "e" atual

for e in brasil:  # Para cada dicionário "e" na lista "brasil"...
    for k, v in e.items():  # Para cada chave "k" e valor "v" nos itens do dicionário "e"...
        print(f'O campo {k} tem valor {v}.')  # Exibe formatado a chave "k" e o valor "v" atuais

for e in brasil:  # Para cada dicionário "e" na lista "brasil"...
    for v in e.values():  # Para cada valor "v" nos valores do dicionário "e"...
        print(v, end=' ')  # Exibe o valor "v" atual com um espaço no final, sem quebrar a linha
    print()  # Dá uma quebra de linha


brasil = list()  # Cria uma nova lista vazia "brasil"
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}  # Cria um dicionário "estado1" com 2 chaves e 2 valores
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}  # Cria um dicionário "estado2" com 2 chaves e 2 valores
brasil.append(estado1)  # Adiciona o dicionário "estado1" inteiro ao final da lista "brasil", como índice [0]
brasil.append(estado2)  # Adiciona o dicionário "estado2" inteiro ao final da lista "brasil", como índice [1]

print(estado1)  # Exibe {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(estado2)  # Exibe {'uf': 'São Paulo', 'sigla': 'SP'}

print(brasil)  # Exibe [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
print(brasil[0])  # Exibe {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(brasil[1])  # Exibe {'uf': 'São Paulo', 'sigla': 'SP'}

print(brasil[0]['uf'])  # Exibe Rio de Janeiro
print(brasil[1]['uf'])  # Exibe São Paulo

print(brasil[0]['sigla'])  # Exibe RJ
print(brasil[1]['sigla'])  # Exibe SP

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}  # Cria um dicionário "pessoas" com 3 chaves e 3 valores
print(pessoas)  # Exibe {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])  # Exibe Gustavo
print(pessoas['idade'])  # Exibe 22

"""  NOTA: Usar aspas duplas no índice do dicionário em prints formatados, para não dar erro. """
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')  # Exibe O Gustavo tem 22 anos.

print(pessoas.keys())  # Exibe dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values())  # Exibe dict_values(['Gustavo', 'M', 22])
print(pessoas.items())  # Exibe dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])

for k in pessoas.keys():  # Para cada chave "k" nas chaves (keys) do dicionário "pessoas"...
    print(k)  # Exibe a chave "k" atual

for v in pessoas.values():  # Para cada valor "v" nos valores (values) do dicionário "pessoas"...
    print(v)  # Exibe a o valor "v" atual

for k, v in pessoas.items():  # Para cada chave "k" e valor "v" nos itens do dicionário "pessoas"...
    print(f'{k} = {v}')  # Exibe formatado a chave "k" e o valor "v" atuais

del pessoas['sexo']  # Deleta a chave 'sexo' (com o valor 'M') do dicionário "pessoas"
pessoas['nome'] = 'Leandro'  # Substitui o valor 'Gustavo' da chave 'nome' por 'Leandro', do dicionário "pessoas"
pessoas['peso'] = 98.5  # Adiciona a chave 'peso' com o valor 98.5 ao final do dicionário "pessoas"

print(pessoas)  # Exibe o dicionário "pessoas" já modificado: {'nome': 'Leandro', 'idade': 22, 'peso': 98.5}


filme1 = {'titulo': 'Star Wars',
          'ano': 1977,
          'diretor': 'George Lucas'}  # Cria um dicionário "filme1" com 3 chaves (keys) e 3 valores (values)

filme2 = {'titulo': 'Avengers',
          'ano': 2012,
          'diretor': 'Joss Whedon'}  # Cria um dicionário "filme2" com 3 chaves (keys) e 3 valores (values)

filme3 = {'titulo': 'Matrix',
          'ano': 1999,
          'diretor': 'Wachowski'}  # Cria um dicionário "filme3" com 3 chaves (keys) e 3 valores (values)

locadora = list()  # Cria uma nova lista vazia "locadora"

locadora.append(filme1)  # Adiciona o dicionário "filme1" inteiro ao final da lista "locadora", como índice [0]
locadora.append(filme2)  # Adiciona o dicionário "filme2" inteiro ao final da lista "locadora", como índice [1]
locadora.append(filme3)  # Adiciona o dicionário "filme3" inteiro ao final da lista "locadora", como índice [2]

print(locadora[0]['ano'])  # Exibe o valor da chave "ano" contida no índice [0] ("filme1") de "locadora": 1977
print(locadora[2]['titulo'])  # Exibe o valor da chave "titulo" contida no índice [2] ("filme3") de "locadora": Matrix

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}  # Cria um dicionário "filme" com 3 chaves (keys) e 3 valores (values)

print(filme.keys())  # Exibe as chaves do dicionário "filme"
print(filme.values())  # Exibe os valores do dicionário "filme"
print(filme.items())  # Exibe os itens (chave + valor) do dicionário "filme"

for k, v in filme.items():  # Para cada chave (k) e valor (v) nos itens do dicionário "filme"...
    print(f'O {k} é {v}')  # Exibe formatado a chave (k) atual e seu respectivo valor (v)

Tuplas: () - Parênteses
Listas: [] - Colchetes
Dicionários: {} - Chaves
Exemplo 1 de Dicionário Vazio:
dados = dict()
Exemplo 2 de Dicionário Vazio:
dados = {}
Exemplo de Dicionário Preenchido com 1 Linha:
dados = {'nome': 'Pedro', 'idade': 25}
Exemplo de Dicionário Preenchido com Múltiplas Linhas:
filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}

dados = {'nome': 'Pedro', 'idade': 25}  # Cria uma dicionário "dados" com os índices 'nome' (Pedro) e 'idade' (25)
print(dados['nome'])  # Exibe Pedro
print(dados['idade'])  # Exibe 25

dados['sexo'] = 'M'  # Adiciona o índice 'sexo' com o valor 'M' ao final do dicionário "dados"
del dados['idade']  # Deleta o índice 'idade' (com o valor 25) do dicionário "dados"


di = input().split()

h = input().split(':')
hi = int(h[0])
mi = int(h[1])
si = int(h[2])

df = input().split()

h = input().split(':')
hf = int(h[0])
mf = int(h[1])
sf = int(h[2])

dt = int(df[1]) - int(di[1])
ht = hf - hi
mt = mf - mi
st = sf - si

if ht < 0:
    ht += 24
    dt -= 1
if ht == 60:
    mt = 0
    dt +=1
if mt < 0:
    mt += 60
    ht -=1
if mt == 60:
    st = 0
    ht +=1
if st < 60:
    st +=60
    mt -=1
if st == 60:
    st = 0
    mt +=1

print('{} dia(s)'.format(dt))
print('{} hora(s)'.format(ht))
print('{} minuto(s)'.format(mt))
print('{} segundo(s)'.format(st))