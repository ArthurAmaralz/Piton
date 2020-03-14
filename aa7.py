### TUPLAS ###
### IDENTIFICADOR DE VOGAIS ###
p = (   'apreder', 'programar', 'linguagem', 'python', 'curso',
        'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
        'programador', 'futuro')
for a in p:
    print(f'\nA palavra {a.upper()} tem vogal(s): ', end='')
    for l in range(0, len(a)):
        if a[l] in 'aeiou':
            print(a[l], end=' ')


### LISTA TABULADA ###
t = ( 'lapis', 1.75, 'caneta', 2, 'caderno', 5,'estojo', 15,'mochila', 25, 'livro', 300,'regua', 2.50)
q = 1
print(f'{"LISTA DE PREÇOS":^40}')
for c in range(0,len(t),2):
    print(f'{t[c]:.<20}.................R${t[q]:>8.2f}')
    q+=2

for i in t:
    if type(i) is str:
        print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:>5.2f}')
print('--'*20)


n = (int(input('Digite um valor')),int(input('Digite um valor')),int(input('Digite um valor')),
     int(input('Digite um valor')))
print(f'Você digitou: {n}')
print(f'O nº 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O 3 aparece na {n.index(3)+1}º posição ')
else:
    print(f'O 3 não aparece na lista')
print('Os valores pares digitados foram:', end=' ')
for c in n:
    if c % 2 == 0:
        print(c, end=', ')
'''for p, c in enumerate(n):
    if c == 3:
        print(f'O 3 aparece na {p+1}º posição ')
for pp,cc in enumerate(n):
    if cc % 2 == 0:
        print(f'Os valores pares são: {cc}')'''

c = 0
n = (int(input('Digite um valor')),int(input('Digite um valor')),int(input('Digite um valor')),
     int(input('Digite um valor')),int(input('Digite um valor')))
if n == 9:
    c+=1
print(f'O nº 9 apareceu {c} vezes')
if n == 3:
    print(n.count(3)+1)
else:
    print('O valor 3 não foi digitado nenhuma vez')
if n[2] % 2 == 0:
    p = n
    print(p)

### NUMEROS RANDOM ###
from random import randint
n = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(n)
print(max(n),min(n))

a = randint(0,10)
b = randint(0,10)
c = randint(0,10)
d = randint(0,10)
e = randint(0,10)
r = (a,b,c,d,e)
print(f'Os valores aleatorios foram: {r}')
print(f'E o maior valor foi {max(r)} e o minimo {min(r)}')

### TABELA CAMP.###
times = ('Flamengo','Santos','Palmeiras','Grêmio','Athletico-PR','São Paulo','Internacional','Corinthians','Fortaleza',
          'Goiás','Bahia','Vasco','Atlético-MG','Fluminense','Botafogo','Ceará','Cruzeiro','CSA','Chapecoense','Avaí')
#for t in times:
    #print(t)
print(f'Todos os times: {times}')
print(f'Os 5 primeiros colocados:\n{times[:5]}', end=' ')
print(f'\nOs 4 ultimos são:\n{times[-4:]}', end=' ')
print(f'\nNomes em ordem alfabetica:\n{sorted(times)}')
print(f'A Chapecoense está em: {times.index("Chapecoense")+1}º')

### CONTADOR POR EXTENSO ###
n = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
v = 0
while True:
    while  0 <= v <= 20:
        v = int(input('Digite um numero entre 0 e 20:[negativo para sair] '))
        while v > 20:
            v = int(input('Digite um numero entre 0 e 20:[negativo para sair] '))
        if v < 0:
            break
        print(f'O numero {v} por extenso é "{n[v]}"')


a = (1, 5, 2, 3, 4, 6, 7, 8, 5)
lan = ('agua', 'hamburgue', 'batata', 'sorvete', 'refri', 'pizza')
print(lan[2])
print(lan[1:4])
print(lan[-1])
print(lan[-3])
print(lan[:5])
print(lan[3:])
print(len(lan))
print(sorted(lan))
com = ('almoco', 'café', 'janta')
print(lan + com)
print(a.index(5, 2))  # OUTRA POSIÇÃO DEPOIS DA VIRGULA#
print(a.count(5))
for c in lan:
    print(c)
# for cont in range(0, len(lan)): !!!igual ao de cima!!!
# print(lan[cont])
for cont in range(0, len(lan)):
    print(cont)
for cont in range(0, len(lan)):
    print(f'comer o {lan[cont]} na  posição {cont}')
##OU
for p, c in enumerate(lan):
    print(f'comer {c} na posição {p}')
