from datetime import datetime
import time

class Mercado:
    def __init__(self):
        self.cpf = None
        self.total = 0
        self.catalogo = {
            'Carne boi': 22.50,
            'File mion': 30.0,
            'Lasanha': 21.99,
            'Torta de frango': 18.40,
            'Bhama': 10.0,
            'Red bull': 7.50
        }
        self.carrinho = []
        self.data_compra = datetime.today()
        
    def view_loja(self):
        for produto, preco in self.catalogo.items():  # Usar .items() para iterar corretamente
            print('=' * 25)
            print(f'{produto} - R${preco:.2f}')  # Formatar o preço
            print('=' * 25)
            
    def compra(self):
        while True:
            produto_escolhido = input('Digite o produto que deseja comprar: ').capitalize()
            if produto_escolhido in self.catalogo:
                self.carrinho.append(produto_escolhido)
                preco = self.catalogo[produto_escolhido]
                self.total += preco
                print(f'O produto {produto_escolhido} foi adicionado ao carrinho! Total atual: R${self.total:.2f}')
            else:
                print(f'Produto {produto_escolhido} não encontrado!')
            opcao = input('Deseja comprar mais alguma coisa? [S/N]: ')
            if opcao.upper() != 'S':
                break
    
    def info_pagamento(self):
        forma_pagamento = input('Digite a forma de pagamento (Pix, Cartão ou Dinheiro?): ').capitalize()
        
        if forma_pagamento == 'Pix':
            chave = '982007590'
            print(f'Nossa chave Pix: {chave}')
            digito = input('Digite nossa chave Pix: ')
            if digito == chave:
                valor = float(input('Digite o valor a ser pago: '))
                if valor < self.total:
                    print('Processando pagamento...')
                    time.sleep(3)
                    print('Ops, seu valor é insuficiente. Tente novamente.')
                else:
                    self.finalizar_pagamento(valor)

        elif forma_pagamento == 'Cartão':
            opcao = input('Crédito ou Débito? : ').capitalize()
            if opcao == 'Crédito':
                parcelas = int(input('Quantas vezes deseja parcelar? : '))
                total_parcelas = self.total / parcelas
                print(f'A compra de R${self.total:.2f} foi parcelada em {parcelas}x de R${total_parcelas:.2f}')
                self.cpf = self.obter_cpf()
                senha = input('Digite sua senha: ')
                while len(senha) != 4 or not senha.isdigit():
                    senha = input('Ops, sua senha está incorreta. Tente Novamente: ')
                print('Compra realizada com sucesso!')
                
        elif forma_pagamento == 'Dinheiro':
            valor = float(input('Digite o valor a ser pago: '))
            if valor < self.total:
                print('Ops, valor insuficiente.')
            else:
                self.finalizar_pagamento(valor)

    def finalizar_pagamento(self, valor):
        self.cpf = self.obter_cpf()
        verifica_cpf = 'Nenhum CPF' if self.cpf == None else self.cpf
        print(f'''
              Valor Total: {self.total:.2f}
              Valor pago: {valor:.2f}
              Data e Hora da compra: {self.data_compra}
              CPF: {verifica_cpf}
              Caixa: 2
              Vendedor: Moises Vinicius
              Tel: 982007590
              Volte sempre!
              ''')

    def obter_cpf(self):
        opcao_cpf = input('Deseja colocar o CPF? [S/N]: ')
        if opcao_cpf.upper() == 'S':
            cpf = input('Digite o número do CPF (somente números): ')
            if len(cpf) == 11 and cpf.isdigit():
                return cpf
            else:
                print('CPF inválido!')
        return None

# Criando uma instância do Mercado
mercado = Mercado()

# Exibindo o catálogo da loja
mercado.view_loja()

# Realizando a compra
mercado.compra()

# Processando o pagamento
mercado.info_pagamento()
