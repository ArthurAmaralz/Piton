q = 0
v = 0
vv = 0
m = 0
h = ''
for a in range(1,5):
    n = str(input(f'Nome da {a}º pessoa: '))
    i = int(input(f'Idade da {a}º pessoa: '))
    s = int(input('[1] para Masculino\n[2] para Feminino'))
    q += i
    if s == 1 and i > v:
        v = i
        h = n
    elif s == 2  and i < 20:
        m+=1
print(f'A media de idade do grupo é: {q/4:.2f}')
print(f'O homem mais velho é {h} e sua idade é {v} anos!')
print(f'Um total de {m} mulheres tem menos de 20 anos!')


import math

n = []
i = []
s = []
for a in range(1,4):
    n.append(str(input(f'Digite o nome da {a}º pessoa: ')))
    i.append(int(input(f'Digite a idade da {a}º pessoa: ')))
    s.append(int(input('Digite [1} para Masculino\nDigite [2] para Feminino\n')))
    m = 1
    f = 2
#if s == 1:

print(f'A media de idade das {len(n)} pessoas é:{sum(i)/len(i):.1f}')


p = []
for a in range(1,6):
    p.append(int(input(f'Digite o peso da {a}º pessoa:')))
print(f'O maior numero é {max(p)} e o menor numero é {min(p)}')

ma = 0
me = 0
for a in range(1,6):
    p = float(input(f'Digite o {a}º peso:'))
    if a == 1:
        ma = p
        me = p
    else:
        if p > ma:
            ma = p
        if p < me:
            me = p
print(f'O maior peso é: {ma}\nO menor peso é: {me}')


from datetime import date
c = 0
e = 0
b = date.today().year
for a in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {a}º pessoa: '))
    if b - ano <= 18:
        c+=1
    else:
        e+=1
print(f'Maior de idade: {e}\nMenor de idade: {c}')


f = str(input("Qual a frase? ")).lower().replace(" ", "")
if f == f[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")


a = str(input('Digite a frase: ')).strip().lower()
b = a.split()
c = ''.join(b)
s = c[::-1]
if c == s:
    print('A frase é um palidromo!')
else:
    print('A frase não é um palindromo!')
print(s)


n = int(input('Digite um numero: '))
c = 0
b = 0
for a in range(1, n+1):
    if n % a == 0:
        c +=1
    else:
        b+=1
    print(a)
print(f' o numero {n} foi dividido {c} vezes!')
if c <= 2:
    print(f'{n} é primo!')
else:
    print(f'{n} não é primo!')


a = int(input('Digite um numero:'))
c = 0
b = 0
for s in range(1, a+1):
    if a % s == 0:
        print('\33[32m', end=' ')
        c+=1
    else:
        print('\33[31m', end=' ')
        b+=1
    print(s, end=' ')
print(f'O numero {a} foi dividido {c} vezes.')
if c == 2 and c != 1:
    print('E é um numero primo.')
else:
    print('Não é primo.')



a1 = int(input('Primeiro termo: '))
r = int(input('Razão:'))
d = a1 + (10)* r
for x in range(a1, d, r):
    print(x)
#a1+(x-1)*r

s = 0
x = 0
for c in range(1, 7):
    a = int(input(f'Digite {c}º numero: '))
    if a % 2 == 0:
        s +=a
        x+=1
print(f'Temos {x} numeros pares e a soma total é {s}')


b = int(input('Digite a tabuada desejada: '))
for a in range(0, 11):
    s = a*b
    print(s)


s = 0
c = 0
for a in range (1, 501, 2):
    if a % 2 != 0 and a % 3 == 0:
        s += a
        c += 1
        print(s, c)

for a in range(2, 51, 2):
    print(a)


import time
for a in range(10, 0, -1):
    print(f'É:{a}')
    time.sleep(1)
print('ZEROOOOO000!!!')


s = 0
for a in range(0, 3):
    n= int(input('Digite um numero:'))
    s += n
print(s)


i = int(input('inicio:'))
f = int(input('Final:'))
p = int(input('Pula:'))
for a in range(i, f+1, p):
    print(a)

q = int(input('Digite um numero:'))
for a in range(0, q+1):#sempre irar contar um valor antes do escolhido, então +1
    print(a)
for a in range(0, 10, 2):
    print(a)
    print('é o que!')
for a in range(6, 1, -1):
    print(a)
for a in range(1, 6):
    print('Boraaaa!')
for a in range(0, 5):
    print('hora do show porra!')
print('Fim!')