import tkinter as tk
from tkinter import messagebox
from consultorio import Consultorio
from medico import Medico
from paciente import Paciente
from consulta import Consulta

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Consultório Médico")

        self.consultorio = Consultorio()

        # Frame para cadastro de médico
        frame_medico = tk.LabelFrame(master, text="Cadastro de Médico")
        frame_medico.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(frame_medico, text="Nome:").grid(row=0, column=0)
        self.medico_nome = tk.Entry(frame_medico)
        self.medico_nome.grid(row=0, column=1)

        tk.Label(frame_medico, text="Sexo:").grid(row=1, column=0)
        self.medico_sexo = tk.Entry(frame_medico)
        self.medico_sexo.grid(row=1, column=1)

        tk.Label(frame_medico, text="Endereço:").grid(row=2, column=0)
        self.medico_endereco = tk.Entry(frame_medico)
        self.medico_endereco.grid(row=2, column=1)

        tk.Label(frame_medico, text="CPF:").grid(row=3, column=0)
        self.medico_cpf = tk.Entry(frame_medico)
        self.medico_cpf.grid(row=3, column=1)

        tk.Label(frame_medico, text="Telefone:").grid(row=4, column=0)
        self.medico_telefone = tk.Entry(frame_medico)
        self.medico_telefone.grid(row=4, column=1)

        tk.Label(frame_medico, text="Identidade:").grid(row=5, column=0)
        self.medico_identidade = tk.Entry(frame_medico)
        self.medico_identidade.grid(row=5, column=1)

        tk.Label(frame_medico, text="CRM:").grid(row=6, column=0)
        self.medico_crm = tk.Entry(frame_medico)
        self.medico_crm.grid(row=6, column=1)

        tk.Label(frame_medico, text="Especialidade:").grid(row=7, column=0)
        self.medico_especialidade = tk.Entry(frame_medico)
        self.medico_especialidade.grid(row=7, column=1)

        tk.Button(frame_medico, text="Cadastrar Médico", command=self.cadastrar_medico).grid(row=8, column=0, columnspan=2, pady=5)

        # Frame para cadastro de pacientes
        frame_paciente = tk.LabelFrame(master, text="Cadastro de Paciente")
        frame_paciente.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(frame_paciente, text="Nome:").grid(row=0, column=0)
        self.paciente_nome = tk.Entry(frame_paciente)
        self.paciente_nome.grid(row=0, column=1)

        tk.Label(frame_paciente, text="Sexo:").grid(row=1, column=0)
        self.paciente_sexo = tk.Entry(frame_paciente)
        self.paciente_sexo.grid(row=1, column=1)

        tk.Label(frame_paciente, text="Endereço:").grid(row=2, column=0)
        self.paciente_endereco = tk.Entry(frame_paciente)
        self.paciente_endereco.grid(row=2, column=1)

        tk.Label(frame_paciente, text="CPF:").grid(row=3, column=0)
        self.paciente_cpf = tk.Entry(frame_paciente)
        self.paciente_cpf.grid(row=3, column=1)

        tk.Label(frame_paciente, text="Telefone:").grid(row=4, column=0)
        self.paciente_telefone = tk.Entry(frame_paciente)
        self.paciente_telefone.grid(row=4, column=1)

        tk.Label(frame_paciente, text="Identidade:").grid(row=5, column=0)
        self.paciente_identidade = tk.Entry(frame_paciente)
        self.paciente_identidade.grid(row=5, column=1)

        tk.Label(frame_paciente, text="Medicação Contínua:").grid(row=6, column=0)
        self.paciente_medicacao = tk.Entry(frame_paciente)
        self.paciente_medicacao.grid(row=6, column=1)

        tk.Button(frame_paciente, text="Cadastrar Paciente", command=self.cadastrar_paciente).grid(row=7, column=0, columnspan=2, pady=5)

        # Frame para cadastro de consulta
        frame_consulta = tk.LabelFrame(master, text="Marcar Consulta")
        frame_consulta.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(frame_consulta, text="CPF do Paciente:").grid(row=0, column=0)
        self.consulta_paciente_cpf = tk.Entry(frame_consulta)
        self.consulta_paciente_cpf.grid(row=0, column=1)

        tk.Label(frame_consulta, text="Relato:").grid(row=1, column=0)
        self.consulta_relato = tk.Entry(frame_consulta)
        self.consulta_relato.grid(row=1, column=1)

        tk.Label(frame_consulta, text="Medicamentos:").grid(row=2, column=0)
        self.consulta_medicamentos = tk.Entry(frame_consulta)
        self.consulta_medicamentos.grid(row=2, column=1)

        tk.Label(frame_consulta, text="Data/Hora (ex: 2024-12-17 15:00):").grid(row=3, column=0)
        self.consulta_data_hora = tk.Entry(frame_consulta)
        self.consulta_data_hora.grid(row=3, column=1)

        tk.Button(frame_consulta, text="Agendar Consulta", command=self.agendar_consulta).grid(row=4, column=0, columnspan=2, pady=5)

        # Frame para operações adicionais
        frame_ops = tk.LabelFrame(master, text="Operações")
        frame_ops.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        tk.Button(frame_ops, text="Imprimir Dados do Consultório", command=self.imprimir_consultorio).grid(row=0, column=0, pady=5)
        
        tk.Label(frame_ops, text="Consultar por CPF do Paciente:").grid(row=1, column=0)
        self.busca_paciente_cpf = tk.Entry(frame_ops)
        self.busca_paciente_cpf.grid(row=1, column=1)
        tk.Button(frame_ops, text="Listar Consultas", command=self.listar_consultas_paciente).grid(row=1, column=2, padx=5)
        
        # Cancelar consulta
        tk.Label(frame_ops, text="Cancelar Consulta - CPF:").grid(row=2, column=0)
        self.cancela_cpf = tk.Entry(frame_ops)
        self.cancela_cpf.grid(row=2, column=1)
        tk.Label(frame_ops, text="Data/Hora:").grid(row=2, column=2)
        self.cancela_data_hora = tk.Entry(frame_ops)
        self.cancela_data_hora.grid(row=2, column=3)
        tk.Button(frame_ops, text="Cancelar", command=self.cancelar_consulta).grid(row=2, column=4, padx=5)

        tk.Button(frame_ops, text="Listar Todas as Consultas", command=self.listar_todas_consultas).grid(row=3, column=0, pady=5, columnspan=5)

    def cadastrar_medico(self):
        nome = self.medico_nome.get()
        sexo = self.medico_sexo.get()
        endereco = self.medico_endereco.get()
        cpf = self.medico_cpf.get()
        telefone = self.medico_telefone.get()
        identidade = self.medico_identidade.get()
        crm = self.medico_crm.get()
        especialidade = self.medico_especialidade.get()

        if not (nome and sexo and endereco and cpf and telefone and identidade and crm and especialidade):
            messagebox.showerror("Erro", "Todos os campos do médico devem ser preenchidos.")
            return

        medico = Medico(nome, sexo, endereco, cpf, telefone, identidade, crm, especialidade)
        self.consultorio.setMedico(medico)
        messagebox.showinfo("Sucesso", "Médico cadastrado com sucesso!")

    def cadastrar_paciente(self):
        nome = self.paciente_nome.get()
        sexo = self.paciente_sexo.get()
        endereco = self.paciente_endereco.get()
        cpf = self.paciente_cpf.get()
        telefone = self.paciente_telefone.get()
        identidade = self.paciente_identidade.get()
        medicacao = self.paciente_medicacao.get()

        if not (nome and sexo and endereco and cpf and telefone and identidade and medicacao):
            messagebox.showerror("Erro", "Todos os campos do paciente devem ser preenchidos.")
            return

        p = Paciente(nome, sexo, endereco, cpf, telefone, identidade, medicacao)
        self.consultorio.cadastrarPacientes(p)
        messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")

    def agendar_consulta(self):
        cpf_paciente = self.consulta_paciente_cpf.get()
        relato = self.consulta_relato.get()
        medicamentos = self.consulta_medicamentos.get()
        data_hora = self.consulta_data_hora.get()

        if not (cpf_paciente and relato and medicamentos and data_hora):
            messagebox.showerror("Erro", "Todos os campos da consulta devem ser preenchidos.")
            return

        # Busca o paciente pelo CPF
        paciente = None
        for p in self.consultorio.pacientes:
            if p.cpf == cpf_paciente:
                paciente = p
                break
        
        if not paciente:
            messagebox.showerror("Erro", "Paciente não cadastrado.")
            return

        c = Consulta(paciente, relato, medicamentos, data_hora)
        self.consultorio.cadastrarConsulta(c)
        messagebox.showinfo("Sucesso", "Consulta agendada com sucesso!")

    def imprimir_consultorio(self):
        # Imprime no console
        self.consultorio.imprimir()

    def listar_consultas_paciente(self):
        cpf = self.busca_paciente_cpf.get()
        if not cpf:
            messagebox.showerror("Erro", "Informe o CPF do paciente para listar as consultas.")
            return

        # Capturar as consultas do paciente
        consultas_paciente = [c for c in self.consultorio.consultas if c.paciente.cpf == cpf]

        if not consultas_paciente:
            messagebox.showinfo("Resultado", f"Nenhuma consulta encontrada para o paciente com CPF {cpf}.")
        else:
            resultado = ""
            for c in consultas_paciente:
                resultado += f"[{c.data_hora}] Paciente: {c.paciente.nome}, Relato: {c.relato}, Medicamentos: {c.medicamentos}\n"
            messagebox.showinfo("Consultas do Paciente", resultado)

    def cancelar_consulta(self):
        cpf = self.cancela_cpf.get()
        data_hora = self.cancela_data_hora.get()

        if not (cpf and data_hora):
            messagebox.showerror("Erro", "Informe o CPF e o horário da consulta a cancelar.")
            return

        self.consultorio.cancelarConsulta(cpf, data_hora)
        messagebox.showinfo("Sucesso", f"Se existia uma consulta para CPF {cpf} no horário {data_hora}, ela foi cancelada.")

    def listar_todas_consultas(self):
        if not self.consultorio.consultas:
            messagebox.showinfo("Consultas", "Nenhuma consulta agendada.")
            return
        resultado = ""
        for c in self.consultorio.consultas:
            resultado += f"[{c.data_hora}] Paciente: {c.paciente.nome} - Relato: {c.relato} - Medicamentos: {c.medicamentos}\n"
        messagebox.showinfo("Todas as Consultas", resultado)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
