agenda = {}

while True:
    print()
    print("********MENU********\n")
    print("[1] - Todos os contatos\n[2] - Novo contato\n[3] - Buscar contato\n[4] - Excluir contato\n[5] - Sair")
    print()

    opcao = input("Digite uma opção: ")
    if opcao.isdigit():
        opcao = int(opcao)
        if opcao == 1:
            if not agenda:  # Verifica se a agenda está vazia
                print("Agenda vazia, selecione uma nova opção abaixo")
            else:
                for nome, telefone in agenda.items():  # Itera sobre os itens da agenda
                    print(f"{nome}: {telefone}")


        elif opcao == 2:  # Adiciona um novo contato à agenda
            nome = input("Nome: ").strip()
            while True:
                telefone = input("Telefone (Apenas número): ").strip()
                telefone = ''.join(filter(str.isdigit, telefone))
                if len(telefone) != 11:
                    print("Número inválido! Certifique-se de digitar os 11 dígitos corretamente.")
                else:
                    telefone_formatado = f"({telefone[:2]}) {telefone[2]}.{telefone[3:7]}-{telefone[7:]}"
                    agenda[nome] = telefone_formatado
                    print(f"Contato {nome} de telefone {telefone_formatado} foi adicionado com sucesso.")
                    break
                

        elif opcao == 3:  # Busca um contato na agenda
            while True:
                nome = input("Digite o nome do contato: ").strip()
                if nome in agenda:
                    print(f"{nome} - {agenda[nome]}")
                    break
                else:
                    print("Contato não encontrado. Tente novamente.")

        elif opcao == 4:  # Exclui um contato da agenda
            while True:
                nome = input("Digite o nome do contato: ").strip()
                if nome in agenda:
                    del agenda[nome]
                    print(f"O contato {nome} foi excluído com sucesso.")
                    break
                else:
                    print("Contato não encontrado. Tente novamente.")

        elif opcao == 5:  # Encerra o programa
            print("Obrigado por usar nosso sistema, volte sempre!")
            break

        else:
            print("Opção inválida. Por favor, insira uma opção válida de 1 a 5.")
    else:
        print("Opção inválida. Por favor, insira uma opção válida de 1 a 5.")
  