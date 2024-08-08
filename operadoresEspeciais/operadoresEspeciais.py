
# vamos aprender a usar os operados:
# Flags, is, is not e None

print(20 * '-')
# usando none
def verificar_status(status):
    if status is None:
        return "Status não definido"
    return f"Status é {status}"

status = None
print(verificar_status(status))  # Resultado: Status não definido

status = "Ativo"
print(verificar_status(status))  # Resultado: Status é Ativo


print(20 * '-')

# usando is para verificar se as variaveis apontam para o mesmo ID na memoria
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # Resultado: True (a e b são o mesmo objeto)
print(a is c)  # Resultado: False (a e c são objetos diferentes com o mesmo conteúdo)

print(20 * '-')

#usando is not para verificar se as variaveis não apontam para o mesmo objeto da memoria
# ou seja, estamos verificando se eles são diferentes

x = 42
y = 42
z = 43

print(x is not y)  # Resultado: False (x e y referem-se ao mesmo objeto int)
print(x is not z)  # Resultado: True (x e z são objetos diferentes)

print(20 * '-')

#usando flags 
# Usando flags para indicar diferentes modos de execução

modo_versao = "debug"  # Pode ser "debug" ou "release"
modo_verbose = True    # Flag para ativar modo verbose

if modo_versao == "debug":
    print("Executando no modo de depuração")
    
if modo_verbose:
    print("Modo verbose ativado")

# Alterando a flag
modo_verbose = False

if not modo_verbose:
    print("Modo verbose desativado")