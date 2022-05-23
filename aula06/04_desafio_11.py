# Dado um arquivo de entrada, escreva um programa que leia o conteudo do arquivo para uma string,
# e escreva um outro arquivo de saída que imprima o texto ao contrário.
# Exemplo de entrada: Oi mulheres maravilhosas do curso de Python do ConstruDelas!
# Exemplo de saída: !saleDurtsnoC od nohtyP ed\nosruc od sasohlivaram serehlum iO

arquivo1 = 'entrada_desafio_11.txt'

# Abrindo o arquivo1 ('entrada_desafio_11.txt') no modo de leitura
arquivo1_aberto = open(arquivo1, 'r')

# Guardando na variável leitura o conteúdo lido do arquivo1
leitura = arquivo1_aberto.read()

# Criando arquivo2 para escrever o conteúdo invertido do arquivo1
arquivo2 = 'saida_desafio_11.txt'

# Abrindo o arquivo2 recém criado
arquivo2_aberto = open(arquivo2, 'w')

# Escrevendo no arquivo2 o conteúdo invertido do arquivo1
arquivo2_aberto.write(leitura[::-1]) # Verificar arquivo 'saida_desafio_11.txt' e seu conteúdo: "!saleDurtsnoC od nohtyP ed osruc od sasohlivaram serehlum iO"

# Fechando o arquivo2
arquivo2_aberto.close()

# Fechando o arquivo1
arquivo1_aberto.close()
