from abc import ABC, abstractmethod

class Funcionario(ABC):

    nome: str
    cpf: str
    __senha: int

    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.__senha = senha

    def getSenha(self):
        return self.__senha

    def __str__(self):
        info = f'Nome: {self.nome}\n'+ f'RG: {self.cpf}\n'
        return info 

    @abstractmethod
    def autenticar(self,user:str,senha:int):
        pass

class Gerente(Funcionario):

    def autenticar(self, user: str, senha: int):
        if(user == self.cpf and self.getSenha() == senha):
            return True
        else:
            return False
        
    def __init__(self, nome, cpf, senha):
        super().__init__(nome, cpf, senha)

    def __str__(self):
        return super().__str__() 
        
    def cancelar_operacao(self):
        info = 'Cancelamento realizado com sucesso!'
        return info
        
class Operador_Caixa(Funcionario):

    numero_caixa: int

    def __init__(self, nome, cpf, senha, numero_caixa):
        super().__init__(nome, cpf, senha)
        self.numero_caixa = numero_caixa

    def autenticar(self, user: str, senha: int):
        if(user == self.numero_caixa and senha == self.getSenha()):
            return True
        else:
            return False
        
    def __str__(self):
        return super().__str__() + f'Numero do caixa: {self.numero_caixa}\n'
    
    def registrar_produto(self):
        info = f'Produto registrado com sucesso!'
        return info 

class Seguranca(Funcionario):

    posto: int 

    def __init__(self, nome, cpf, senha, posto):
        super().__init__(nome, cpf, senha)
        self.posto = posto

    def __str__(self):
        return super().__str__() + f'Posto: {self.posto}'
    
    def autenticar(self, user: str, senha: int):
        if(user == self.posto and senha == self.getSenha()):
            return True
        else: return False

    def acionar_alarme(self):
        info = 'OOOOOOOOOOOOuuuuuuuuuoOoUOuouOUoUOUOUOUOUOUo'
        return info
        