# Calcula o maior, o menor e a média aritmética 
def cinco_numeros(maior, menor, aritmetica):
    maior = max(maior)
    menor = min(menor)
    aritmetica = sum(aritmetica) / len(aritmetica)
    return maior, menor, aritmetica

# Função principal
def main():

    #entrada de dados
    num1 = float(input("Digite o 1º número: "))
    num2 = float(input("Digite o 2º número: "))
    num3 = float(input("Digite o 3º número: "))
    num4 = float(input("Digite o 4º número: "))
    num5 = float(input("Digite o 5º número: "))

    #processamento
    num = [num1, num2, num3, num4, num5]
    maior, menor, aritmetica = cinco_numeros(num, num, num)

    #saida de dados
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Média aritmética: {aritmetica}")

# Chama a função principal
if __name__ == '__main__':
    main()