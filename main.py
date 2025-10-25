# Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir que todos
# os registros tenham valores positivos para quantidade e preço. Escreva um programa
# que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

# ex1
# quantidade = int(input("Digite a quantidade vendida: "))
# preco = float(input("Digite o preço do produto: "))

# if(quantidade > 0 and preco > 0):
#     print("Dados válidos!")
# else:
#     print("Dados inválidos")

# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. 
# Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

#ex 2

temperatura = float(input("Informe a temperatura: "))

if(temperatura < 18):
    print("Temperatura Baixa!")
elif(temperatura >= 18 and temperatura <= 26):
    print("Temperatura Normal!")
else:
    print("Temperatura Alta!")