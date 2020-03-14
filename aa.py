a = str(input('Digite seu nome:\n')).strip()
print(f'Seu nome é: {a}')
print(f'Primeiro nome é: {a.split()[0]}')
print(f'Ultimo nome é: {a.split()[-1]}')

n = str(input('Digite seu nome:\n')).strip()
print(f'Existe amaral no nome?: {"amaral" in n.lower()}')

n = str(input('Digite sua cidade: ')).strip()
print(f'Tem santo no nome? {n.lower()[:5] == "santo"}') #descobrir se está no inicio

c = str(input('Frase:')).strip().lower()
print('Seu nome tem essa quantidada de letras A: ',c.count('a'))
print('A primeira letra A aparece na posição: ',c.find('a')+1)
print('A ultima letra A aparece na posição ',c.rfind('a')+1)


a = int(input("Digite um numero entre 0 e 9999\n"))
q = a // 1 % 10
w = a // 10 % 10
e = a // 100 % 10
r = a // 1000 % 10
print(f'A unidade é: {q}')
print(f'A dezena é: {w}')
print(f'A centena é: {e}')
print(f'O milhar é: {r}')
#ou
n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('O número {} possui, {} milhares.'.format(n, n2[1]))
print('O número {} possui, {} centenas. '.format(n, n2[2]))
print('O número {} possui, {} dezenas. '.format(n, n2[3]))
print('O número {} possui, {} unidades.'.format(n, n2[4]))


n = str(input('Digite seu nome completo:\n')).strip()
print(n.upper())
print(n.lower())
print(len(n)-n.count(' '))
print(len(n.split()[0]))


frase = 'Curso Em Video Python'
print(len(frase))
print(frase[3:13])
print(frase[:13])
print(frase[1:])
print(frase[1::2])
print(frase[::2])
print(frase.replace('Python', 'Píton'))
print('Curso' in frase)
print(frase.lower().find('video'))
print(frase.split())
print(frase.split()[2]) #divide a frase em blocos e acrecentando o [2] só imprime o 3 bloco (0,1,2,3}
print(frase.split()[0][1]) #com o [1] imprime o 2 termo do primeiro bloco 1 (0)
print(frase.count('o')) #conta a quantidade de O na frase
print(frase.upper().count('O')) #conta a quantidade de O na frase maiuscula
