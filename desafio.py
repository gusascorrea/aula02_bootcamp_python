CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome

nome_usuario = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
while True:
    try:
        salario_usuario = float(input("Digite o seu salario: "))
        if salario_usuario <= 0:
            print("Digite um salario válido")
            continue
        break
    except:
        print("Digite um salario válido")


# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
while True:
    try:
        bonus_usuario = float(input("Digite o seu bonus: "))
        if bonus_usuario < 0:
            print("Digite um bonus válido")
            continue
        break
    except:
        print("Digite um bonus válido")

# 4) Calcule o valor do bônus final

valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus
print(f"O usuario {nome_usuario} possui o bonus de {valor_do_bonus}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

# - Não há conferência do tipo de dados inserido
# - Não há conferência da coerência do dado inserido
# - O nome pode não estar na formatação correta do banco de dados (pode não nos dizer nada)
# - O salário pode ser negativo ou zero
# - O bônus pode ser zero ou negativo