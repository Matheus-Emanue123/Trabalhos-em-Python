from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome: str, sexo: str, endereco: str, cpf: str, telefone: str, identidade: str, crm: str, especialidade: str):
        super().__init__(nome, sexo, endereco, cpf, telefone, identidade)
        self.crm = crm
        self.especialidade = especialidade
