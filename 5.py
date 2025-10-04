# Calcula o valor de uma compra
def compra(valor, desconto_09, prestacao_5x, prestacao_10x):
    desconto_09 = valor * 0.91
    prestacao_5x = valor / 5
    prestacao_10x = (valor * 1.17) / 10
    return desconto_09, prestacao_5x, prestacao_10x

# Função principal
def main():

    #entrada de dados
    valor = float(input("Digite o valor da compra: "))
    

    #processamento
    desconto_09, prestacao_5x, prestacao_10x = compra(valor, 0, 0, 0)

    #saida de dados
    print(f"Valor com desconto de 9%: {desconto_09:.2f}")
    print(f"Valor da prestação em 5x: {prestacao_5x:.2f}")
    print(f"Valor da prestação em 10x: {prestacao_10x:.2f}")

# Chama a função principal
if __name__ == '__main__':
    main()
