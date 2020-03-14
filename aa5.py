### LEITOR ###
n = m = a = b = c = 0
v = 's'
while v in 's':
    n = float(input('Digite um numero:'))
    m += n
    c += 1
    if c == 1:
        a = b = n
    else:
        if n > a:
            a = n
        if n < b:
            b = n
    v = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
print(f'O maior numero é : {a}\nO menor é: {b}')
print(f'A media é: {m/c}')


###  SOMA DE FATORES ###
n = int(input('Digite um numero: ')) ## n = s = c = 0###
s = c = 0
while n != 999:
    s += n
    c += 1
    n = int(input('Digite outro valor: (999 para terminar)'))
print(f'Foram digitados um total de {c} valores\n soma total de {s}')


####Fibonacci####
n = int(input('Numero de termos de fibonacci: '))
b = 0
t = 1
c = 3
print(b)
print(t)
while c <= n:
    q = t + b
    print(q)
    b = t
    t = q
    c+=1


#### PA #####
a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
n = 1
t = 0
m = 10
print(a)
while m != 0:
    t += m
    while n < t:
        a += r
        n+=1
        print(a)
    m = int(input('Mais algum termo? ([0] zero para terminar)'))
print(f'Você solicitou um total de {t} termos!')

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 10
while c > 0:
    print(p, end=' ')
    p += r
    c -= 1
    if c == 0:
        c = int(input('\nAcrescentar mais números na sequência: '))

a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
n = 1
print(a)
while n < 10:
    a += r
    n+=1
    print(a)

#### FATORIAL ####
a = int(input('Valor do fatorial:'))
c = a
f = 1
for c in range(a, 0 ,-1):
    f*=c

a = int(input('Digite o valor do fatorial: '))
c = a
f = 1
print(f'Fatorial de {a}!: ', end='')

while c > 0:
    print(c , end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

from math import factorial
a = int(input('Digite um numero: '))
b = factorial(a)
print(b)

##### MENUS #####
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
a = 0
while a != 5:
    a = int(input('[1] Para soma\n[2] Para multiplicar\n[3]Maior\n[4]Novos valores\n[5]Sair do programa\n'))
    if a == 1:
        print(f'A soma de {n1} + {n2} é: {n1+n2}')
    elif a == 2:
        print(f'A multiplicação de {n1} *  {n2} é: {n1*n2}')
    elif a == 3:
        print(f'O maior valor é {max(n1,n2)}')
    elif a == 4:
        n1 = int(input('Novo valor 1º:'))
        n2 = int(input('Novo valor 2º'))
    elif a > 5 or a == 0:
        print('Digite uma opção valida!')

##### JOGO NUMERO #####
from random import randint
r = randint(0, 10)
a = int(input('Tente acertar o numero pensado: '))
c = False
v = 1
while not c:
    a = int(input('Tente mais uma vez:'))
    v+=1
    if a == r:
        c = True
    else:
        if a > r:
            print('Menosss')
        elif a < r:
            print('Maissss')
print(f'Parabens!!! Você acertou com um total de {v} tentativas.')


r = randint(0, 10)
a = int(input('Adivinhe o numero: '))
v = 1
while a != r:
    a = int(input('Tente mais uma vez: '))
    v+=1
if a == r:
    print(f'Você acertou com um total de {v} tentativas!!!')

#### ENTRADA DE SEXO ####
s = str(input('Digite seu sexo [M/F]:')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Sexo não validado, informe um valido [M/F]:')).strip().upper()[0]
print(f'Seu sexo é {s}')
