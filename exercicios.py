import math
from datetime import datetime

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
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números


    numero = int(input("digite um numero: "));
if isinstance(numero, int):
    print("A variavel é um numero")
else: 
    print("A variavel não é um numero")

# 25: Conversão de Tipo com Validação

