from entities.cliente import Cliente
from entities.conta import  Conta, ContaCorrente, ContaPoupanca
from utils.exceptions import ContaInexistenteError

class Banco():
    
    """
        Classe que gerencia as operacoes do banco
    """
    
    def __init__(self, nome: str):
        self.nome = nome
        self._cliente = {}
        self._contas = {}
        pass
    
    #Metodo para adicionar um novo cliente ao banco
    def adicionar_clientes(self, nome:str, cpf:str) -> Cliente:
        
        #Se já existe um CPF
        if cpf in self._cliente:
            print("Erro: Cliente com este CPF já cadastrado.")
            return self._cliente[cpf]
        
        novo_cliente = Cliente(nome, cpf)
        self._cliente[cpf] = novo_cliente
        
        print(f"Cliente {nome} adicionado com sucesso!")
        return novo_cliente
    
    # Método para criar uma conta para um cliente
    def criar_conta(self, cliente: Cliente, tipo: str) -> Conta:
        
        """Cria uma nova conta para um cliente existente."""
        
        numero_conta = Conta.get_total_contas() + 1
        
        if tipo.lower() == 'corrente':
            nova_conta = ContaCorrente(numero_conta, cliente)
        
        elif tipo.lower() == 'poupanca':
            nova_conta = ContaPoupanca(numero_conta, cliente)
        
        # Caso o tipo não seja válido
        else:
            print("Tipo de conta inválido. Escolha 'corrente' ou 'poupanca'.")
            return None

        # Adiciona a conta ao dicionário de contas
        self._contas[numero_conta] = nova_conta
        
        # Associa a conta ao cliente
        cliente.adicionar_conta(nova_conta)
        print(f"Conta {tipo} nº {numero_conta} criada para o cliente {cliente.nome}.")

        return nova_conta

    # Método para buscar uma conta pelo número
    def buscar_conta(self, numero_conta: int) -> Conta:
          
        """Busca uma conta pelo seu número."""
        
        # Tenta recuperar a conta do dicionário
        conta = self._contas.get(numero_conta)
        
        # Se não encontrar, lança exceção personalizada
        if not conta:
            raise ContaInexistenteError(numero_conta)
        return conta
    

            