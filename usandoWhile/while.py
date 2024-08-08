"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':

        break # é usado para encerra o bloco de codigo

print('Acabou')

# o script so termina se o usuario digitar a palavra 'sair'