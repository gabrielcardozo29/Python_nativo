print("BANCO")
opcao = 0
saldo_atual = 0
while opcao != 4:
    opcao = int(input("***MENU*** \n [1]Depósito \n [2]Saque \n [3]Extrato \n [4]Sair \n"))
    
    if opcao == 1:
        deposito = float(input("Digite o Valor para depósito."))
        saldo_atual += deposito #mesma coisa que saldo_atual = saldo atual + valor
        print(f"Seu Saldo atual é de R${saldo_atual:.2f}")
        print("Deseja realizar mais alguma transação?")

    elif opcao == 2:
        saque = float(input("Digite o valor desejado para saque: "))
        if saque <= saldo_atual:
            saldo_atual -= saque
            print(f"Saque realizado com sucesso, seu saldo atual é de R${saldo_atual:.2f}")
            print("Deseja realizar mais alguma transação?")
        else:
            print("Saldo insuficiente, verifique seu saldo e tente novamente.")
    
    elif opcao == 3:
        print(f"Seu saldo atual é de R${saldo_atual:.2f}")
        print("Deseja realizar alguma transação?")
    
    elif opcao != 4:
        print("Opção incorreta, seleciona uma opção válida do menu.")


else:
   print("Obrigado por usar nosso sistema.")