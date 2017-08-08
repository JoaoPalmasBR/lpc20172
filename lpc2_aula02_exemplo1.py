class Endereco():
    logradouro = None
    
    def __init__(self, logradouro=None):
        self.logradouro = logradouro

    def __str__(self):
        return self.logradouro
#-----------------------------------------------------------------------
class Pessoa():
    nome = None
    nascimento = None
    endereco = None
    
    def __init__(self, nome=None, nascimento=None, endereco=None):
        self.nome = nome
        self.nascimento = nascimento
        self.endereco = Endereco('Rua 01.')
    
    def __str__(self):
        return self.nome
#-----------------------------------------------------------------------
class PessoaFisica(Pessoa):
    cpf = None
    
    def __init__(self, nome=None, nascimento=None, cpf=None):
        Pessoa.__init__(self ,nome, nascimento)
        self.cpf = cpf
#-----------------------------------------------------------------------
class PessoaFisica(Pessoa):
    cnpj = None
    
    def __init__(self, nome=None, nascimento=None, cnpj=None):
        Pessoa.__init__(self ,nome, nascimento)
        self.cnpj = cnpj
#-----------------------------------------------------------------------
p1 = Pessoa(nome='joao', nascimento='natal')
print(p1.nome)