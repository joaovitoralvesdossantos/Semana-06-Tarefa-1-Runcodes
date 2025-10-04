# Faz o calculo da quantidade de caracteres 
def caracteres(quantidade):
    quantidade = len(quantidade)
    return quantidade

# Função principal
def main():

    #entrada de dados
    nome = input("Digite um nome: ")

    #processamento
    quantidade = caracteres(nome)

    #saida de dados
    print(f"O nome {nome} tem {quantidade} caracteres.")


# Chama a função principal
if __name__ == '__main__':
    main()