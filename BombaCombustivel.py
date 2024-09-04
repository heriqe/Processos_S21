class Bomba_Combustivel:
    
    def __init__(self, valor_litro, quantidade_disponivel):
        self.__valor_litro = valor_litro
        self.__quantidade_disponivel = quantidade_disponivel

    @property
    def valor_litro(self):
        return self._valor_litro

    @valor_litro.setter
    def valor_litro(self, valor):
        self._valor_litro = valor

    @property
    def quantidade_disponivel(self):
        return self._quantidade_disponivel

    @quantidade_disponivel.setter
    def quantidade_disponivel(self, quantidade):
        self._quantidade_disponivel = quantidade
    
    def _validar_quantidade_disponivel(self, litros):
        if litros <= self._quantidade_disponivel:
            return True
        else:
            return False
    
    def abastecer_por_valor(self, valor):
        litros = valor / self.__valor_litro
        
        if litros <= self.__quantidade_disponivel:
            self.__quantidade_disponivel -= litros
            return litros
        
        else:
            return -1
        
    def abastecer_por_litro(self, litros):

        if litros <= self.__quantidade_disponivel:
            self.__quantidade_disponivel -= litros
            return litros * self.__valor_litro
        
        else:
            return -1
        
    