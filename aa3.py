from random import choice
import random

#itens = ('Pedra', 'Papel', 'Tesoura')
#comp = random.randint(0, 2)
#print(f'imprimir resultado {itens[comp]}')
print('Escolha:\n1 - Pedra\n2 - Tesoura\n3 - Papel')
a = int(input('Qual deles: '))
r = choice([1,2,3]) ## ou r = random.randint (1,3)
if a == r:
    print('Empate!')
elif a == 1 and r == 2:
    print('Você venceu!escolhi tesoura')
elif a == 1 and r == 3:
    print('Você perdeu!deu papel')
elif a == 2 and r == 1:
    print('Você perdeu!deu pedra')
elif a == 2 and r == 3:
    print('voce ganhou! escolhi papel')
elif a == 3 and r == 1:
    print('você ganhou! escolhi pedra')
elif a == 3 and r == 2:
    print('você perdeu! deu tesoura')
print(r)


p = float(input('Preço do produto: '))
f = int(input('Qual a forma de pagamento?\n1 - para Dinheiro/Cheque\n2 - para Vecimento Cartão\n3 - para até 2x no Cartão\n4 - para 3x ou mais no Cartão\n'))
a = 1 ; b = 2 ; c = 3 ; d = 4
if f == a:
    print(f'Desconto de 10%!\n valor da compra: {p*0.9}')
elif f == 2:
    print(f'Desconto de 5%!\n valor da compra de {p*0.95}')
elif f == 3:
    print(f'Sem desconto!\n valor {p}')
elif f == 4:
    pf = p*1.2
    par = int(input('Quantas parcelas deseja dividir? '))
    print(f'Juros de 20%\nTotal:{pf}!\n Valor das parcelas de {(p*1.2)/par}')
else:
    print('Escolha uma opção valida!')


p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
i = p/a**2
if i < 18.5:
    print(f'Seu IMC é {i}\nVocê está a baixo do peso!')
elif 18.5 <= i < 25:
    print(f'Seu IMC é ideal! {i}')
elif 25 <= i < 30:
    print(f'seu IMC é {i}\nVocê está sobrepeso.')
elif 30 <= i <= 40:
    print(f'Seu IMC é {i}\nVocê está obeso')
else:
    print(f'Tu tá gordo pra caralho irmão!\nObesidade morbida {i} IMC')



r1 = int(input('Primeira Reta: '))
r2 = int(input('Segunda Reta: '))
r3 = int(input('Terceira reta: '))
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print('Forma um triangulo!')
    if r1==r2==r3:
        print('Esse triangulo é EQUILATERO')
    elif r1!=r2!=r3!=r1:
        print('Esse trialgulo é ESCALENO')
    else:
        print('Esse triangulo é ISOSCELES')
    #elif r1 == r2 !=r3 or r1 == r3 != r2 or r2 == r3 != r1
else:
    print('Não forma um triangulo')


from datetime import date
i = int(input('Digite seu ano de nascimento:'))
n = date.today().year
t = n-i
if t <= 9:
    print('Categoria: MIRIM')
elif t <= 14:
    print('Categoria: INFANTIL')
elif t <= 19:
    print('categoria: JUNIOR')
elif t <= 25:
    print('categoria SENIOR')
elif t > 25: 
    print('categoria MASTER')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
m = (n1+n2)/2
if m < 5:
    print(f'Você foi reprovado! media {m}')
elif 5 <= m < 6.9:
    print(f'Você está na recuperação! media {m}')
elif m >= 7:
    print(f'Parabens! aprovado!!!')

from datetime import date
ano = (date.today().year)
id = int(input('Digite seu ano de nascimento: '))
d = ano - id
if ano - id < 18:
    print(f'Você ainda ira se alistar!\nFaltam {18-(ano - id)} ano(s)\nSeu ano de alistamento é:{ano+(18-d)}')
elif ano - id == 18:
    print('Está na hora de se alistar! Procure a junta militar.')
elif ano - id > 18:
    print(f'Já passou do tempo de se alistar!\nMulta de atraso de {(ano - id)-18} anos\nSeu ano de alistamento era:{ano-(d-18)}')


n = int(input('Digite o primeiro valor:'))
v = int(input('Digite o segundo valor '))
if n > v:
    print(f'O maior valor é o primeiro: {n}')
elif v > n:
    print(f'O maior valor é o segundo: {v}')
else:
    print('Os valores são iguais!')


num = int(input('Digite o valor: '))
p = int(input('Você deseja converter ele em:\n1 - para binario\n2 - para octal\n3 - para hexadecimal\n'))
if p == 1:
    print(f'O valor de {num} em binario é: {bin(num)[2:]}')
elif p == 2:
    print(f'O valor de {num} em octal é: {oct(num)[2:]}')
else:
    print(f'Ovalor de {num} em hexadecimal é: {hex(num)[2:]}')

val = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salario?'))
temp = float(input('Quantos anos deseja pagar? '))
if val/(temp*12) <= sal*0.3:
    print(f'Seu emprestimo foi aprovado! em {temp} anos, no valor de {val/(12*temp):.2f}')
else:
    print(f'Infelizmente seu emprestimo não foi aprovado,\nPois a prestação foi de {val/(12*temp):.2f} e supera os 30% do seu salario')



n = str(input('Qual seu nome?:')).lower().strip()
if n == 'arthur':
    print(f'Que lindo nome {n}')
elif n == 'maria' or n =='joão' or n== 'josé' or n == 'lais':
    print('Que bosta de nome!')
elif n in 'ana teo joaquin amaral':
    print('nome de corno!')
else:
    print('nome sem graça!')
print(f'Tenha um otimo dia! {n}')
