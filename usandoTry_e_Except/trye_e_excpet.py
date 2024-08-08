numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str) #se a conversão do que o usuario digitar for bem sucedido para float então o try é executado
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:  # agora se o usuario digitar algo que nao possa ser convertido para float, então o except é executado
    print('Isso não é um número')

# ou seja se a conversação for bem sucedida o trye é executado, se nao o except é executado
