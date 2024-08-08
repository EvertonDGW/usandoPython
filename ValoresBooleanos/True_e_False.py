# Tipo de dado bool (boolean)
# Ao questionar algo em um programa,
# só existem duas respostas possíveis:
# sim (True) ou não (False).
# Existem vários operadores para "questionar".
# Dentre eles o ==, que é um operador lógico que
# questiona se um valor é igual a outro
print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))

# quando uma string for convertida para um valor booleano ela retorna true

print(bool('everton'))
print(bool(' ')) # A STRING NAO ESTA VAZIA, note que dentro das aspas EXISTE um espaço vazio, ou seja, existe algo la
print(bool('      ')) # A STRING NAO ESTA VAZIA, note que dentro das aspas EXISTE um espaço vazio, ou seja, existe algo la

# agora quando uma string vazia, ou seja, SEM ESPAÇO for convertida para um valor booleano ela retorna FALSE

print(bool('')) #note que NAO EXISTE nenhum espaço vazio entre as ASPAS, logo, retona false