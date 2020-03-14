#### SAQUE DO BANCO ####
print('Disponivel apenas cedulas de R$50, R$20, R$10 e R$1')
while True:
    n = int(input('Digite o valor a ser sacado: R$'))
    a1 = n // 50
    a2 = (n % 50) // 20
    a3 = ((n % 50) % 20) // 10
    a4 = ((n % 50) % 20) % 10 // 1
    print(f'total de\n{a1} R$50\n{a2} R$20\n{a3} R$10\n{a4} R$1')
    v = ' '
    while v not in 'sn':
        v = str(input('Mais algum saque? [S/N]')).strip().lower()[0]
    if v == 'n':
        break

saque = int(input('Sacar R$: '))
cedulas = [1, 10, 20, 50]
c = 3
while saque > 0:
    qtdced = saque // cedulas[c]
    saque -= qtdced * cedulas[c]
    if qtdced > 0:
        print(f'{qtdced} cédulas de R$ {cedulas[c]}')
    c -= 1

#### SUPERMERCADO ####
q = qq = v = m = 0
b = ''
while True:
    n = str(input('Digite o nome do produto: ')).strip().lower()
    p = float(input('Valor:R$'))
    r = ' '
    while r not in 'sn':
        r = str(input('Deseja continuar? [S/N]:')).strip().lower()[0]
    v+=p
    qq +=1
    if p > 1000:
        q += 1
    if qq == 1 or p < m :
        b = n
        m = p
    if r == 'n':
        break
print(f'Valor total da compra:R${v}\nQuantos produtos acima de R$1000:{q}\nNome do produto mais barato {b} e seu valor é {m}')


#### BASE de CADASTRO ####
c = cm = cf = 0
while True:
    i = int(input('Digite sua idade:'))
    s =' '
    while s not in 'mf':
        s = str(input('Digite seu sexo [M] Masculino /[F] Feminino:')).strip().lower()[0]
    p = ' '
    while p not in 'sn':
        p = str(input('Deseja cadastrar novas pessoas? [S/N]')).strip().lower()[0]
    if i >= 18:
        c += 1
    if s == 'm':
        cm += 1
    if s == 'f' and i <= 20:
        cf += 1
    if p == 'n':
        print(f'Registrado um total de {c} maiores de 18 anos.')
        print(f'Um total de {cm} Homens cadastrados.')
        print(f'Um total de {cf} mulheres menores de 20 anos.')
        break


### PAR OU IMPAR ###
from random import randint
c = 0
while True:
    rr = randint(0, 10)
    v = int(input('Digite o valor: '))
    r = str(input('Par ou Impar? [P/I]')).lower().strip()[0]
    while r not in 'pi':
        r = str(input('Invalid, tente novamente, Par ou Impar? [P/I]')).lower().strip()[0]
    if (rr + v) % 2 == 0 and r == 'p':
        print('Parabens, deu par!! você venceu =D')
        print(f'Você jogou {v} e o computador {rr} e o total foi {v + rr} que é PAR')
        c+=1
    elif (rr +v) % 2 != 0 and r == 'i':
        print('Parabens, deu impar!! você venceu =D')
        print(f'Você jogou {v} e o computador {rr} e o total foi {v + rr} que é IMPAR')
        c+=1
    else:
        print(f'Que pena, você perdeu!\nNº de vitorias {c}')
        print(f'Você jogou {v} e o computador {rr} e o total foi {v + rr}')
        break
    print('Jogue novamente!')


####TABUADA####
while True:
    v = int(input('Deseja a tabuade que qual numero: '))
    if v < 0:
        break
    for n in range(1, 11):
        print(f'{v} X {n} = {n*v}')

#### SOMA DE VALORES####
n = s = q = 0
while True:
    n = int(input('Digite um numero:[999 para terminar] '))
    if n == 999:
        break
    s+=n
    q+=1
print(f'A soma dos valores foi:{s}\nCom um total de {q} valores')

c = 1
while True:
    print(c, end=' ')
    if c == 100:
        break
    c+=1
