# a converção de valores e classificada em tres 3 grupos, são eles: 
"""
Type Conversion (Conversão de Tipo): Isso é quando você decide mudar um tipo de dado para outro. Tipo, se você tem um número e quer transformá-lo em texto, você faz uma conversão de tipo. É algo que você faz de propósito.

Typecasting (Casting de Tipo): É o mesmo que conversão de tipo, mas com um nome diferente. A diferença é que “casting” é um termo mais genérico e você pode usá-lo em várias linguagens de programação. Basicamente, é só um jeito de falar sobre mudar o tipo de dado.

Coercion (Coerção): Isso acontece quando o Python faz a conversão de tipo automaticamente sem você pedir. Por exemplo, se você soma um número e um texto e o Python faz a mágica para você, isso é coerção. O Python tenta fazer a coisa certa automaticamente para que o código funcione.

"""
# exemplo:

# Type Conversion (Conversão de Tipo)
numero = 123
texto = "o numero é: " + str(numero)
print(texto) # retorna uma string (str)

# Typecasting (Casting de Tipo)
numeroFlutuante = 5.67 #numero de ponto flutuante
numeroInteiro = int(numeroFlutuante) # convertendo para um numero inteiro (int)
print(numeroInteiro)


# Coerção implícita
numero = 5
texto = "A resposta é: " + str(numero)  # Convertendo explicitamente para string
print(texto)

