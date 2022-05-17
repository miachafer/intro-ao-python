# Escreva um código que imprima cada palavra da letra de música abaixo apenas uma vez.
# A saída deve estar ordenada (ordem lexicográfica).
# Saída esperada: And Breathe Come Down Everlong Hello Hold I I'll I'm I've If Out She Slow, So The Tonight, When You've again along always and anything ask away be been breathe can could down ever everything feel for forever good got head head, her here how in into it know me my myself not now of only out over promise real red sang say she sing stop the thing this throw to waited wanted waste when with wonder you you've your

# Dica: Python oferece recursos mais interessantes para trabalhar com strings, como aspas triplas que permitem escrever
# longos textos mais facilmente. Elas funcionam como as aspas, mas permitem digitar a mensagem em várias linhas.
everlong_foo_fighters = """
Hello
I've waited here for you
Everlong
Tonight, I throw myself into
And out of the red
Out of her head, she sang
Come down and waste away with me
Down with me
Slow, how you wanted it to be
I'm over my head
Out of her head, she sang
And I wonder
When I sing along with you
If everything could ever be this real forever
If anything could ever be this good again
The only thing I'll ever ask of you
You've got to promise not to stop when I say when
She sang
Breathe out
So I can breathe you in
Hold you in
And now
I know you've always been
Out of your head
Out of my head, I sang
And I wonder
When I sing along with you
If everything could ever feel this real forever
If anything could ever be this good again
The only thing I'll ever ask of you
You've got to promise not to stop when I say when
She sang
And I wonder
If everything could ever feel this real forever
If anything could ever be this good again
The only thing I'll ever ask of you
You've got to promise not to stop when I say when
"""

# Tirando as quebras de linha sem usar o splitlines
letra_sem_quebra_de_linha = everlong_foo_fighters.replace('\n', ' ')

# Tirando as vírgulas
letra_sem_virgula = letra_sem_quebra_de_linha.replace(', ', ' ')

# Finalmente transformando as palavras da música em uma lista de palavras
palavras = letra_sem_virgula.split(' ')

# Criando um set com as palavras - trata-se aqui de um conjunto de palavras onde nenhuma delas se repete
conjunto = set(palavra for palavra in palavras)

# Transformando o set em uma lista novamente para ordená-la com o método sort()
palavras_unicas = list(conjunto)

# Ordenando a lista usando o método sort()
palavras_unicas.sort()

# Tranformando a lista em uma string novamente
string_de_palavras = ' '.join(item for item in palavras_unicas)

print(string_de_palavras) # Output:  And Breathe Come Down Everlong Hello Hold I I'll I'm I've If Out She Slow So The Tonight When You've again along always and anything ask away be been breathe can could down ever everything feel for forever good got head her here how in into it know me my myself not now of only out over promise real red sang say she sing stop the thing this throw to waited wanted waste when with wonder you you've your
