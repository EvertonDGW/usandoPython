"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break


print('Acabou')
"""
quando o contador for igual 6 a mensagem 'Não vou mostrar o 6.' é exibida,
o continue é usado para encerrar qualquer linha de codigo para o 6,
em seguida o codigo volta para o inicio a parti do numero 7, ou seja,
apos o contador chegar em 6 o continue não executada mais nada para o 6, 
apenas para o proxima valor que é o 7 é o valores restantes
"""