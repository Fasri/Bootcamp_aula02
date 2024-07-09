CONSTANTE_BONUS = 1000

# 1) Solicite ao usuário que digite seu nome
try:
    nome_usuario = input("Digite seu nome: ")
    if len(nome_usuario) ==0:
        raise ValueError("O nome está vazio.")
        exit()
    elif any(char.isdigit() for char in nome_usuario):
        raise ValueError("O nome não deve conter números.")
        exit()
    elif nome_usuario.isspace():
        print("Você só digitou espaço!")
        exit()
    else:
        print("Nome válido: ", nome_usuario)
except ValueError as e:
    print(e)
    exit() 

# 2) Solicite ao usuário que digite o valor do seu salário
# Converta a entrada para um número de ponto flutuante
try:
    salario_usuario = float(input("Digite seu salário: "))
    if salario_usuario< 0:
        print("O sálario tem que ser um valor positivo!")
        exit()
except ValueError:
    print("Digite um número para o sálario!")
    exit()

# 3) Solicite ao usuário que digite o valor do bônus recebido 
# Converte a entrada para um número de ponto flutuante
try:
    bonus_usuario = float(input("Digite o valor do bônus: "))
    if bonus_usuario < 0:
        print("Digite um valor positivo!")
        exit()
except ValueError:
    print("Digite um número pa o bônus!")
    exit()

# 4) Calcule o valor do bônus final
valor_do_bonus = CONSTANTE_BONUS + salario_usuario*bonus_usuario

# 5) Imprima a mensagem persolazida incluindo o nome do usuário,e o valor do bônus
print(f"O usuário {nome_usuario} possui o bonus de {valor_do_bonus}")