 
from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome: str, sexo: str, endereco: str, cpf: str, telefone: str, identidade: str, medicacao_continua: str):
        super().__init__(nome, sexo, endereco, cpf, telefone, identidade)
        self.medicacao_continua = medicacao_continua
