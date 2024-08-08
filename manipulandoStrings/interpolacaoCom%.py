# vamos usar um tipo de formatação chamada interpolação com %


nome = 'Luiz'
preco = 1000.95897643

# o valor da variavel nome e jogado para dentro de %s
# o valor da variavel preço e jogado dentro de %.2f, em seguida  é formatado para exibir apenas 2 casas decimais

variavel = '%s, o preço é R$%.2f' % (nome, preco)


print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))