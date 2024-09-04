from BombaCombustivel import Bomba_Combustivel

class BombaEtanol(Bomba_Combustivel):
    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)