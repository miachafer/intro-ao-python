from datetime import date, datetime, timedelta

# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro

# Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele

# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta

# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta

# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não
# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.

### SOLUÇÃO

print('Digite a data do seu próximo aniversário no formato dd/mm/aaaa: ')
aniversario = input()

dia_de_hoje = date.today()

# Usei a função slice para isolar cada elemento da data e depois transformei cada elemento em um número inteiro
dia_aniversario = int(aniversario[0:2])
mes_aniversario = int(aniversario[3:5])
ano_aniversario = int(aniversario[6:])

# Transformei a data em um objeto do tipo date, lembrando que: datetime(year, month, day)
aniversario = date(ano_aniversario, mes_aniversario, dia_aniversario)

# Fiz a diferença entre o dia do aniversário (sempre será no futuro) e o dia_de_hoje.
# Novamente usei a função slice depois de ter tornado a variável diferença em string para filtrar apenas o número de dias de diferença entre as datas, que não pode ter mais do que 3 dígitos
diferenca = str(aniversario - dia_de_hoje)[0:3]

print('Seu aniversário é daqui a {} dias'.format(diferenca))

print()

gosta_aniversario = input("Você gosta de aniversário? (s/n) ")
vai_ter_festa = input("Você vai fazer festa? (s/n) ")

if gosta_aniversario == 's' and vai_ter_festa == 's':
    print("Você vai ganhar presente!")
else:
    print("Você não vai ganhar presente :(")
    