import config as cfg

from abc import ABC, abstractmethod
from datetime import datetime
from utils.exceptions import SaldoInsuficienteError


class Conta(ABC):
    
    """
        Classe base abstrata que representa uma conta bancária.
    """
    _total_contas = 0  # Atributo de classe para rastrear o número total de contas
    
    def __init__(self, numero: int, cliente):
        
        """
            Inicializa uma nova conta bancária.
            
            Args:
                numero (int): O número da conta.
                cliente (Cliente): O cliente associado à conta.
        """
        super().__init__()
        self._numero = numero
        self._saldo = 0.0
        self._cliente = cliente
        self._historico = []
        Conta._total_contas += 1  # Incrementa o contador de contas ao criar uma nova conta
        
    @property
    def saldo(self):
        
        """
            Retorna o saldo atual da conta.
        """
        return self._saldo
    
    @classmethod
    def get_total_contas(cls):
        
        """
            Retorna o número total de contas criadas.
        """
        return cls._total_contas 
    
    def depositar(self, valor: float):
        
        if valor>0:
            self._saldo += valor
            self._historico.append((datetime.now(), f"Depósito de R${valor:.2f}"))
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")

        
        else:
            print("Valor de depósito inválido. O valor deve ser positivo.")
            
    @abstractmethod   
    def sacar(self, valor: float):
        
        """
            Método abstrato para sacar um valor da conta.
            
            Args:
                valor (float): O valor a ser sacado.
        """
        pass
        
    def extrato(self):
        
        """
            Método abstrato para exibir o extrato da conta.
        """
        
        print(f"\n ----- Extrato da Conta Nº{self._numero} -----")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Saldo atual: {self._saldo:.2f}")
        print("Histórico de transações:")
        
        if not self._historico:
            print("Nenhuma transação realizada.")
        
        for data, transacao in self._historico:
            print(f"- {data.strftime('%Y-%m-%d %H:%M:%S')}: {transacao}")
            
        print ("----------------------------------------\n")
        pass
    
class ContaCorrente(Conta):
    
    """
        Subclasse que representa uma conta corrente.
    """
    
    def __init__(self, numero: int, cliente, limite: float = cfg.LIMITE_PADRAO):
        super().__init__(numero, cliente)
        self._limite = limite
        
    def sacar(self, valor: float):
        
        if valor <= 0:
            print("Valor de saque inválido. O valor deve ser positivo.")
            return
        
        saldo_disponivel = self._saldo + self._limite
        
        if valor > saldo_disponivel:
            print("Saldo insuficiente para realizar o saque.")
            return
        
        self._saldo -= valor
        
        self._historico.append((datetime.now(), f"Saque: -{valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
    
class ContaPoupanca(Conta):
    
    """
        Subclasse que representa uma conta poupança
    """
    
    def __init__(self, numero:int,cliente):
        super().__init__(numero,cliente)
        
    def sacar(self, valor:float):
        
        if valor <=0:
            print("Valor de saque inválido")
        
        if valor > self._saldo:
            
            raise SaldoInsuficienteError(self._saldo, valor)
        
        self._saldo -= valor
        
        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
        
    
        