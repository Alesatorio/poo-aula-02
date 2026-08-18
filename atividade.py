import os

# ============================
# Definição das Classes (UML)
# ============================

class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
    
    def exibir_info(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Email: {self.email}"

class Medico(Pessoa):
    def __init__(self, nome, idade, email, especialidade):
        super().__init__(nome, idade, email)
        self.especialidade = especialidade
        
    def atender(self):
        print(f"O médico {self.nome} está realizando um atendimento.")

class Paciente(Pessoa):
    def __init__(self, nome, idade, email, historico):
        super().__init__(nome, idade, email)
        self.historico = historico
    
    def marcar_consulta(self, medico, data):
        # Instancia e retorna uma Consulta vinculando este paciente e o médico escolhido
        return Consulta(data, self, medico)

class Consulta:
    def __init__(self, data, paciente, medico):
        self.data = data
        self.paciente = paciente
        self.medico = medico
        self.diagnostico = None

    def registrar_diagnostico(self, texto):
        self.diagnostico = texto

    def exibir_consulta(self):
        print("\n--- Consulta ---")
        print(f"Data: {self.data}")
        print(f"Paciente: {self.paciente.exibir_info()}")
        print(f"Médico: {self.medico.exibir_info()} | Esp: {self.medico.especialidade}")
        if self.diagnostico:
            print(f"Diagnóstico: {self.diagnostico}")
        else:
            print("Diagnóstico: [a definir]")
        print("----------------\n")


# ============================
# Funções Auxiliares (DRY)
# ============================

def coletar_dados_pessoa():
    """Centraliza a coleta de dados básicos para evitar repetição de código (DRY)"""
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("Email: ")
    return nome, idade, email


# ============================
# Menu de Linha de Comando
# ============================

medicos = []
pacientes = []
consultas = []

while True:
    print("===== Sistema da Clínica =====")
    print("1 - Cadastrar Médico")
    print("2 - Cadastrar Paciente")
    print("3 - Listar Médicos")
    print("4 - Listar Pacientes")
    print("5 - Marcar Consulta")
    print("6 - Listar Consultas")
    print("7 - Registrar Diagnóstico")
    print("0 - Sair")

    opcao = input("Escolha: ")
    # os.system("clear") # 'clear' funciona em Linux/Mac. Em Windows use 'cls'
    # Utilizando um ternário seguro para limpar a tela em qualquer SO:
    os.system('cls' if os.name == 'nt' else 'clear')

    # 1 - Cadastrar Médico
    if opcao == "1":
        print("--- Cadastrar Novo Médico ---")
        nome, idade, email = coletar_dados_pessoa()
        especialidade = input("Especialidade: ")
        medicos.append(Medico(nome, idade, email, especialidade))
        print("\nMédico cadastrado com sucesso!\n")

    # 2 - Cadastrar Paciente
    elif opcao == "2":
        print("--- Cadastrar Novo Paciente ---")
        nome, idade, email = coletar_dados_pessoa()
        historico = input("Histórico médico: ")
        pacientes.append(Paciente(nome, idade, email, historico))
        print("\nPaciente cadastrado com sucesso!\n")

    # 3 - Listar Médicos
    elif opcao == "3":
        if not medicos:
            print("Nenhum médico cadastrado!\n")
        else:
            print("--- Lista de Médicos ---")
            for i, m in enumerate(medicos):
                print(f"[{i}] {m.exibir_info()} | Esp: {m.especialidade}")
            print()

    # 4 - Listar Pacientes
    elif opcao == "4":
        if not pacientes:
            print("Nenhum paciente cadastrado!\n")
        else:
            print("--- Lista de Pacientes ---")
            for i, paciente in enumerate(pacientes):
                print(f"[{i}] {paciente.exibir_info()} | Histórico: {paciente.historico}")
            print()

    # 5 - Marcar Consulta
    elif opcao == "5":
        if not medicos or not pacientes:
            print("É necessário cadastrar ao menos um médico e um paciente primeiro!\n")
            continue
        
        print("--- Marcar Nova Consulta ---")
        for i, p in enumerate(pacientes):
            print(f"[{i}] {p.nome}")
        idx_p = int(input("Escolha o ID do paciente: "))
        paciente = pacientes[idx_p]

        for i, m in enumerate(medicos):
            print(f"[{i}] {m.nome} ({m.especialidade})")
        idx_m = int(input("Escolha o ID do médico: "))
        medico = medicos[idx_m]

        data = input("Data da consulta (dd/mm/aaaa): ")
        
        consulta = paciente.marcar_consulta(medico, data)
        consultas.append(consulta)
        print("\nConsulta marcada com sucesso!\n")

    # 6 - Listar Consultas
    elif opcao == "6":
        if not consultas:
            print("Nenhuma consulta registrada!\n")
        else:
            print("--- Lista de Consultas Agendadas ---")
            for c in consultas:
                c.exibir_consulta()

    # 7 - Registrar Diagnóstico
    elif opcao == "7":
        if not consultas:
            print("Nenhuma consulta disponível para registrar diagnóstico!\n")
            continue
            
        print("--- Registrar Diagnóstico ---")
        for i, c in enumerate(consultas):
            print(f"[{i}] {c.data} | Paciente: {c.paciente.nome} | Médico: {c.medico.nome}")
        idx_c = int(input("Escolha o ID da consulta: "))
        diag = input("Digite o diagnóstico: ")
        consultas[idx_c].registrar_diagnostico(diag)
        print("\nDiagnóstico registrado!\n")

    # 0 - Sair
    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!\n")