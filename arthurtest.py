d = int(input('Quantos dias o carro foi alugado? '))
k = float(input('Quantos km foram rodados?'))
print(f'O valor a ser cobrado é de {(d*60)+(k*0.15)}R$')
#-------------------------------------------------------------------
c = int(input('Qual a temperatura em Cº? '))
print(f'A temperatura em Fº é: {(c*9)/5+32}')
#-------------------------------------------------------------------------------------------------
f = int(input('Salario: '))
print(f'Ele ganhará {f*1.15}R$')
#-------------------------------------------------------------------------------------------------
p = int(input('Valor da roupa: '))
print(f'O desconto é de: {p*0.05} R$ e vc pagará {p*0.95} R$')
#-------------------------------------------------------------------------------------------------
l = int(input('Largura da parade? '))
c = int (input('Comprimento da parede? ' ))
print (f'A sua parede tem area de {l*c} M² e será nescessario: {(l*c)/2} Litros para pinta-la  ' )
#-------------------------------------------------------------------------------------------------
k = float(input('Quantos R$ vc tem? '))
print (f'Em dolar vc teria {k/3.27} U$')
#-------------------------------------------------------------------------------------------------
m =float(input('Digite o valor em metros: \n'))
print(f'Em centimetros temos: \n {m*100}cm \nEm milimetros: \n {m*1000}mm.')
#-------------------------------------------------------------------------------------------------
print('Olá, por favor informe suas notas')
n = float(input('Primeira nota: '))
n1 = float(input('Segunda nota: '))
n2 = float(input('Terceira nota: '))
n3 = float(input ('Quarta nota: '))
m = (n+n1+n2+n3)/4
print("Sua media é ", m )
#------------------------------------------------------------------------------------------------
q = int(input('Escreva um numero'))
print (f'O numero é {q}, seu dobro é {q*2}, seu triplo é {q*3} e sua raiz é {q**(1/2):.4f}')
'''{:.4f} é para indicar quantas casas decimais do resultado!'''
#-------------------------------------------------------------------------------------------------
a = int(input('Escreva um numero: '))
print(f'O numero foi {a}, seu sucessor é {a+1} e antecessor é {a-1}')

