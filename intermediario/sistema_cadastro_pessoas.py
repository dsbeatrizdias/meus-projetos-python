#Um programa no terminal onde o usuário pode:
#cadastrar pessoas
#listar pessoas
#sair do sistema

pessoas = []

while True:
    print("\n1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))

        pessoa = {
            "nome": nome,
            "idade": idade
        }

        pessoas.append(pessoa)
        print("Pessoa cadastrada com sucesso!")

    elif opcao == "2":
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
            for p in pessoas:
                print(f"Nome: {p['nome']} | Idade: {p['idade']}")

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")