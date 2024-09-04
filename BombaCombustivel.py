class BombadeCombustivel:
    
    def __init__(self, tipoCombustivel, valor_litro, quantidade_disponivel):
        self.__tipoCombustivel = tipoCombustivel
        self.__valor_litro = valor_litro
        self.__quantidade_disponivel = quantidade_disponivel
        
    def abastecer_por_valor(self, valor):
        litros = valor / self.__valor_litro
        
        if litros > self.__quantidade_disponivel:
            print("Quantidade insuficiente de combustivel na bomba.\n")
            return
        
        self.__quantidade_disponivel -= litros
        print(f"A quantidade abastecida de litros foi {litros} L\n")
        
    def abastecer_por_litro(self, litros):
        if litros > self.__quantidade_disponivel:
            print("Quantidade insuficiente de combustivel na bomba.\n")
            return
        
        valor = litros * self.__valor_litro
        self.__quantidade_disponivel -= litros
        
        print(f"O valor a ser pago é R$ {valor}\n")
        
    def alterarValor(self, novo_preço):
        self.__valor_litro = novo_preço
        print(f"O novo preço por litro é R$ {novo_preço}\n")
        
    def alterarCombustivel(self, tipo):
        tipo = self.__tipoCombustivel 
        print(f"Tipo de combustivel alterado para {tipo}\n")
        
    def alterar_quantidade_disponivel(self, nova_quantidade):
        nova_quantidade = self.__quantidade_disponivel
        print(f"A nova quantidade restante de litros é {nova_quantidade} L\n")

# Exemplo de uso
bomba = BombadeCombustivel('gasolina', 4, 100)
bomba.abastecer_por_valor(20)
bomba.abastecer_por_litro(10)
bomba.alterarValor(6)
bomba.alterarCombustivel('alcool')
bomba.alterar_quantidade_disponivel(150)
