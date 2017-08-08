#Pessoa
class Pessoa():
    nome = None
    nascimento = None
    def __init__(self, nome=None, nascimento=None):
        self.nome = nome
        self.nascimento = nascimento
    def __str__(self):
        return self.nome
#PessoaFisica
class PessoaFisica(Pessoa):
    cpf = None
    def __init__(self, nome=None, nascimento=None, cpf=None):
        Pessoa.__init__(self ,nome, nascimento)
        self.cpf = cpf
#PessoaJuridica
class PessoaJuridica(Pessoa):
    cnpj = None
    def __init__(self, nome=None, nascimento=None, cnpj=None):
        Pessoa.__init__(self ,nome, nascimento)
        self.cnpj = cnpj
#Projeto
class Projeto():
    nome = None
    def __init__(self, nome=None):
        self.nome = nome
    def __str__(self):
        return self.nome
#Tarefa
class Tarefa():
    projeto = None
    descricao = None
    dataInicio = None
    dataFim = None
    prioridade = None
    solicitante = None
    realizador = None
    def __init__(self, projeto = None, descricao = None, dataInicio = None, dataFim = None, prioridade = None, solicitante = None, realizador = None):
        self.projeto = projeto
        self.descricao = descricao
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.prioridade = prioridade
        self.solicitante = solicitante
        self.realizador = realizador

    def __str__(self):
        return self.nome