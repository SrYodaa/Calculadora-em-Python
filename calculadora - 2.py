import math

print("Bem-Vindo à Calculadora")

# Função para 'Adicionar'
def add(x, y):
    return x + y      

# Função para 'Subtrair'
def subtract(x, y):
    return x - y

# Função para 'Multiplicar'
def multiply(x, y):
    return x * y

# Função para 'Dividir'
def divide(x, y):
    if y == 0:
        return "Erro! Divisão por Zero."
    return x / y

# Função para 'Potencia'
def power(x, y):
    return x ** y

# Função para 'Raiz Quadrada'
def sqrt(x):
    if x < 0:
        return "Erro! Raiz quadrada de número negativo."
    return math.sqrt(x)

def calculator():
    # Função principal para executar a calculadora
    print("Selecione a operação")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    
    # Solicitar ao usuário que selecione a operação
    choice = input("Digite sua escolha (1/2/3/4/5/6): ")
    
    # Verificar se a escolha é válida
    if choice in ['1', '2', '3', '4', '5', '6']:
        if choice == '6':
            num = float(input("Digite o número: "))
            print(f"A raiz quadrada de {num} é {sqrt(num)}")
        else:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
    else:
        print("Escolha inválida!")

# Executar a calculadora
calculator()