class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}")
        else:
            print("Valor de depósito inválido.")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}")
        else:
            print("Valor de saque inválido ou saldo insuficiente.")

    def ver_extrato(self):
        print(f"Extrato da conta {self.numero_conta} - Saldo: R${self.saldo}")

    def transferencia(self, outra_conta, valor):
        if valor > 0 and valor <= self.saldo:
            self.saque(valor)
            outra_conta.deposito(valor)
            print(f"Transferência de R${valor} realizada com sucesso para a conta {outra_conta.numero_conta}.")
        else:
            print("Valor de transferência inválido ou saldo insuficiente.")

# Exemplo de uso
if __name__ == "__main__":
    # Criando duas contas
    conta1 = ContaBancaria(numero_conta=1, titular="João", saldo=1000.0)
    conta2 = ContaBancaria(numero_conta=2, titular="Maria", saldo=500.0)

    # Realizando operações
    conta1.ver_extrato()
    conta1.deposito(200.0)
    conta1.saque(50.0)
    conta1.ver_extrato()

    conta2.ver_extrato()
    conta1.transferencia(conta2, 100.0)
    conta2.ver_extrato()
