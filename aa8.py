###  VALIDAR EXPRESSÕES ###
exp = str(input('Digite a expressão: '))
if exp.count('(') == exp.count(')'):
    print('Sua expressão é válida!!')
else:
    print('Sua expressão não é válida')


n = []
v = input('Digite a expressão: ')
n.append(v)
if v in '()':
    v.count('(')
    v.count(')')
if v.count('(') != v.count(')'):
    print('Expressão invalida!')
else:
    print('Expressão aceita!')

### LISTA PAR/ IMPAR ###
n = []
i = []
p = []
while True:
    v = int(input('Digite um valor: '))
    n.append(v)
    if v % 2 == 0:
        p.append(v)
        print(f'{v} é PAR.')
    else:
        i.append(v)
        print(f'{v} é IMPAR')
    a = str(input('Deseja Continuar?[S/N]')).lower().strip()[0]
    while a not in 'sn':
        a = str(input('Valor invalido, Digite [S/N]: ')).lower().strip()[0]
    if a == 'n':
        print(f'Todos os valores {n}\nConjunto PARES {p}\nConjunto IMPARES {i}')
        break


### LISTA SIMPLES ###
n = []
while True:
    n.append(int(input('Digite um valor: ')))
    a = str(input('Deseja continuar?[S/N]')).lower().strip()[0]
    while a not in 'sn':
        a = str(input('Opção invalida, digite [S/N]? '))
    if a == 'n':
        n.sort(reverse=True)
        print(f'Um total de {len(n)} foram digitadas\n Valores em ordem decrescente {n}')
        if 5 in n:
            print('5 Está na lista')
        else:
            print('5 Não está na lista')
        break


### LISTA SEM SORTED ###
n = []
for c in range(5):
    v = int(input('Digite um valor:'))
    if c == 0 or v > n[-1]:
        n.append(v)
        print(f'Add no final da lista')
    else:
        p = 0
        while p < len(n):
            if v <= n[p]:
                n.insert(p,v)
                print(f'Add na posição {p}')
                break
            p+=1
print(f'Valores em ordem: {n}')


lista = []
for c in range(5):
    n = int(input('Número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('O número foi adicionado no final da lista.')
    else:
        for i in range(5):
            if n <= lista[i]:
                lista.insert(i,n)
                print(f'O número foi adicionado na posição {i}.')
                break
print(lista)



### LISTA DE NUMEROS Ñ REPETIDOS ###
n = []
while True:
    v = (int(input('Digite um valor: ')))
    if v not in n:
        n.append(v)
    else:
        print('Não adicionado, valor repetido!')
    a = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
    while a not in 'sn':
        a = str(input('Não entendi,Deseja continuar [S/N]? ')).strip().lower()[0]
    if a == 'n':
        print(f'Os valores digitados foram: {sorted(n)}')
        break


### MAIOR E MENOS COM POSIÇÕES ###
n = []
for c in range(0,5):
    n.append(int(input(f'Digite o {c+1}º valor: ')))
print(f'O maior valor foi {max(n)} na posição {n.index(max(n))+1}º'
      f' e o menor {min(n)} na posição {n.index(min(n))+1}º')

n = []
for c in range(0,5):
    n.append(int(input(f'Digite o {c+1}º valor: ')))
print(f'A posição de {max(n)} é: ', end='')
for i, v in enumerate(n):
    if v == max(n):
        print(i+1, end='...')
print()
print(f'A posição de {min(n)} é: ', end='')
for i, v in enumerate(n):
    if v == min(n):
        print(i+1, end='...')
print()





