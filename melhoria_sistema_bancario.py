
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "001"
usuarios = []
contas = []


def menu():

    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar usuário
    [c] Criar conta
    [lc] Listar contas
    [q] Sair

    => """
    return menu


#Depositar
def deposito(saldo,valor,extrato):
           
    if valor > 0:
            saldo+=valor
            extrato += f"Depósito: {valor:.2f}\n"
            print("Depósito realizado com sucesso !")
            
    else:
            print("Falha na operação ! Valor informado é inválido !")

    return saldo,extrato;


#Sacar
def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):

    
    if valor > saldo:
            print("Saldo insuficiente !")
            
    elif valor > limite:
            print("Valor superior ao limite diário permitido !")

    elif numero_saques >= limite_saques:
            print("Limite de saques diário, atingido !")

    elif valor > 0:

            saldo-=valor
            extrato+=f"Saque: {valor:.2f}\n"
            numero_saques+=1
            print("Saque realizado com sucesso !")
           

    else:
            print("Valor infomado inválido !")

    return saldo,extrato,numero_saques;


#Extrato
def mostra_extrato(saldo,/,extrato):
    if not  extrato == False:

         print("-------------- Extrato --------------")
         print("Movimentações:\n")
         print(extrato)
         print("\n-----------------------------------")
         print(f"Saldo atual: {saldo:.2f}")

    else:
            print("Não foram realizadas movimentações !")

    return saldo, extrato;


#Criar usuário
def criar_usuario(usuarios):


    cpf = input("Informe somente os números do cpf:")
    usuario = verifica_usuario(cpf,usuarios)

    if usuario:
          print("CPF já cadastrado !")
          return
         
    nome = input("Informe o nome:")
    data_nascimento = input("Informe a data de nascimento:")
    endereco = input("Informe o endereço (Logradouro, Nº - Bairro - Cidade/UF):")
         
    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})

    print(f"Nome:{nome}\nData de nascimento:{data_nascimento}\nCPF:{cpf}\nEndereço:{endereco}")



#Verifica se cpf já está cadastrado
def verifica_usuario(cpf,usuarios):
      consulta = [user for user in usuarios if user["cpf"]==cpf]
      return consulta[0] if consulta else None


def criar_conta(agencia,numero,usuarios):
    

      cpf = input("Informe somente os números do cpf:")

      usuario = verifica_usuario(cpf,usuarios)

      if usuario:
          
            print("\n Conta criada com sucesso !")
            return {"agencia":agencia,"numero":numero,"usuario":usuario}
      else:
            print("Usuário não identificado !")



def listagem_contas(contas):
      for c in contas:
            
            print(f"""\
              Agência:\t{conta['agencia']}
              C/C:\t\t{conta['numero']}
              Titular:\t{conta['usuario']['nome']}
             """)
        
         
    


while True:

    opcao = input(menu())

    if opcao == "d":

        valor = float(input("Informe o valor do depósito:"))
        
        saldo, extrato = deposito(saldo,valor,extrato)      
     

        
    elif opcao == "s":
        
        valor = float(input("Informe o valor do saque:"))
       
        saldo , extrato, numero_saques = saque(
            saldo = saldo, 
            valor = valor, 
            extrato = extrato, 
            limite = limite, 
            numero_saques = numero_saques, 
            limite_saques = LIMITE_SAQUES
            )
           
    

    elif opcao == "e":

        mostra_extrato(saldo, extrato=extrato)      

    
    elif opcao == "u":
          
        criar_usuario(usuarios)

    elif opcao == "c":
          
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "lc":
          listagem_contas(contas)

       
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
