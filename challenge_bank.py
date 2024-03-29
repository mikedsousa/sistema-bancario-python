MENU = """
-------------------------
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair
-------------------------
"""

LIMITE_DE_SAQUES = 3
VALOR_MAXIMO_SAQUE = 500

numero_de_saques = 0
saldo = 500.00
movimentacao = ""

def main():
  while True:
    opcao = input(MENU)
    
    if opcao == "1":
      depositar()
      
    elif opcao == "2":
      sacar()
    
    elif opcao == "3":
      extrato()
    
    elif opcao == "4":
      print("Saindo...")
      break
  
    else:
      print("Opção inválida!")
  

# Função para depositar dinheiro
def depositar():
  # Variáveis globais
  global saldo
  global movimentacao 
  
  valor = float(input("Digite o valor do depósito: "))
  
  if valor <= 0:
    print("Valor inválido!")
    return
  
  saldo += valor
  print(f"Depósito de R${valor:.2f} realizado com sucesso!")
  print(f"Saldo atual: R${saldo:.2f}")
  movimentacao += f"Depósito de R${valor:.2f}\n"

  
  
# Função para sacar dinheiro 
def sacar():
  # Variáveis globais
  global saldo
  global numero_de_saques
  global movimentacao
  
  if numero_de_saques >= LIMITE_DE_SAQUES:
    print("Limite de saques atingido!")
    return
  
  valor = float(input("Digite o valor do saque: "))
  
  if valor > VALOR_MAXIMO_SAQUE:
    print(f"O valor máximo de saque é de R${VALOR_MAXIMO_SAQUE:.2f}")
    return
  
  if valor > saldo:
    print("Saldo insuficiente!")
    return
  
  saldo -= valor
  numero_de_saques += 1
  
  print(f"Saque de R${valor:.2f} realizado com sucesso!")
  print(f"Saldo atual: R${saldo:.2f}")
  movimentacao += f"Saque de R${valor:.2f}\n"
  
  
def extrato():
  global movimentacao
  print(movimentacao)
  print(f"Saldo atual: R${saldo:.2f}")
  
  
main()