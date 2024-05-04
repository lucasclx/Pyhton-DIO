menu_principal = """

Depositar - aperte |d|
Sacar - aperte |s|
Extrato - aperte |e|
Sair - aperte |s|

=> """

saldo_conta = 0
limite_saque = 500
registro_extrato = ""
numero_saque_efetuados = 0
LIMITE_SAQUES_CONSTANTE = 3

while True:

    opcao_menu = input(menu_principal)

    if opcao_menu == "d":
        valor_deposito = float(input("Informe o valor do depósito: "))

        if valor_deposito > 0:
            saldo_conta += valor_deposito
            registro_extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao_menu == "s":
        valor_saque = float(input("Informe o valor do saque: "))

        excedeu_saldo_disponivel = valor_saque > saldo_conta

        excedeu_limite_saque = valor_saque > limite_saque

        excedeu_numero_saques = numero_saque_efetuados >= LIMITE_SAQUES_CONSTANTE

        if excedeu_saldo_disponivel:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite_saque:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_numero_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor_saque > 0:
            saldo_conta -= valor_saque
            registro_extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saque_efetuados += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao_menu == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not registro_extrato else registro_extrato)
        print(f"\nSaldo: R$ {saldo_conta:.2f}")
        print("==========================================")

    elif opcao_menu == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
