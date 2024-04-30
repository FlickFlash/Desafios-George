def numeric_operation():
    op = input("Qual operação deseja realizar? Soma [+], subtração [-], multiplicação [*] ou divisão [/]: ")
    while not op in ["+", "-", "*", "/"]:
        op = input("Escolha inválida! Digite somente o símbolo da operação: [+], [-], [*], [/]:")

    number_1 = input("Digite um número: ")
    while not number_1.isnumeric():
        number_1 = input("Valor inválido! Digite um número válido: ")
    number_1 = int(number_1)


    number_2 = input("Digite outro número: ")
    while not number_2.isnumeric():
        number_2 = input("Valor inválido! Digite outro número válido: ")
    number_2 = int(number_2)

    print(f"Calculando ( {number_1} {op} {number_2} ) ...")
    print("O resultado é ", end="")

    match op:
        case "+":
            print(number_1 + number_2)
        case "-":
            print(number_1 - number_2)
        case "*":
            print(number_1 * number_2)
        case "/":
            print(number_1 / number_2)

numeric_operation()