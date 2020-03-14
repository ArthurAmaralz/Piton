'''\033[1;31;45m] #\codigo de cor[estilo;texto;background m]'''
print('\033[7;30mOlá mundo\033[m')
print('\033[0;33;44mOlá mundo\033[m')
print('\33[34mOlá mundo!\033[m')
print('\033[31mOlá mundo!')

cor = {'a' : '\033[34m', 'vm' : '\033[31m', 's' :'\033[m'}
print(f"{cor['a']}Arthur{cor['vm']} amaral {cor['a']}de {cor['vm']}lima{cor['s']}")


a = int(input('primeiro numero: '))
b = int(input('segundo numero: '))
c = int(input('terceiro numero:'))
n = [a,b,c]
print(f' O maior numero é: {max(n)}\n O menor numero é: {min(n)}')

a = int(input('escreva um numero: '))
b = int(input('escreva outro numero:'))
c = int(input('escreve outro numero: '))
if a > b and a > c: # primeiro metodo pra fazer
    print(f'{a} é o maior')
elif b > a and b > c:
    print(f'{b} é o maior')
else:
    print(f'{c} é o maior')
m = a # Segundo metodo pra fazer
if b < a and b < c:
    m = b
elif c < a and c < b:
    m = c
print(f'e o menor valor é {m}')

from _datetime import date
a = int(input('Qual ano deseja saber?(0 para ano atual): '))
if a == 0:
   a = date.today().year
if a % 4 == 0 and a % 100 !=0 or a % 400 == 0:
    print(f'O ano é de {a} é Bissexo!')
else:
    print(f'O ano de {a} não é bissexo!')

v = int(input('Qual a velocidade do veiculo? \n'))
c = (v-80)*7
if v > 80:
    print(f'Você foi multado!\nO valor da sua multa é de: {c}R$')
else:
    print('Você não foi multado!')


r1 = int(input('reta 1:'))
r2 = int(input('reta 2: '))
r3 = int(input('reta 3:'))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('é possivel formar um triangulo')
else:
    print('Não forma um triangulo')


s = int(input('Seu salario: '))
if s >= 1250:
    n = s*1.1
else:
    n = s*1.15
print(f'Seu salario é {n:.2f}R$')


a = float(input('Qual a distancia da viagem?\n'))
if a <= 200:
    print(f'O valor da passagem é de:{a*0.5}R$')
else:
    print(f'O valor da passagem é de:{a*0.45}R$')

a = int(input('Digite um numero: '))
if a % 2 == 0:
    print('Seu numero é par')
else:
    print('Seu numero é impar')

from time import sleep
from random import randint
n = randint (0, 5)
a = int(input('Escolha um numero:\n'))
print('Aguarde!')
sleep(2)
if a == n:
    print('Parabens! você acertou :D')
else:
    print(f'O numero era:{n}\nTente novamente!')

from random import randint
n = randint (0, 5)
a = int(input('Escolha um numero:\n'))
if a == n:
    print('Parabens! você acertou :D')
else:
    print(f'O numero era:{n}\nTente novamente!')



n1 = float(input('Sua primeira nota: '))
n2 = float(input('Sua segunda nota: '))
n3 = float(input('Sua terceira nota: '))
m = (n1+n2+n3)/3
print(f'Sua media é: {m:.2f}')
if m >= 7:
    print('Parabens, você foi aprovado!')
else:
    print('Que pena, você foi reprovado!')
print('Boas ferias!')