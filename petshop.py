class Responsavel_do_pet:
    def __init__(self, name, parentesco, telefone):
        self.name = name
        self.parentesco = parentesco
        self.telefone = telefone
    
    def imprimir_dados_responsavel(self):
        print(f"Nome do responsável: {self.name}")
        print(f"Parentesco: {self.parentesco}")
        print(f"Telefone: {self.telefone}")


class Pet:
    def __init__(self, nome,raca, idade, responsavel):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.responsavel = responsavel

    def imprimir_dados_pet(self):
        print(f"Nome do pet: {self.nome}")
        print(f"Raça: {self.raca}")
        print(f"Idade: {self.idade} anos")
        print("Dados do responsável:")
        self.responsavel.imprimir_dados_responsavel()

    def horario_passeios(self):
        horarios = [
            "(1) Segunda-feira: 10:00",
            "(2) Quarta-feira: 14:00",
            "(3) Sexta-feira: 16:00"
        ]

        print("--- Horários e datas para passeios ---")
        print("Horários disponíveis:")
        for item in horarios:
            print(item)

        escolha = input("Escolha um horário (1, 2 ou 3): ")

        if escolha == "1":
            print("Passeio agendado para Segunda-feira às 10:00")
        elif escolha == "2":
            print("Passeio agendado para Quarta-feira às 14:00")
        elif escolha == "3":
            print("Passeio agendado para Sexta-feira às 16:00")
        else:
            print("Horário inválido. Tente novamente.")
            

print("--- Bem-vindo ao Gato a Jato Petshop! ---")
nome_responsavel = input("Digite o nome do responsável pelo pet: ")
parentesco = input("Digite o parentesco com o pet: ")
telefone = input("Digite o telefone do responsável: ")
responsavel = Responsavel_do_pet(nome_responsavel, parentesco, telefone)
nome_pet = input("Digite o nome do pet: ")
especie_pet = input("Digite a espécie do pet (ex: cachorro, gato): ")
raca_pet = input("Digite a raça do pet: ")
idade_pet = input("Digite a idade do pet: ")


pet = Pet(nome_pet, raca_pet, idade_pet, responsavel)

pet.imprimir_dados_pet()
pet.horario_passeios()
print(f"Obrigado por escolher o Gato a Jato Petshop {nome_responsavel}!")