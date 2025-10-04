# Converte uma quantidade de segundos em horas, minutos e segundos
def segundos(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

# Função principal
def main():

    #entrada de dados
    segundos = int(input("Digite a quantidade de segundos do evento: "))
    
    #processamento
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    
    #saida de dados
    print(f"O evento tem duração de {horas} horas {minutos:02} minutos e {segundos:02} segundos.")

# Chama a função principal
if __name__ == '__main__':
    main()