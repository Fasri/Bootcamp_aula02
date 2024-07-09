import math

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# primeiro_numero = int(input("Digite o primeiro número: "))
# segundo_numero = int(input("Digite o segundo número: "))
# print(f"A soma é {primeiro_numero+segundo_numero}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# numero = int(input("Insira um número para saber o resto da divisão por 5: "))
# resto = numero//5
# print(f"O resto da divisão por 5 é {resto}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# primeiro_numero = int(input("Digite o primeiro número: "))
# segundo_numero = int(input("Digite o segundo número: "))
# resultado = primeiro_numero*segundo_numero
# print(f"A multiplicação é {resultado}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# primeiro_numero = int(input("Digite o primeiro número: "))
# segundo_numero = int(input("Digite o segundo número: "))
# resultado = primeiro_numero/segundo_numero
# print(f"A divisão é {resultado}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# numero = int(input("Digite um numero para saber seu quadrado: "))
# quadrado = numero**2
# print(f"O quadrado de {numero} é {quadrado}")

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# primeiro_numero = float(input("Digite o primeiro número: "))
# segundo_numero = float(input("Digite o segundo número: "))
# print(f"A soma é {primeiro_numero+segundo_numero}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# primeiro_numero = float(input("Digite o primeiro número: "))
# segundo_numero = float(input("Digite o segundo número: "))
# media = (primeiro_numero+segundo_numero)/2
# print(f"A média é de {primeiro_numero} e {segundo_numero} é {media}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# numero = float(input("Digite o número para calculo da pontência: "))
# expoente = float(input("Digite o qual o expoente: "))
# potencia = numero**expoente
# print(f"A potência de {numero} de expoente {expoente} é {potencia}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input("Digite a temperatura em celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"A temperatura em Fahrenheit é {fahrenheit}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = float(input("Digite o raio do círculo para calcular a área: "))
# area = math.pi*raio**2
# print(f"A área do círculo é {area}")

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# palavra = input("Digite uma String: ")
# maiuscula = palavra.upper()
# print(maiuscula)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = input("Digite um nome: ")
# nome_modificado = nome.lower()
# print(nome_modificado)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input("Digite uma frase: ")
# frase_sem = frase.strip()
# print(frase_sem)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input("Digite a data no formato dd/mm/aaaa")
# data_separada = data.split("/")
# dia = data_separada[0]
# mes = data_separada[1]
# ano = data_separada[2]
# print(f"O dia é {dia}, o mês é {mes} e o ano é {ano}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# string1 = input("Digite a primeira String: ")
# string2 = input("Digite a segunda String: ")
# string_concatenada = string1 + string2
# print(string_concatenada)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# bool1 = True
# bool2 = True
# resultado = bool1 and bool2
# print("O resultado do AND é :", resultado)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# bool1 = False
# bool2 = False
# resultado = bool1 or bool2
# print("O resultado do OR é :", resultado)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# bool1 = False
# bool_not = not bool1
# print("Resultado do NOT é: ", bool_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# numero1 = 4
# numero2 = 4
# resultado = (numero1 == numero2)
# print("O resultado sa igualdade é : ", resultado)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# numero1 = int(input("Digite o primeiro número: "))
# numero2 = int(input("Digite o segundo número: "))
# resultado = (numero1 != numero2)
# print("O resultado da diferença é: ", resultado)

# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
# try:
#     celsius = float(input("Digite a temperatura em celsius: "))
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"A temperatura em Fahrenheit é {fahrenheit}")
# except ValueError:
#     print("Digite um valor válido para a temperatura em Celcius")


# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# palavra = input("Digite uma palavra ou frase: ")
# if isinstance(palavra, str):
#     palavra = palavra.replace(" ", "").lower()
#     palavra_invertida = palavra[::-1]
#     if palavra == palavra_invertida:
#         print(f"A palavra {palavra} é palíndromo")
#     else:
#         print(f"A palavra {palavra} não é palíndromo, a palavra invertida fica {palavra_invertida}")
# else:
#     print("Entrada invalida, Por favor, digite uma palavra ou frase")

# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.
try:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    ope = input("Qual operação vai ser realizada? Digite +, -, x ou /")
    if ope == "+":
        resultado = num1 + num2
        print(f"A soma é {resultado}")
    elif ope == "-":
        resultado = num1 - num2
        print(f"A subtração é {resultado}")
    elif ope == "x":
        resultado = num1 * num2
        print(f"A multiplicação é {resultado}")
    elif ope == "/":
        resultado = num1 / num2 and num2 != 0
        print(f"A divisão é {resultado}")
    else:
        print("Operador invalido ou divisão por zero")

except ValueError:
    print("Apenas números!")

# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.



