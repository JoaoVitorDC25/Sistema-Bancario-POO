class SaldoInsuficienteError(Exception):
    
    """
        Exceção levantada quando uma operação de saque excede saldo.
    """
    
    def __init__(self, saldo_atual, valor_saque, mensagem="Saldo insuficiente para realizar o saque."):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        self.mensagem = f"{mensagem} Saldo atual: R${saldo_atual:.2f}, Tentativa de saque: R${valor_saque:.2f}"
        
        super().__init__(self.mensagem)
    
class ContaInexistenteError(Exception):
    
    """
        Exceção levantada ao tentar operar conta inexistente 
    """
    
    def __init__(self, numero_conta, mensagem = "A conta especificada não foi encontrada."):
        self.numero_conta = numero_conta
        self.mensagem = f"{mensagem} Número da conta: {numero_conta}"
    
        super().__init__(self.mensagem)
        
        