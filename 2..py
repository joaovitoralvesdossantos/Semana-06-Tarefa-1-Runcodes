# Retorna o código unicode do caractere
def caractere(codigo_unicode):
    codigo_unicode = ord(codigo_unicode)
    return codigo_unicode

# Função principal
def main():

    #entrada de dados
    codigo = (input("Digite um caractere: ") + " ")[0]
    #processamento
    caractere_resultado = caractere(codigo)
    #saida de dados
    print("O codigo numérico do caractere é:", caractere_resultado)

# Chama a função principal
if __name__ == '__main__':
    main()