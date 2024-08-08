import math
from datetime import datetime
'''
# #### Inteiros (`int`)
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num11 = int(input('Digite um numero para numerador: '));
num12 = int(input('Digite um numero para denominador: '));
print("adição")
print(num11+num12);

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num21 = int(input('Digite um numero para dividir por 5: '));
print("divisao por 5")
print (num21/5) # Retorna a divisão
print (num21//5) # Retorna a parte inteira da divisão
print (num21%5) # Retorna o resto da divisão tipo, 7/5 da 1 de divisão e sobra 2

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
print("multiplicação")
print(num11 * num12);

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
print("divisão")
print(num11/num12);

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
print("quadrado")
print(num11**num12);

# #### Números de Ponto Flutuante (`float`)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
num61 = float(input('Digite um numero para numerador: '));
num62 = float(input('Digite um numero para denominador: '));
print("adição")
print(num61+num62);

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
membros = [num61,num62]
media = sum(membros)/len(membros)
print(f"a mpedia é {media}");

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
potencia = num61**num62
print(f"A potencia é {potencia}");

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celcius = float(input('Digite um a temperarua: '));
fahrenheit = (celcius * 9/5) + 32
print(f"O grau Celcius {celcius} equivale a {fahrenheit} graus fahrenheit")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio: "));
area =  math.pi * raio ** 2
print(f"area do circulo é {area}");

# #### Strings (`str`)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
txt = str(input('Digite uma fraze: '));
upper = txt.upper();
print(upper);

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
lower = txt.lower();
print(lower);

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
strip = txt.replace(" ","");
print(strip);

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
try:
    date = (input('Digite uma data no formato dd/mm/aaaa: '));
    date2 = datetime.strptime(date, '%d/%m/%Y').date();
    print(date2);
    #year = datetime.strptime(date, '%d/%m/%Y').year();
    #print(year)
    year = date2.year
    print(year)
    day = date2.day
    print(day)
    month = date2.month
    print(month)
except:
    print("deu erro")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
try:
    str1 = (input('Digite uma palavra: '));
    str2 = (input('Digite uma palavra: '));
    print(str1+" "+str2);
except:
    print("deu erro")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
valor1 = True
valor2 = False
resultado_and = valor1 or valor2
print("Resultado do OR lógico:", resultado_and)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
valor1 = True
resultado_and = not valor1 
print("Resultado do OR lógico:", resultado_and)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
valor1 = "Alan"
valor2 = "Alan "
resultado_and = (valor1 == valor2)
print("Resultado do OR lógico:", resultado_and)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
valor1 = "Alan"
valor2 = "Alan "
resultado_and = (valor1 != valor2)
print("Resultado do OR lógico:", resultado_and)

# #### try-except e if

# 21: Conversor de Temperatura
try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F.")
except ValueError:
    print("Por favor, digite um número válido para a temperatura.")

# 22: Verificador de Palíndromo
entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# 23: Calculadora Simples
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")

# 24: Classificador de Números
try:
    numero =int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    elif numero == 0:
        print("Zero")
    else:
        print("Verificar")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
'''
# 25: Conversão de Tipo com Validação

#entrada_lista = input("Digite uma lista de números separados por vírgula: ")
entrada_lista = "5,8,9,8,9,8,a"
numeros_str = entrada_lista.split(",")
print(entrada_lista)
print(numeros_str)
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")