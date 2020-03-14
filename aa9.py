###CADASTRO ALUNOS,MEDIA E NOTAS ###
l = []
ll = []
while True:
    a = str(input('Nome: '))
    n = int(input('1º nota: '))
    n1 = int(input('2º nota '))
    l.append(a)
    l.append(n)
    l.append(n1)
    co = str(input('Mais algum aluno? [S/N]')).lower().strip()[0]
    ll.append(l[:])
    l.clear()
    if co in 'n':
        for i, c in enumerate(ll):
            print(f'{i}º - Aluno: "{c[0]}" Media: {(c[1]+c[2])/2}')
        while True:
            v = int(input('Deseja ver as notas de qual aluno [Nº]?[para parar 999] '))
            if v == 999:
                break
            print(f'Primeira nota: {ll[v][1]}\nSegunda nota: {ll[v][2]}')
        break


### MEGA SENA ###
from random import randint
from random import sample
from time import sleep

jog = int(input('Quantos jogos sorteados: '))
print(f'Total de {jog} jogos')
for c in range(jog):
    num = sample(range(1, 60),k=6)
    num.sort()
    print(f'Jogo {c+1}: {num}')


l = []
l2 = []
c1 = 1
p = int(input('Quantos jogos sorteados: '))
while p >= c1:
    c = 0
    while True:
        a = randint(1,60)
        if a not in l:
            l.append(a)
            c+=1
        if c == 6:
            break
    c1 += 1
    l.sort()
    l2.append(l[:])
    l.clear()
for i, j in enumerate(l2):
    print(f'O {i+1}º foi: {j}')
    sleep(1)


###  MATRIZ SOMA, MAIOR, LINHAS E COLUNAS ###
m = [[],[],[]]
s = sc = ml = 0
for i in range(3):
    for j in range(3):
        m[i].append(int(input(f'Digite o valor {i,j}:')))
for a in range(3): # poderia colocar "i" novamente e "j" em baixo.
    for b in range(3):
        print(f'[{m[a][b]:^5}]', end='')
        if m[a][b] % 2 == 0: ## PAR
            s+=m[a][b]
    print()
for i in range(3): ## SOMA DA 3º COLUNA
    sc+=m[i][2]
for j in range(3): ## MAIOR VALOR DA 2º LINHA
    if j == 0 or m[1][j] > ml:
        ml = m[1][j]
#for v in m:
 #  for k in v:
  #      if k % 2 == 0:
   #         s+=k
print(f'Soma dos pares: {s}\nSoma da 3º Coluna {sc}\nMaior valor da 2º linha: {ml}')





### MATRIZ 3X3 ###
m = [[],[],[]]
for l in range(3):
    for c in range(3):
        m[l].append(int(input(f'Digite o valor [{l},{c}]: ')))
for a in range(3):
    for b in range(3):
        print(f'[{m[a][b]}:^5]', end='')
    print()
# OUUUU  >>> for v in m:    print(v)





### UNICA LISTA PARA PARES E IMPARES ###
l = [[],[]]
for c in range(7):
    r = (int(input(f'Digite o {c+1}º valor: ')))
    if r % 2 == 0:
        l[0].append(r)
    else:
        l[1].append(r)
#OU l[0].sort / l[1].sort
#print ( l[0] / l[1] )
print(f'{sorted(l[0])} PARES')
print(f'{sorted(l[1])} IMPARES')
print(l)


### LISTA NOME, PESO, MAIOR/MENOR PESO ###
n = []
h = []
ma = me = 0
while True:
    n.append(str(input('Digite seu nome: ')))
    n.append(int(input('Seu peso:')))
    if len(h) == 0:
        ma = me = n[1]
    else:
        if n[1] > ma:
            ma = n[1]
        if n[1] < me:
            me = n[1]
    h.append(n[:])
    n.clear()
    a = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    if a in 'n':
        print(h)
        print(f'Cadastrada um total de {len(h)} pessoas.')
        for p in h:
            if p[1] == ma:
                print(f'Maior peso foi de {p[0]}, com {ma} ')
        for p in h:
            if p[1] == me:
                print(f'Menor peso foi de {p[0]}, com {me}')
                break


### MAIOR E MENOR ID ###
v = []
p = []
ma = me = 0
for c in range(2):
    v.append(str(input('Digite seu nome: ')))
    v.append(int(input('Digite sua idade: ')))
    p.append(v[:])
    v.clear()
for l in p:
    if l[1] >= 18:
        ma +=1
        print(f'{l[0]} é de maior!')
    else:
        me +=1
        print(f'{l[0]} é de menor!')
print(f'total de {ma} maior e {me} menor')


g = [['arthur',26],['maria',19],['joao',23],['jose',18],['ruan', 29]]
for v in g:
    print(f'{v[0]} tem {v[1]} anos')

n = []
n.append('Arthur')
n.append(26)
print(n)
g = []
g.append(n[:])
n[0] = 'Tutu'
n[1] = 23
g.append(n)
print(g)


a = [1,0,3]
b = [8,7,9]
b.append(a[:])
print(b)
p = [['pedro', 25],['arthur', 26],['lais', 24]]
print(p[0][1])
print(p[1][0])
print(p[2])