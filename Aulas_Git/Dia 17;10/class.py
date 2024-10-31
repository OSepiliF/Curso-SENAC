class Veiculo:
    def __init__(self, marca, modelo, cor, ano, portas):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.portas = portas

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, ano, portas, air_bag):
        super().__init__(marca, modelo, cor, ano, portas)
        self.air_bag = air_bag

    def acelerar(self):
            print(f'O carro {self.modelo} da marca {self.marca} acelerou. ')

    def freiar(self):
            print(f'O carro {self.modelo} da marca {self.marca} freiou. ')

class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, ano, portas, guidao):
        super().__init__(marca, modelo, cor, ano, portas)
        self.guidao = guidao

    def acelerar(self):
        print(f'A moto {self.modelo} da marca {self.marca} acelerou. ')

fusca = Carro('VolksWagen','Fusca','Preto',1967,2, False)
civic = Carro('Honda',"Civic","Vermelho",1945,4, True)
harley = Moto('Harley Davidson','FatBoy','Azul',2019, 0, True)

print("\n======== Carros ========")
print(vars(fusca))
print(vars(civic))

print("\n======== Motos ========")
for key, value in vars(harley).items():
    print(f"{key}: {value}")

print('')
fusca.freiar()
harley.acelerar()
print('')