# Módulo de Faturamento e Assinaturas de Clientes

# Banco de dados em memória utilizando dicionários
clientes = {}
planos = {}
assinaturas = {}


# Função responsável por cadastrar clientes
def cadastrar_cliente():
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
        if id_cliente < 0:
            raise ValueError("O ID não pode ser negativo.")
        if id_cliente in clientes:
            raise ValueError("Cliente já cadastrado.")
        nome = input("Digite o nome do cliente: ")
        clientes[id_cliente] = {
            "nome": nome
        }

    except ValueError as erro:
        print("Erro:", erro)
    else:
        print("Cliente cadastrado com sucesso!")
    finally:
        print("Operação de cadastro finalizada.\n")

# Função responsável por cadastrar planos
def cadastrar_plano():
    try:
        id_plano = int(input("Digite o ID do plano: "))
        if id_plano < 0:
            raise ValueError("ID inválido.")
        if id_plano in planos:
            raise ValueError("Plano já cadastrado.")
        nome = input("Nome do plano: ")
        valor = float(input("Valor mensal: "))
        meses = int(input("Quantidade de meses: "))
        if valor <= 0:
            raise ValueError("Valor deve ser maior que zero.")
        if meses <= 0:
            raise ValueError("Quantidade de meses inválida.")

        planos[id_plano] = {
            "nome": nome,
            "valor": valor,
            "meses": meses
        }

    except ValueError as erro:
        print("Erro:", erro)
    else:
        print("Plano cadastrado com sucesso!")
    finally:
        print("Operação de plano finalizada.\n")

# Função para criar uma assinatura para um cliente
def criar_assinatura():
    try:
        id_cliente = int(input("ID do cliente: "))
        if id_cliente not in clientes:
            raise KeyError("Cliente não encontrado.")
        id_plano = int(input("ID do plano: "))
        if id_plano not in planos:
            raise KeyError("Plano não encontrado.")
        id_assinatura = len(assinaturas) + 1

        assinaturas[id_assinatura] = {
            "cliente": id_cliente,
            "plano": id_plano,
            "valor_total":
            planos[id_plano]["valor"] *
            planos[id_plano]["meses"]
        }

    except KeyError as erro:
        print("Erro:", erro)
    except ValueError:
        print("Digite apenas números.")
    else:
        print("Assinatura criada com sucesso!")
    finally:
        print("Processo de assinatura encerrado.\n")

# Função para pesquisar cliente
def pesquisar_cliente():
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
        if id_cliente not in clientes:
            raise KeyError("Cliente não cadastrado.")
        print("\nCliente encontrado:")
        print(clientes[id_cliente])

    except KeyError as erro:
        print("Erro:", erro)
    except ValueError:
        print("ID inválido.")
    finally:
        print()

# Função para atualizar uma assinatura
def atualizar_assinatura():
    try:
        id_assinatura = int(input("ID da assinatura: "))
        if id_assinatura not in assinaturas:
            raise KeyError("Assinatura inexistente.")
        novo_plano = int(input("Novo ID do plano: "))
        if novo_plano not in planos:
            raise KeyError("Plano não encontrado.")
        assinaturas[id_assinatura]["plano"] = novo_plano

        assinaturas[id_assinatura]["valor_total"] = (
            planos[novo_plano]["valor"] *
            planos[novo_plano]["meses"]
        )

    except KeyError as erro:
        print("Erro:", erro)
    except ValueError:
        print("Digite valores válidos.")
    else:
        print("Assinatura atualizada.")
    finally:
        print()

# Função para listar informações do sistema
def listar_dados():
    print("\n--- CLIENTES ---")

    for cliente in clientes:
        print(cliente, clientes[cliente])

    print("\n--- PLANOS ---")

    for plano in planos:
        print(plano, planos[plano])

    print("\n--- ASSINATURAS ---")

    for assinatura in assinaturas:
        print(assinatura, assinaturas[assinatura])
        
    print()

# Função principal do sistema
def menu():
    while True:
        try:
            print("===== SISTEMA DE FATURAMENTO =====")
            print("1 - Cadastrar Cliente")
            print("2 - Cadastrar Plano")
            print("3 - Criar Assinatura")
            print("4 - Pesquisar Cliente")
            print("5 - Atualizar Assinatura")
            print("6 - Listar Dados")
            print("0 - Sair")
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                cadastrar_cliente()
            elif opcao == 2:
                cadastrar_plano()
            elif opcao == 3:
                criar_assinatura()
            elif opcao == 4:
                pesquisar_cliente()
            elif opcao == 5:
                atualizar_assinatura()
            elif opcao == 6:
                listar_dados()
            elif opcao == 0:
                print("Sistema encerrado.")
                break
            else:
                print("Opção inválida.")

        except ValueError:
            print("Digite somente números.\n")

# Inicialização do programa
menu()
