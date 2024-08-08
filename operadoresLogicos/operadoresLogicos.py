# operador logico end : significa 'e'. o operador end retorna true se ambas condicoes forem verdadeiras
print('operador logico end')
a = 10
b = 5

if a > 0 and b > 0:
    print("Ambos a e b são verdadeiros")
else:
    print("Pelo menos um dos valores é false")

print('  ')
#----------------------------------------------------------------------------------------------------------------------------------------------------

print('operador logico or')
# o operador logico or significa 'ou'. o operador or retorna true se pelo menos uma das condicoes forem verdadeiras
a = -10
b = 5

if a > 0 or b > 0:
    print("Pelo menos um dos valores é verdadeiro")
else:
    print("Nenhum dos valores é verdadeiro")

print('  ')
#-----------------------------------------------------------------------------------------------------------------------------------------------------

print('operador logico not')
# o operador logico not é usado para inverte um valor ou condicao
# note que a condicao é 'a MENOR que 0', mas o operador not esta invertendo isso, ou seja, a condicao é: 'a MAIOR que 0'
# basicamente o operador not ele inverte o resultado de true para false ou false para true
# nesse exemplo a condicao resulta em false, mas o not inverte o resultado para true
a = 10

if not (a < 0):
    print("a não é negativo")
else:
    print("a é negativo")