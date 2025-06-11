menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        """
            1.Somente valores positivos
            2. Armazenar depósitos em uam variável e exibir no extrato.
        """
        valor = float(input("Informe o valor do depósito:"))
        
        if valor > 0:
            saldo+=valor
            extrato += f"Depósito: {valor:.2f}\n"
        else:
            print("Falha na operação ! Valor informado é inválido !")

        
    elif opcao == "s":
        """
            1. Permitir 3 saques diários com limite de R$500,00 por saque
            2. Emitir mensagem quando o não houver saldo disponível.
            3. Saques armazenados em uma variável e exibir no extrato.
        """
        
        valor = float(input("Informe o valor do saque:"))

        if valor > saldo:
            print("Saldo insuficiente !")
            
        elif valor > limite:
            print("Valor superior ao limite diário permitido !")

        elif numero_saques >=LIMITE_SAQUES:
            print("Limite de saques diário, atingido !")

        elif saldo > 0:

            saldo-=valor
            numero_saques+=1
            extrato+=f"Saque: {valor:.2f}\n"
            print("Saque realizado com sucesso !")
           

        else:
            print("Valor infomado inválido !")

           
    elif opcao == "e":
        
        if extrato != "":

         print("-------------- Extrato --------------")
         print("Movimentações:\n")
         print(extrato)
         print("\n-----------------------------------")
         print(f"Saldo atual: {saldo:.2f}")

        else:
            print("Não foram realizadas movimentações !")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
