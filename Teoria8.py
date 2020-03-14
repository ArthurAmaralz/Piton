Resumão Não executável Comentado

INPUT SEM CLEAR DA LISTA:
    guys.append ( [ input('Digite o nome ') ,  float ( input('Digite o peso') ) ] )

lista.append([a,[b,c],d]) ## exemplo para add listas

a = [1,0,3]
b = [8,7,9]
b.append(a[:])
print(b)
p = [['pedro', 25],['arthur', 26],['lais', 24]]
print(p[0][1])
print(p[1][0])
print(p[2])


lanche = list[]
lanche.append('valor')  # inclui valor na última posição
lanche.insert(0, 'valor')  # substitui valor na posição '0'
del lanche[3]
lanche.pop()  # elimina o último e reposiciona os valores na lista
if 'valor' in lanche:  # evita msg de erro
    lanche.remove('valor')  # evita msg de erro
lista2 = list(range(4, 11))  # lista2 = [4,5,6,7,8,9,10]
lista3 = [8, 5, 4, 3, 0]
lista3.sort()  # ordenar valores [0,3,4,5,8]
lista3.sort(reverse=True)  # ordenar valores de forma inversa [8,5,4,3,0]
len(lista3)  # resposta: 5

Resumão Comentado
num = [2, 5, 9, 1, 7]
# num1 = num #link entre lista num e num1
# num1[1]=6
num1 = num[:]  # gera uma cópia de num
num1[1] = 6, 8
print(num1)
# num.append(8) #adiciona '8'
# num[0]=3 #substitui a posição 0 pelo valor '3'
# num.sort(reverse=True) #ordena de forma inversa
# num.insert(2,4) #adiciona valor '4' após a posição 2 reordenando a lista
# num.pop() #exclui o último valor '8'
# num.pop(4) #exclui o valor na posição 2 por '1'
print(f'Lista primária: {num}')
print('Excluído valor: {}, Nova lista: {}'.format(num.pop(4), num))
if (9) in num:  # Atenção
    num.remove(9)  # Muita Atenção
    num.append(0)  # Importante
print(f'Condição verificada: {num}' if (1) and (2) or (6) in num else 'Condição não se aplica!')  # Importante

print(f'Lista verificada: {num}')
num.sort()
print(f'Lista ordenada: {num}')
print(f'Lista com {len(num)} elementos.')

Resumão(Bônus)

num1 = list()
num1.append(1), num1.append(4), num1.append(5), num1.append(3)

for c, v in enumerate(num1):
    print(f'Na {c + 1}ª posição temos o valor: {v}.')
print('Informe mais 6 (seis) valores!')
for c in range(0, 6):
    num1.append(int(input(f'Informe {c + 5}º valor: ')))
print(f'{num1}')
for c, v in enumerate(num1):
    print(f'Na posição {c + 1} temos o valor: {v}.')

lan = [0, 1, 2, 3, 4]
lan.append(9)
lan.insert(0, 3)
print(lan)
del lan[2]
print(lan)
lan.pop(2)
print(lan)
lan.remove(3)
print(lan)
if 9 in lan:
    lan.remove(9)
print(lan)
val = list(range(4, 11))
print(val)
v = [1, 2, 5, 6, 8, 4, 47, 14, 62, 0]
print(v)
v.sort()
print(v)
print(sorted(v))
v.sort(reverse=True)
print(v)
len(v)
n = [1, 2, 3, 4]
n[2] = 5
n.append(8)
print(n)
n.insert(2, 2)
print(n)
n.pop(2)
print(n)
for c, l in enumerate(v):
    print(f'Na posição {c + 1} está {l}')
a = [1, 2, 3, 4]
b = a[:]  # copia da lista
b[2] = 8
print(f'Lista A:{a}\nLista B:{b}')
