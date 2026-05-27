# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
print(num1 + num2)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
divisao = int(input("Digite um número: "))
print(divisao % 5)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
print('Vamos multiplicar dois números!')
mult1 = int(input('Digite o primeiro número: '))
mult2 = int(input('Digite o segundo número: '))
mult_res = mult1 * mult2
print(f'O resultado da multiplicação é: {mult_res}')

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
try:
    div_1 = int(input("Digite o primeiro número: "))
    div_2 = int(input("Digite o segundo número: "))
    div_res = div_1 / div_2
    print(f'O resultado foi: {div_res}')
except:
    print('Parece que ocorreu um erro')

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
quad = int(input('Digite um número para calcular o quadrado: '))
print(f'O quadrado de {quad} é: {quad ** 2}')

# #### Números de Ponto Flutuante (`float`)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
val_1 = float(input('Digite um número flutuante: '))
val_2 = float(input('Digite outro número flutuante: '))
soma_float = val_1 + val_2
print(f'O resultado é {soma_float}')

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
med_1 = int(input('Digite um número: '))
med_2 = int(input('Digite outro número: '))
media = float(med_1 + med_2) / 2
print(f'A média é: {media}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base_1 = int(input("Digite o número base: "))
potencia_1 = int(input('Digite a potência: '))
res_pot = float(base_1 ** potencia_1)
print(f'O resultado da potência é: {res_pot}')

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = int(input('Digite a temperatura em Celsius: '))
conversor = float((celsius * 9/5) + 32)
print(f'A temperatura em Fahrenheit é: {conversor}')

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math
pi = math.pi
raio = float(input('Digite o raio do cirulo'))
area_circulo = pi * raio ** 2
print(f'A área do circulo é: {area_circulo}')

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

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
# 25: Conversão de Tipo com Validação
