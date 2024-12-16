 
from typing import List
from paciente import Paciente
from medico import Medico
from consulta import Consulta

class Consultorio:
    def __init__(self):
        self.pacientes: List[Paciente] = []
        self.medico: Medico = None
        self.consultas: List[Consulta] = []

    def imprimir(self):
        print("=== Dados do Consultório ===")
        print("Médico:")
        if self.medico:
            self.medico.imprimirDados()
            print(f"CRM: {self.medico.crm}")
            print(f"Especialidade: {self.medico.especialidade}")
        else:
            print("Nenhum médico cadastrado.")
        print("Pacientes:")
        for p in self.pacientes:
            p.imprimirDados()
            print(f"Medicação Contínua: {p.medicacao_continua}\n")

        print("Consultas:")
        for c in self.consultas:
            print(f"[{c.data_hora}] Paciente: {c.paciente.nome} - Relato: {c.relato} - Medicamentos: {c.medicamentos}")
        print("===========================\n")

    def cadastrarPacientes(self, paciente: Paciente):
        for p in self.pacientes:
            if p.cpf == paciente.cpf:
                print(f"Paciente com CPF {paciente.cpf} já cadastrado.")
                return
        self.pacientes.append(paciente)

    def removerPacientes(self, cpf: str):
        paciente_encontrado = False
        for p in self.pacientes:
            if p.cpf == cpf:
                self.pacientes.remove(p)
                paciente_encontrado = True
                break
        if not paciente_encontrado:
            print(f"Nenhum paciente com o CPF {cpf} encontrado.")

    def setMedico(self, medico: Medico):
        self.medico = medico

    def cadastrarConsulta(self, consulta: Consulta):
        if consulta.paciente not in self.pacientes:
            print("Paciente não cadastrado. Não é possível marcar consulta.")
            return

        if not self.medico:
            print("Não há médico atribuído ao consultório. Não é possível marcar consulta.")
            return

        # Aqui poderíamos checar se o horário colide com outros horários do mesmo paciente ou do médico
        # Por simplicidade, apenas verificamos se o paciente já tem uma consulta nesse mesmo horário:
        for c in self.consultas:
            if c.data_hora == consulta.data_hora and c.paciente.cpf == consulta.paciente.cpf:
                print(f"O paciente {consulta.paciente.nome} já possui uma consulta neste horário.")
                return

        self.consultas.append(consulta)

    def cancelarConsulta(self, cpf: str, data_hora: str):
        consulta_encontrada = False
        for c in self.consultas:
            if c.paciente.cpf == cpf and c.data_hora == data_hora:
                self.consultas.remove(c)
                consulta_encontrada = True
                break
        if not consulta_encontrada:
            print(f"Nenhuma consulta para o paciente com CPF {cpf} neste horário {data_hora} foi encontrada.")

    def imprimirConsultasPaciente(self, cpf: str):
        encontrou = False
        for c in self.consultas:
            if c.paciente.cpf == cpf:
                print(f"[{c.data_hora}] Paciente: {c.paciente.nome} - Relato: {c.relato} - Medicamentos: {c.medicamentos}")
                encontrou = True
        if not encontrou:
            print(f"Nenhuma consulta encontrada para o paciente com CPF {cpf}.")

    def imprimirTodasConsultas(self):
        if not self.consultas:
            print("Nenhuma consulta agendada.")
            return
        for c in self.consultas:
            print(f"[{c.data_hora}] Paciente: {c.paciente.nome} - Relato: {c.relato} - Medicamentos: {c.medicamentos}")
