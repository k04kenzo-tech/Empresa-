import os

class Produtos:

    def __init__(self, nome, valor, quantidade):
        self.nomeproduto = nome
        self.valorproduto = valor
        self.quantidadeproduto = quantidade


class SistemaCadastroProduto:

    def _init_(self):
        self.arquivo = r"produtos.txt"

    def cadastrarproduto(self):

        print("\n===== CADASTRAR PRODUTO =====\n")

        while True:

            while True:

                nomeproduto = input("Digite o nome do produto: ").strip()

                if not nomeproduto.isalpha() or nomeproduto == "":
                    print("\nNome inválido\n")
                else:
                    break

            while True:

                try:

                    valorproduto = float(input("\nDigite o valor do produto: "))

                    if valorproduto < 0:
                        print("\nValor invalido")
                    else:
                        break
                except ValueError:
                    print("\nDigite apenas números")

            while True:

                try:

                    quantidadeproduto = int(input("\nDigite a quantidade de produtos: "))

                    if quantidadeproduto < 0:
                        print("\nQuantidade invalida")
                    else:
                        break
                except ValueError:
                    print("\nDigite apenas numeros")
                
            
            produto = Produtos(nomeproduto, valorproduto, quantidadeproduto)

            with open(self.arquivo, "a", encoding="utf-8") as arquivo:

                arquivo.write(
                    f"Produto: {produto.nomeproduto} |"
                    f"Valor: {produto.valorproduto}R$ |"
                    f"Estoque: {produto.quantidadeproduto} |\n"
                    )

            print("\nProduto cadastrado com sucesso!\n")

            break

SCP = SistemaCadastroProduto()

SCP.cadastrarproduto()
