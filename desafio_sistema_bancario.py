import textwrap

def menu():
    menu = """ \n
    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [nc] \tNova Conta
    [lc] \tListar Contas
    [nu] \tNovo Usuario
    [q]  \tSair
    """
    return input(textwrap.dedent(menu))

# Função de depósito
def depositar(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função de saque
def sacar(*, saldo, extrato, limite, numero_saques):
    LIMITE_SAQUES = 3
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

# Exibir extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Função para criar usuário
def criar_usuario(usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario_existente = filtrar_usuarios(cpf, usuarios)
    
    if usuario_existente:
        print("Usuário já cadastrado.")
        return
    
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento do usuário: ")
    endereco = input("Informe o endereço do usuário: ")
    
    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário cadastrado com sucesso.")

# Função para filtrar usuários pelo CPF
def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrado[0] if usuarios_filtrado else None

# Função para criar conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("\nConta criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado.")

# Função para listar contas
def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']} - Conta: {conta['numero_conta']} - CPF: {conta['usuario']['cpf']}")

# Função principal
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    AGENCIA = "0001"
    NUMERO_CONTA = 1

    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            conta = criar_conta(AGENCIA, NUMERO_CONTA, usuarios)
            if conta:
                contas.append(conta)
                NUMERO_CONTA += 1

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Opção inválida, por favor selecione novamente.")

# Chamar a função principal para rodar o programa
if __name__ == "__main__":
    main()
