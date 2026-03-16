from datetime import *
dataNas = input("Digite sua data de nascimento (AAAAMMDD): ")
dataQuaseFormatada = datetime.strptime(dataNas, "%Y%m%d")
dataFormatada = dataQuaseFormatada.strftime("%d%m%Y")

print(f'Você nasceu em {dataFormatada}')