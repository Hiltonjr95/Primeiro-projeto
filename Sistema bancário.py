menu = """
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

"""
extrato=""
saldo = 0
limite = 500
numero_saque=0
LIMITE_SAQUE=3

while  True:
  print(menu)
  opcao = int(input("Digite a opçao desejada:"))

  if (opcao == 1):
    valor_deposito= float(input("Quanto voçê quer depositar?:"))
    if (valor_deposito>0):
      print("valor depositado com sucesso:")
      saldo += valor_deposito
      extrato += f"Depósito: R$: {valor_deposito:.2f}\n"
      
      
    else:
     print("Valor inválido.")

  elif(opcao==2):
    valor_saque=float(input("Digite o valor que deseja sacar:"))
    if(valor_saque>saldo):
      print("Saldo insuficiente")
    elif(valor_saque>limite):
      print("Valor excede o limite de saque")
    elif(numero_saque>=LIMITE_SAQUE):
      print("Limite de saque diário excedido")
    
    elif(valor_saque>0):
      saldo-= valor_saque
      extrato+= f"Saque: R${valor_saque:.2f}\n"
      numero_saque+= 1

    else:
      print("O valor informado é inválido")

  elif(opcao==3):
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:R${saldo:.2f}")

  elif(opcao==4):
    break
  else:
    print("Operação inválida, tente novamente.")
 
       