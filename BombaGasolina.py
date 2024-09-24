from BombaCombustivel import Bomba_Combustivel

class BombaGasolina(Bomba_Combustivel):
    def __init__(self,  valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)

    def abastecer_por_valor_com_aditivo(self, valor):
        valor_aditivo = valor * 1.05
        litros = valor_aditivo / super().get_valor_litro()
        
        if litros <= super().get_quantidade_disponivel():
            super().set_quantidade_disponivel() -= litros
            return litros
        else:
            return -1

    def abastecer_por_litro_com_aditivo(self, litros):
        if litros <= super().get_quantidade_disponivel():
            valor_com_aditivo = litros * super().get_valor_litro() * 1.05
            super().get_quantidade_disponivel() -= litros
            return valor_com_aditivo
        else:
            return -1