"""
um valor é considerado IMUTAVEL quando não é possivel altera-lo, se voce tentar altera-lo
um novo objeto com um novo identicador é criado
"""
print('exemplo com numbers')
a = 10
print(id(a)) # exibi o identicador unico do objeto 'a'

a = 20
print(id(a)) #exibi um identicador diferente , indicando que um novo objeto foi criado

print('    ')

print('exemplo com strings')

s = 'bom dia!'
print(id(s)) #vai ser exibido o identicador unico do objeto 's'

s = s + ' ' 'everton'
print(id(s)) #vai ser exibido um identificar diferente, por que criamos uma nova string

print('    ')

print('exemplo com tuplas')

t = (1,2,3,4)
print(id(t)) #vai exibir o identicador unico de 't'

t= t + (5,)
print(id(t)) # vai exibir um identificador diferente, porque adicionamos o numero 5 dentro da tupla, criando assim uma nova tupla

# basicamente quando um valor é reutilizado ou usado para criar uma nova string, number, tupla etc.. ele é considerado imutavel
