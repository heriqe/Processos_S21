class Bomba_Combustivel:
    
    def __init__(self, valor_litro, quantidade_disponivel):
        self.__valor_litro = valor_litro
        self.__quantidade_disponivel = quantidade_disponivel
    
    def get_valor_litro(self):
        return self.__valor_litro
    
    def get_quantidade_disponivel(self):
        return self.__quantidade_disponivel
    
    def set_quantidade_disponivel(self, litros):
        if litros <= self.__quantidade_disponivel:
            self.__quantidade_disponivel -= litros
            return litros
        else:
            return -1
    
    def _validar_quantidade_disponivel(self, litros):
        if litros <= self.__quantidade_disponivel:
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
        
    