import random
l = input('primeiro:')
j = input('Segundo: ')
p = input('Terceiro: ')
a = input('Quarto: ')
r = [l, j, p, a]
random.shuffle(r)
print(f'O aluno escolhido foi {random.choice(r)}')
print(f'A ordem de apresentação dos trabalhos {r}') #OU
print(f'A ordem de apresentação dos trabalhos {random.sample(r,k=4)}')


import math
a = float(input('Digite o angulo:'))
aa = math.radians(a)
print(f'A tangente de {aa} é {math.tan(aa):.2f}\nO seno é {math.sin(aa):.2f}\nO cosseno é {math.cos(aa):.2f}\n'
      f'Em radianos é {math.radians(aa):.2f}')

import math
a = float(input('Digite o angulo:'))
print(f'A tangente de {a} é {math.tan(a):.2f}\nO seno é {math.sin(a):.2f}\nO cosseno é {math.cos(a):.2f}\n'
      f'Em radianos é {math.radians(a):.2f}')


a = int(input('Digite o primeiro cateto: '))
b = int(input('Digite o segundo cateto: '))
print(f'A hipotenusa é igual a: {(a**2 + b**2)**0.5}')

import math
a = float(input('Digite um numero decimal: '))
print(f'O valor é {a} e a parte inteira é {math.trunc(a)}')


a = int(input('Digite o valor de A(termo X²): '))
b = int(input('Digite o valor de B(termo X): '))
c = int(input('Digite o valor de C(constante): '))
d = (b**2)-(4*a*c)
print(f'O valor do Delta é {d}  O valor de X1 = {(-b+d**0.5)/2*a} e X2 = {(-b-d**0.5)/2*a}')
#------------------------------------------------------------------------
import math
n = int(input('Digite um numero: '))
r = math.sqrt(n)
print(f'A raiz é {r:.2f}')
#ou simplificar fazendo:
from math import sqrt
n = int(input('digite uma raiz: '))
r = sqrt(n)
print(f'A raiz é {r:.4f}')