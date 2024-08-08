

# os operador not in e in significam: não estar entre e estar entre exemplo:

nome = 'Otávio'
print(nome[2])
print(nome[-4])
print('vio' in nome) #verificando se existe a string vio no nome otavio
print('zero' in nome) #verificando se existe a string zero no nome otavio
print(10 * '-')
print('vio' not in nome) # verificando se não existe a string vio no nome otavio
print('zero' not in nome)

# digite seu nome no input em seguida responda que caracteres voce quer encontra no seu nome
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')