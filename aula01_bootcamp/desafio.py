# O programa deve começar solicitando ao usuário que insira seu nome.
# Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário.
# Considere que este valor pode ser um número decimal.
# Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
# O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
# Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".

print("Vamos calcular o seu bônus!")

valor_constante = 1000
nome_usuario = input("Digite seu nome: ")

salario_usuario = float(input("Digite o seu salário: "))

bonus = float(input("Digite a porcentagem do bônus: "))

valor_final = float(valor_constante + salario_usuario * bonus)

print(f"Olá {nome_usuario}, o seu valor bônus foi de R${valor_final}")
