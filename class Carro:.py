class Veiculo:
    def __init__(self, ano, cor, marca, velocidade_maxima):
        self.ano = ano
        self.cor = cor
        self.marca = marca
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, valor):
        if self.velocidade_atual + valor <= self.velocidade_maxima:
            self.velocidade_atual += valor
        else:
            print("Velocidade máxima atingida")

    def frear(self, valor):
        if self.velocidade_atual - valor >= 0:
            self.velocidade_atual -= valor
        else:
            print("O carro já está parado")

class Caminhao(Veiculo):
    def __init__(self, ano, cor, marca, velocidade_maxima, peso, tonelagem, tipo_carroceria):
        super().__init__(ano, cor, marca, velocidade_maxima)
        self.peso = peso
        self.tonelagem = tonelagem
        self.tipo_carroceria = tipo_carroceria

    def carregar(self, carga):
        if carga <= self.tonelagem:
            print("Carga carregada com sucesso")
        else:
            print("Excesso de carga, tonelagem máxima excedida")


meu_caminhao = Caminhao(2023, "Azul", "Volvo", 100, 5000, 10000, "Baú")
print("Ano de Fabricação:", meu_caminhao.ano)
print("Cor:", meu_caminhao.cor)
print("Marca:", meu_caminhao.marca)
print("Velocidade Máxima:", meu_caminhao.velocidade_maxima)
print("Peso:", meu_caminhao.peso)
print("Tonelagem:", meu_caminhao.tonelagem)
print("Tipo de Carroceria:", meu_caminhao.tipo_carroceria)

meu_caminhao.acelerar(60)
print("Velocidade Atual:", meu_caminhao.velocidade_atual)

meu_caminhao.carregar(8000)


meu_carro = Veiculo(2023, "Azul", "Toyota", 200)
print("Ano de Fabricação:", meu_carro.ano)
print("Cor:", meu_carro.cor)
print("Marca:", meu_carro.marca)
print("Velocidade Máxima:", meu_carro.velocidade_maxima)

meu_carro.acelerar(50)
print("Velocidade Atual:", meu_carro.velocidade_atual)

meu_carro.frear(20)
print("Velocidade Atual após frear:", meu_carro.velocidade_atual)

