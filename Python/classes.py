import datetime

class Cliente:    
    id_cliente = 1
# Dados obrigatórios para criação do cliente
    def __init__(self, nome, endereco, email, senha, tipo_sanguineo):
        self.id_cliente = Cliente.id_cliente
        self.log_data_cliente = datetime.datetime.now()
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.senha = senha
        self.lista_tipo_sanguineo = ["+A", "+B", "+AB", "+O", "-A", "-B", "-AB", "-O"]
        if tipo_sanguineo in self.lista_tipo_sanguineo:
            self.tipo_sanguineo = tipo_sanguineo
        else:
            print("Tipo sanguíneo incompatível")
        Cliente.id_cliente += 1           
    
# Função pra trocar o nome, pode ser chamado com variável.trocar_nome()
    def trocar_nome(self, novo_nome):
        self.nome = novo_nome

# Função pra trocar o endereço, pode ser chamado com variável.trocar_endereco()
    def trocar_endereco(self, novo_endereco):
        if novo_endereco in self.lista_tipo_sanguineo:
            self.endereco = novo_endereco

# Função pra imprimir dados do cliente, pode ser chamado com imprimir_informacoes()
    def imprimir_informacoes(self):
        print("ID:", self.id)
        print("Nome do cliente:", self.nome)
        print("Endereço:", self.endereco)
        print("Tipo Sanguíneo:", self.tipo_sanguineo)

class Doacao(Cliente):
    id_doacao = 1
    def __init__(self, email, senha, tipo_sanguineo):
        self.id_doacao = Doacao.id_doacao
        self.log_data_doacao = datetime.datetime.now()
        super.__init__(email, senha, tipo_sanguineo)
        Doacao.id_doacao += 1
    
    def criar_doacao():
        data_doacao = input(str("Digite a data para a Doação: (DD/MM/AA HH:MM): "))
        return data_doacao
        

agendamento = Doacao.criar_doacao()
print(agendamento)

class Receber(Cliente):
    def __init__(self):
        pass
