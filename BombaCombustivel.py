class BombadeCombustivel:
    
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
        
    def abastecerPorValor(self, valorAbastecer):
        litros_abastecidos = valorAbastecer / self.valorLitro
        
        if litros_abastecidos > self.quantidadeCombustivel:
            print("Quantidade insuficiente de combustivel na bomba.\n")
            return
        
        self.quantidadeCombustivel -= litros_abastecidos
        print(f"A quantidade abastecida de litros foi {litros_abastecidos} L\n")
        
    def abastecerPorLitro(self, qtdLitros):
        if qtdLitros > self.quantidadeCombustivel:
            print("Quantidade insuficiente de combustivel na bomba.\n")
            return
        
        valor_a_pagar = qtdLitros * self.valorLitro
        self.quantidadeCombustivel -= qtdLitros
        
        print(f"O valor a ser pago é R$ {valor_a_pagar}\n")
        
    def alterarValor(self, novo_preço):
        self.valorLitro = novo_preço
        print(f"O novo preço por litro é R$ {novo_preço}\n")
        
    def alterarCombustivel(self, tipo):
        self.tipoCombustivel = tipo
        print(f"Tipo de combustivel alterado para {self.tipoCombustivel}\n")
        
    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade
        print(f"A nova quantidade restante de litros é {self.quantidadeCombustivel} L\n")

# Exemplo de uso
bomba = BombadeCombustivel('gasolina', 4, 100)
bomba.abastecerPorValor(20)
bomba.abastecerPorLitro(10)
bomba.alterarValor(6)
bomba.alterarCombustivel('alcool')
bomba.alterarQuantidadeCombustivel(150)
