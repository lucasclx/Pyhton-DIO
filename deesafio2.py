saldo_conta = 0
limite_saque = 500
registro_extrato = ""
numero_saque_efetuados = 0
LIMITE_SAQUES_CONSTANTE = 3

def operacao_deposito():
    global saldo_conta, registro_extrato
    valor_deposito = float(input("Informe o valor do depósito: "))
    if valor_deposito > 0:
        saldo_conta += valor_deposito
        registro_extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

def operacao_saque():
    global saldo_conta, registro_extrato, numero_saque_efetuados
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

def operacao_extrato():
    global saldo_conta, registro_extrato
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not registro_extrato else registro_extrato)
    print(f"\nSaldo: R$ {saldo_conta:.2f}")
    print("==========================================")

def operacao_sair():
    global continua
    continua = False

def menu_principal():
    opcao_menu = input("""
    Depositar - aperte |d|
    Sacar - aperte |s|
    Extrato - aperte |e|
    Sair - aperte |q|

    => """)
    
    if opcao_menu == "d":
        operacao_deposito()
    elif opcao_menu == "s":
        operacao_saque()
    elif opcao_menu == "e":
        operacao_extrato()
    elif opcao_menu == "q":
        operacao_sair()
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

continua = True
while continua:
    menu_principal()
