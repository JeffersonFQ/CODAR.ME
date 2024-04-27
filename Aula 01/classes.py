class Cliente:
    def __init__(self, nome, cpf, endereco, pagamento):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.pagamento = pagamento


C1 = Cliente("Jéfferson", 70013153110, "Rua Joaquim Q11 L06", "Pix")
print(C1.nome)