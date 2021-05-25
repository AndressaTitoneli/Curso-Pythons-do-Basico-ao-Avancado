 #Program make a simple calculator
 #This function adds two numbers 
#def add(x, y):
     #return x + y
 # This function subtracts two numbers
#def subtracts(x, y):
     #return x - y
# This function multiplies two numbers
#def multiplies(x, y):
     #return x * y
# This function divides two numbers
#def divides(x, y):
    #return x / y

#print("Select operation.")
#print("1.add")
#print("2.subtracts")
#print("3.multiply")
#print("4.divides")

#def multiplies(x, y):
    #return x * y

#print("Select operation")
#print("multiply")''''

# A Andressa tem 25 anos de idade e mora em Leme

#nome = 'Andressa'
#idade = '26'
#cidade = 'Leme'

#print('A ' + nome + ' tem ' + idade + ' anos de idade e mora em ' + cidade + '.')

#Adicionando Imput = Aula 16

#o imput é quando vc pede para o usuário passar dados ou informações e agrega isto no código.

#nome = input('Qual é o nome da sua sobrinho (a) ')
#anos = input('A quantos anos sua cunhada da migué?  ')
#amor = input('Você amaria o bacuri?  ')
#cidade = input('Pra onde você vai sumir com a Amora? ')


#print(' ' + nome + ' a quantos anos recebe o migué? ' + anos + ' anos, ' + amor + '.' ' Pra onde você vai sumir com a Amora? '  + cidade + '.' ) 

#AULA 17 CALCULANDO A IDADE COM input

#ano_nascimento = input('Em que ano você nasceu? ')
#print(type(ano_nascimento))

#idade = 2021 - int(ano_nascimento)
#print(type(idade))
#print(idade)

#AULA 18. ENTENDENDO O SLICE
#SLICE é um corte, para uso de str cortando informações
#fruta = 'Abacate'
#.    INDEX      esta variavel armazena abacate e ele é armazenado por caracter e cada caracter ganha uma posição dentro da variavel que é  chamada de INDEX
# INDEX sempre vai começar com ZERO exemplo 0123456
#RELACIONANDO A VARIAÇÃO AO INDEX TEMOS
#0=A INDEX
#1=B INDEX
#2=A INDEX
#3=C INDEX
#4=A INDEX
#5=T INDEX
#6=E INDEX

#print(fruta[-1])

#ENTÃO PARA BUSCAR O INDEX ESPECIFICO DE UMA VARIAVEL PRECISA SER USADO [] E DENTRO DE UM PRINT
#SE QUISER PEGAR MAIS LETRAS EXEMPLO DO 2 ATÉ O 5 PRECISA USAR : FICANDO DESTA FORMA [2:5]
#NO PYTHON O INDEX SEMPRE VAI RETORNAR 1 LETRA ANTES ENTÃO SE [2:5] LOGO RETORNO SERÁ aca E NÃO acat ISTO OCORRE PORQUE É UMA REGRA DE PYTHON | ATENÇÃO NO PYTHON É PERMITIDO AGREGAR VALOR NEGATIVO OU SEJA É POSSÍVEL USAR DA SEGUINTE FORMA E OBTER RESULTADO [-1] = e A CONTAGEM SEGUE DESTA FORMA: -1,-2,-3,-4,-5,-6...CONTANDO INVERTIDO etacaba

#valor = 99.75
#valor =str(valor)
#INDEX 01234
#print(valor[3:5])

#ou seja slice é pegar porções de dados e trabalhar com eles via index.

# AULA 19. UTILIZANDO FORMATED STRINGS
#serve para facilitar a leitura da str e facilitar a inserção de variaveis dentro da str e ficara mais lóggico de ler e executar

# A Andressa Titoneli é uma excelente [Programadora]
#nome = 'Andressa'
#sobrenome = 'Titoneli'
#profissao = 'Programadora'

#texto = 'A ' + nome + ' ' + sobrenome + ' é uma excelente ' + '[' + profissao + ']'

#texto2 = f'A {nome} {sobrenome} é uma excelente [{profissao}]'

#print(texto)
#print(texto2)
#COMO CHAGAR NO MESMO RESULTADO COM UMA QUANTIDADE MENOR DE CARACTER OU PALAVRAS / TEXTO.?
#FORMATAR TEXTO OU STRINGS SEMPRE SERÁ INICIADA COM A LETRA 'F'

#STR SEM FORMATAR :
#nome = 'Andressa'
#sobrenome = 'Titoneli'
#profissao = 'Programadora'

#texto = 'A ' + nome + ' ' + sobrenome + ' é uma excelente ' + '[' + profissao + ']'
#print(texto)

#COM A STRING FORMATADA ATRAVEZ DO F E TUDO QUE CONTER DENTRO SERA IMPIMIDO DA MESMA FORMA, SÓ QUE COM A STR FORMATADA É POSSÍVEL ADICIONAR SEM TER QUE FORMATAR AS VARIAVEIS DENTRO DA MINHA STR.
#nome = 'Andressa'
#sobrenome = 'Titoneli'
#profissao = 'Programadora'

#texto2 = f'A {nome} {sobrenome} é uma excelente [{profissao}]'

# AULA 20. METODOS PARA STRINGS
#METODOS DENTRO DE UMA STRING É O FORMATO QUE VC TEM DE ALTERAR TEXTO, ENCONTRAR TEXTO, MODIFICAR TEXTO DENTRO DE UMA STR. para adicionar um metodo basta inserir o nome da sua variavel . e o metodo.

#mensagem = 'Eu adoro comida Caseira'

#print(mensagem.lower()) ATENTA sempre precisa abrir ( ) ao adicionar o método.
#lowe vai deixar todas as letras em minusculo

#print(mensagem.upper())
#upper vai deixar todas as letras em maiusculo

#print(mensagem.capitalize()) 
#Capitalize ele pega sem pre a primeira letra da string e coloca ela em maiusculo.
#mensagem = 'Eu adoro comida Caseira'
#INDEX      0123456789
# 0e|1u|2espaço|3a|4d|5o|6r|7o|8espaço|9c|10o|11m|12i|13d|14a|15espaço|16c|17a|18s|19e|20i|21r|22a|
#print(mensagem.find('C'))
#find vai procurar a posição da letra informada e apresentará na tela o valor em número do local desta letra.
# O Python, é um case sensitive ou seja se colocar um C em caixa alta então ele vai pegar dentro da variavel a letra C em maisculo.

#print(mensagem.find('adoro')) #Também é possível procurar a onde inicia uma palavra.

# atenção, sempre que retornar no console o valor -1 é porque não foi encontrado a palavra dentro da variavel procurada. Então e possível criar regra para quando o resultado for negativo -1 ele retornar um erro para o usuário.

#mensagem = 'Eu adoro comida Caseira'

#print(mensagem.replace('a', 'e')) usando letras
# replace ele vai localizar o antigo e o novo, então identificar o que vc tem e o qu eprecisa trocar e por qual precisa trocar.

#print(mensagem.replace('Caseira', 'feita em casa')) #usando palavras

#mensagem = '       Eu adoro comida Caseira'
#print(mensagem.strip())
#Strip ela vai remover qualquer espaço que tenha antes do primeiro caracter, antes da primeira letra.

#BUSCAR MAIS MÉTODOS E APLICAR OS MÉTODOS!

# AULA 21. OPERAÇÕES MATEMÁTICAS DENTRO DE PYTHON

# Parenteses calculo = (2 + 2) * 3 

# Exponenciais calculo = 2 ** 3 + 4 

# Multiplicação e Divição  calculo = 2 + 2 * 3 / 2 (VEM SEMPRE ANTES DE) se tiver este na mesma linha ele executa sempre da esquerda para direita. 

# Adição e Subtração calculo = 2 + 2 * 3

#calculo = 2 + 2 * 3 / 2

#print(calculo)

# AULA 22. OPERADORES DE COMPARAÇÃO

#   ==  Equal                       IGUAL operadores = 10 == 10 então TRUE se = 10 == 11 então FALSE
#   !=  Not equal                   DIFERENTE operadores = 10 != 10 então FALSE
#   >   Greater than                MAIOR operadores = 20 > 10 então TRUE se  = 10 > 20 então FALSE
#   <   Less than                   MENOR operadores = 10 < 20 então TRUE se = 30 < 20 então FALSE
#   >=  Greater than or equal to    MAIOR OU IGUAL A = 93 >= 10 OR = 12 >= 92 então FALSE
#   <=  Less than or equal to       MENOR OU IGUAL A = 10 <= 93 então TRUE OR = 93 <= 10 então FALSE

#operadores = 12 >= 92

#print(operadores)

# AULA 23. OPERADORES DE ATRIUIÇÃO  OU ASSIGNMENT OPERATORS
#É UMA FORMA QUE TEMOS DE REALIZAR CALCULOS MATEMATICOS COM UM CODIGO UM POUCO MAIS SIMPLES DO QUE O NORMAL

#x = 10
#x = x + 5
#print(x)

#AGORA ESCREVENDO DE FORMA MAIS SIMPLES

#x = 10
#x = x + 5
#x += 5
#x -= 5
#x *= 5
#x /= 5
#x %= 3 # significa que ele conta quanto 3 existem dentro de 10 ou seja 3+3+3=9 resanto 1 pra 10.

#print(x)

#e um formato de colocar as operações de forma simples com o mesmo resultado.

# SEÇÃO 6. controle de fluxo: AULA 24. IF , ELSE -> declarações condicionadas

#ndentation sempre será criado com 4 caracter e sempre que adicionar if 

#velocidade = 60


#if velocidade > 110:
#criou um sistema chamado ndentation e se contar tem 4 espaços, tudo que colocar aqui embaixo será referente ao IF informado acima.
#    print('Acima da velocidade permitida')
#    print('Favor reduzir a sua velocidade')
#elif velocidade < 60:
#    print('Favor dirigir acima de 60Km/h')
# ELIF É PERMITIDO USAR SEM LIMITAÇÃO!

#else:
#    print('Velocidade OK!')

# AULA 25. OPERADORES LÓGICOS

# EXERCICIO: PRECISARÁ APROVAR UM FINANCIAMENTO, A PESSOA PRECISA TER UMA RENDA ACIMA DE 5.000,00 E NOME LIMPO

#renda_acima_5mil = False
#nome_limpo = False

#if renda_acima_5mil or nome_limpo: #pode usar and ou OR o and valida os 2 o OR um ou outro.
#    print('Financiamento aprovado')

#else:
#    print('Financiamento negado')

# AULA 26. OPERADORES TERNÁRIO -> É A FORMA QUE TENHO DE ECONOMIZAR UMA GRANDE LINHA DE CÓDIGO COM IF, ELS, STATEMENT

#idade = 13
#if idade >= 16:
#    resultado = print('Voto permitido')

#else:
#    resultado = print('Voto não permitido')

#AGORA USANDO OPERADOR TERNÁRIO É POSSÍVEL REDUZIR AS 4 LINHAS DE COMANDO EM 1 LINHA SÓ.
#idade = 12
#resultado = 'Voto permitido' if idade >= 16 else 'Voto não permitido'
#print(resultado)


#AULA 27. MULTIPLOS OPERADORES DE COMPARRAÇÃO -> ISSO SIGNIFICA QUE PODE SER COLOCAR AND, OR, MAIOR OU IGUAL ETC...

#  EXEMPLO/EXERCICIO:
#  IMAGINA QUE VC ADMINISTRA UM SITE E VÁRIAS PESSOAS PUBLICAM PRODUTO DENTRO DO SITE, SÓ QUE PRA PUBLICAR UM PRODUTO EXISTE UMA REGRA, ONDE O PRODUTO PRECISA CUSTAR ENTRE R$20,00 E R$40,00 SE O PRODUTO CUSTA 19,00 ELE NÃO PODE ENTRAR E SE FOR ATÉ 40,00 PODE ENTRAR E ACIMA DE 40,00.

#valor = 20

#if 20 <= valor < 40:

#if valor >= 20 and valor < 40:
#    print('Produto foi Aceito')

#else:
#    print('Produto não aceito')

# AULA 28 FOR LOOP - UTILIZANDO NÚMEROS 

#Pode ser usado em todas as parter do código, quando precisar de algo repetitivo / dentro de variável ...pode ser utilizado pra número, strings, scripts...

#FOR LOOPS para Número:
#TAREFA: IMPRIMIR DE 1 A 5

#print('1')
#print('2')
#print('3')
#print('4')
#print('5')

#Com for loops usando variável ele vai rodar:
#in = Na
# range = quantidade de vezes que quer rodar o loop
#Python, sempre conta por Index então sempre vai pegar o ZERO

#for numero in range(0, 12000):
#   print(numero)



# AULA 29 FOR LOOP - UTILIZANDO STRINGS

#imprimir index por index: 

#for letra in 'Google':
#    print(letra)

#palavra = 'Google'
#for letra in palavra:
#    print(letra + '  esta dentro da palavra Google')

#palavra = 'Andressa'
#for letra in palavra:
#    print(f' {letra} esta dentro da palavra {palavra}')
# A vantagem deste formato é que poderá ser alterado a palavra = 'Google', por qualquer outra que o comando será aplicado sem erros e sem precisar mudar mais nada ...


# AULA 30 FOR LOOP - UTILIZANDO IF  E  ELSE
# Enviar um E-mail com os detalhes da compra Online. (Máximo 3 tentativas) para compras confirmadas.

#compra_confirmada = False
#dados_compra = 'Compra no valor de R$12,50 e entrega confirmada'


#for enviar in range(3):
#    if compra_confirmada:
#        print(dados_compra)
#        print('Detalhes enviado para o seu E-mail')
#        break
    
#else:
#    print('Falha na compra')

# AULA 31 FOR LOOP - UTILIZANDO NESTED LOOPS

# é loop dentro de um outro loop.

# Outer loop
# Inner Loop
'''
for numero1 in range(5):
    print(numero1)
    for numero2 in range(5):
        print(numero2, numero1)
'''
# O LOOP FAZ O GIRO DENTRO DELE MESMO

#for numero1 in range(1, 6):
#    print('Produto' + str(numero1)) 
#    for numero2 in range(11):
#        print(numero2, numero1)


# AULA 32 FOR LOOP - UTILIZANDO SEPARANDO STRINGS
#CRIAR UM LOOP PRA PEGAR CADA LETRA E ADICIONAR ESPAÇO.

# == FOR LOOP NESTED ==
# Outer loop    
# Inner loop

# Modificar de FANTASTICO para F A N T A S T I C O 

#palavra ='FANTASTICO'

#for spaco in palavra:
#    print(f' {spaco}' , end='')

# AULA 33 FOR LOOP - Criando um Retangulo:

#Ou seja, criar um comando pra imprimir um retangulo, onde vai criar linhas e colunas em look.

# Outer loop
# Inner loop
#Criar um retangula 6 por 6

'''
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
'''
'''
linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()    
'''

# AULA 34 - Conhecendo o While Loop

'''
WHILE LOOPS
EXCELENTE PARA LOOPS DEPENDENTES DE UMA CONDIÇÃO

CRIAR UMA PROMOÇÃO PARA UM PRODUTO NO VALOR DE R$100,00
A CONDIÇÃO É DE QUE A CADA DIA O PRODUTO FICARÁ R$05,00 MAIS BARATO.
1 DIA VENDA DE 100,00
2 DIA VENDA DE 95,00 E ASSIM ...
o valor de compra do SKU é de 20,00 então ao chegar em 20,00 parar a promoção.
'''
'''
valor = 100
dia = 0
while valor > 20:
    dia += 1
    print(f' No dia {dia} o produto vair ser vendido por: R$ {valor}')
    valor -= 5
'''

# AULA 35 - Diferenças entre FOR LOOP e While Loop
'''
• if else sempre executa 1 vez só e sempre quando for verdadeiro

• for loop precisa de um comando de ação, só reoda se você ordenar: para essa variavel e gira x vezes.

• While Loop,precisa de comando pra parara a variavel e se for isto ou aquilo gire x vezes.

if e else é verdadeiro ou falso, true or false e vai rodar 1 x só.

for loop vai rodar quando vc não sabe o tamanho do seu looop.

o while loop trabalho com condições e também é possível fazer com for loop e if else, porém o while é mais fácil
'''
# RESUMO:
# IF ELSE é pra uma condição de verdadeiro ou falso e ele não fica girando.

# FOR LOOP é quando você sabe o que você quer, ex. quero que gire por 5x.

# WHILE LOOP é quando você não sabe quantas vezes precisa girar, você espera atingir um resultando, ex. quando estiver cansado então pare de girar, o cansado é a condição.


# AULA 36 - CRIANDO CONDIÇÕES COM WHILE LOOP:
'''
Simular : loja virtual vende produtos de 3º, porém quando o cliente tenta publicar um produto, será adicionado um valor de 10% do valor do Produto e só pode ser aplicado em cima de produto com valor superior a 20,00.
'''
# Excelente para loops dependentes de uma condição.

# Publicar um produto com comissão de 10% se for acima de R$20,00
'''
valor = int(input('Digite o valor do seu produto R$: '))
print(valor)

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f' O valor final do seu produto será de R$ {valor}')
    break
'''

# AULA 37. DE FUNCTIONS A LIBRARIES

# function = Exemplo / analogia usada de um supermercado:

#Imagine a função como sendo um ITEM dentro do mercado, então vamos colocar o ITEM como MAÇA 
# MAÇÃ TEM: PESO , COR , VALOR R$ 

#IMAGINE QUE DENTRO DO PROGRAMA VC PRECISA UTILIZAR ESTE ITEM MAÇA E TRAZER ESTA INFORMAÇÃO OU REUTILIZAR ESTES VALORES VARIAS VEZES, ENTÃO É INTELIGENTE FAZER O USO DO FUNCTION!


# module = OBS. QUANDO TEMOS MAIS DE 1 FUNÇÃO OU ITEM MAÇÃ/BANANA ETC...ENTÃO USAMOS O MODULO, ENTÃO  É POSSÍVEL CONVERTER TUDO DENTRO DE UM MÓDULO E CRIAR UM NOME PRA ELE DE SESSÃO.
#SESSÃO DE FRUTAS E VERDURAS 

#então se criar um módulo é possível acelerar e reduzir a quantidade de linhas dentro do código. 
'''
sessão  fruta e verduras
sessão de beleza 
sessão de carner e etc...'''

# package = É possível pegartodas estas sessões:
'''
sessão  fruta e verduras
sessão de beleza 
sessão de carner e etc...'''

# E jogar dentro do PACKAGE, e uma package é um grupo de sessões e cada sessão é um grupo de funções 

#  Package vai se chamar super mercado A 
#  super mercado A é especialista em comidas do Brasil.
# super mercado B é especialista em comidas do caribe.
# super mercado C é especialista em comigas do compra_confirmada


# library =  Sendo assim tendo o Grupo de package, é possível levar para LIBRARY , que é uma biblioteca do grupo do super mercado, exemplo Hyper Markert. ou qualquer outro nome para o grupo de PACKAGE


# AULA 38. COMO FUNCIONA UMA FUNÇÃO

# Função = imagina que vc tem um pedaçã de código que resolve algum problema... 
#  Função é um grupo com um nome definido que poderá ser chamado no final do código para que não precise fazer um processo de repetição


# EXEMPLO:

# FUNCTIONS (FUNÇÕES)

# DRY - Don't repeat yourself.

# IMPORTANTE: QUANDO 
# quando criado uma função ela fica armazenada em alguma parte da memória, e não é retornado em tela. Para que apareça em tela precisará ser chamada/executada.
'''

def boas_vindas():
    print('Olá')
    print('Temos 5 laptops em estoque')

boas_vindas()

# IMAGINE QUE temos estes prints que precisam ser chamados novamente, para não ter que escrever:
#     print('Olá')
#     print('Temos 5 laptops em estoque')
# PARA CADA UM, é só colocar a boas_vindas() ou seja chamar a função!

print('Teste 1')
print('Teste 2')
print('Teste 3')
print('Teste 4')
print('Teste 5')
print('Teste 6')

boas_vindas()

'''

#  AULA 39. CRIANDO UMA FUNÇÃO DE setattr

# FUNCTIONS (FUNÇÕES)

# DRY - Don't repeat yourself.

# as variaveis e as funções, trabalham um pouco diferente, por exemplo:

# criar uma funçaõ onde precisa ser somado o número 1 e número 2 , criar dentro de função. 

'''
numero1 = 10
numero2 = 5
resultado = numero1 + numero2
print(resultado)
'''
'''
def somar_dois_numeros():
    numero1 = 10 # variável
    numero2 = 5 # variável
    resultado = numero1 + numero2 # variável
    print(resultado)


somar_dois_numeros()
'''
# SE APAGAR:
'''
numero1 = 10
numero2 = 5
resultado = numero1 + numero2
print(resultado)
'''
#NÃO SERÁ RETORNADO NADA EM TELA, PORQUE PRECISARÁ CHAMAR A FUNÇÃO QUE ESTA DENTRO DE DEF

# importante: por definição sempre criar 2 espação depois de criar uma função porque fica mais organizado.

''' 
Se 
    numero1 = 10 # variável
    numero2 = 5 # variável
    resultado = numero1 + numero2 # variável

...CONTINUAR A AULA ...
'''
'''
def somar_dois_numeros():
    numero1 = 10 # variável
    numero2 = 5 # variável
    resultado = numero1 + numero2 # variável
    print(resultado)


somar_dois_numeros()'''
'''
PERGUNTA: A variavel número1 e número2 e a resultado, elas estão somente dentro da função ou podemos chamar elas pra fora?

Existe uma diferença entre as variaveis, as variaveis que estão fora são chamadas de variaveis globais e as que estão dentro são chamadas de variaveis de dentro da função.

ENTÃO, variavel número1 e número2 e a resultado estão dentro da função, então elas pertencem aquela função e não a parte global.
'''
'''def somar_dois_numeros():
    numero1 = 10 # variável
    numero2 = 5 # variável
    resultado = numero1 + numero2 # variável
    print(resultado)


somar_dois_numeros()
'''
#Então se colocar esta variavel:
#print(resultado)

#Será retornado um erro em tela:
'''Traceback (most recent call last):
  File "main.py", line 582, in <module>
    print(resultado)
NameError: name 'resultado' is not defined'''
# Este erro informa que a variavel não esta dento da função, ou seja, ela não é uma variavel global

#Abaixo esta um exemplo de duplicar função com as mesmas variaveis sem problema nenhum.
'''
def somar_dois_numeros():
    numero1 = 10 # variável
    numero2 = 5 # variável
    resultado = numero1 + numero2 # variável
    print(resultado)

def somar_dois_numeros1():
    numero1 = 10 # variável
    numero2 = 2 # variável
    resultado = numero1 + numero2 # variável
    print(resultado)

somar_dois_numeros()
somar_dois_numeros1()
'''
# OU SEJA, conseguimos trabalhar com 2 funções diferentes ou mais, sem erros no Python, porque ele entende que são 2 blocos e deverá ser tratado totalmente independente do restante do meu código

# AULA 40. PARÂMETROS E ARGUMENTOS EM UMA FUNÇÃO 

# FUNCTIONS (FUNÇÕES)

# DRY - Don't repeat yourself.

# ABAIXO TEMOS UMA FUNÇÃO:
'''def boas_vindas_Jacqueline():
    print('Olá Jacqueline')
    print('Temos 5 laptops em estoque')

boas_vindas()'''
#COMO ESTENDER PARA 2 OU MAIS CLIENTES?
'''
def boas_vindas_Jacqueline():
    print('Olá Jacqueline')
    print('Temos 5 laptops em estoque')

def boas_vindas_Monique():
    print('Olá Monique')
    print('Temos 1 laptops em estoque')

def boas_vindas_Andressa():
    print('Olá Andressa')
    print('Temos 53 laptops em estoque')

boas_vindas_Jacqueline()
boas_vindas_Monique()
boas_vindas_Andressa()
'''
# criado 3 funções e chamei as funções, mas agora quero que caia de 3 pra 1 só, usando PARÂMETROS

# COM PARAMETRO -> Argumento 
'''
def boas_vindas(nome,quantidade):
    print(f' Olá {nome}')
    print(f' Temos {str(quantidade)} laptops em estoque')

boas_vindas('Andressa', 5)
boas_vindas('Monique', 1)
boas_vindas('Jacqueline', 3)
'''
# Argumento é quando você coloca pra chamar a função.

# oU SEJA, COM PARAMETRO É POSSÍVEL REDUZIR A QUANTITADE DE LINHA OU SEJA DO CÓDIGO.

# AULA 41. ARGUMENTOS DEFAULT E NON-DEFAULT

# VERIFICAR O QUE ACONTECE SE COLCOAAR MAIS ARGUMENTOS, MENOS ARGUMENTOS, SE NÃO FOREM IGUAIS?

# FUNCTIONS 
    # DRY - Don't repeat yourself
        # Parametro -----> Argumento
            # Default = Aquele que você define o valor no parametro.

            # Non-Default = Aquele que você não define o valor no parametro.
'''
def boas_vindas(nome,quantidade):
    print(f' Olá {nome}')
    print(f' Temos {str(quantidade)} laptops em estoque')

boas_vindas('Andressa', 5)             
'''
# Para cada parametro temos 1 argumento:
# ex. parametro nome = argumento Andressa.
# ex. parametro quantidade = argumento 5.

# Então se retirar 1 argumento e manter 2 paramentros o sistema vai retornar o seguinte erro: boas_vindas('Andressa')

'''
Traceback (most recent call last):
  File "main.py", line 672, in <module>
    boas_vindas('Andressa')             
TypeError: boas_vindas() missing 1 required positional argument: 'quantidade


def boas_vindas(nome,quantidade):
    print(f' Olá {nome}')
    print(f' Temos {str(quantidade)} laptops em estoque')

    No erro é informado que:missing 1 required positional argument: 'quantidade
    ou seja, missing é a posição, sendo assim a posição é obrigatória. 

boas_vindas('Andressa')

e este erro também vai acontecer se colocar mais argumentos que parametro.

'''

'''

def boas_vindas(nome,quantidade=5):
    print(f' Olá {nome}')
    print(f' Temos {str(quantidade)} laptops em estoque')

boas_vindas('Andressa')  
'''

#REGRA
#  Se for definir algum parametro para que ele vira algum argumento depois, ele tem que estar sempre no final. 
# SEMPRE COLOCAR NO FINAL

# def boas_vindas(nome='Andressa', quantidade): errado

# def boas_vindas(quantidade, nome='Andressa'): correto

# nome='Andressa' =  Default argumento que define o valor
# quantidade = Non-Default argumento que não define o valor

# AULA 42. PRINT OR RETURN EM FUNÇÕES
'''
Funções basicamente fazem 2 coisas 
1 realizam uma tarefas 
2 retornam um valor

realizar um tarefa = imprima isto na tela'
retornar um valor = é de este resultado 
 
Como identificar 
esta é uma tarefa :

def cliente1(nome):
    print(f' Olá {nome}')

cliente1('Maria')

não armazena nenhum dado e não é possível colocar em uma variavel 


qual a diferença: é que o return armazena os dados e permite trabalhar com várias variaveis :

def cliente1(nome):
    print(f' Olá {nome}')

cliente1('Maria')

def cliente2(nome):
    return f'Olá 1{nome}'
   
cliente1('José')


FOR Ex. 
'''
'''
def cliente1(nome):
    print(f'Olá {nome}')

def cliente2(nome):
    return f'Olá {nome}'
   
cliente1('Maria')
print(cliente2('José'))

x = cliente1('Maria')
y = cliente2('José')

print(x)
print(y)

'''

#  AULA 43. VÁRIOS ARGUMENTOS XARGS COM NÚMEROS

# CRIAR UMA FUNÇÃO, SÓ QUE EM SEUS ARGUMENTOS, PRECISAM ESTAR INDEFINIDOS, PRA CONSEGUIR COLOCAR VÁRIOS ARGUMENTOS MAIS OU MENOS. 
'''
Neste código abaixo, não vai somar a variavel porque não existe um for loop ...
def soma(*numeros):
    return numeros

# quando colocamos o *, informamos ao sistema que existe a possibilidade de entrar vários número all

x= (2,3,4,7)

print(x)
'''

# VEJA COMO FICA COM O LOOP
'''def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado    

x= soma(2,3)

print(x)'''

# AULA 44. VÁRIOS ARGUMENTOS XARGS NOMEANDO PARAMETROS.

# Para identificar meus argumentos, como pode ser feito?

# Functions 
    # DRY - Don't repeat yourself
    # Vários argumentos (xargs) identificando parametro.

# Criar uma função que armazena numeros e strings (DADOS)    
# 1 * vários argumentos // ** vários parametros.
'''def agencia(**carro):
    return carro

print(agencia(marca='Gol', cor='Branco', motor=1.0, placa='ABC123'))
print(agencia(marca='Gol', cor='verde', motor=2.0))
print(agencia(marca='Gol', cor='Azul', motor=1.0, placa=1234))

'''
# AULA 45. IMPORTANDO UM MÓDULO

# Qual o fatorial de 4
# 4*3*2*1=24
'''
import math

print(math.factorial(40))
'''
'''
fatorial = 4 * 3 * 2 * 1
print(fatorial)
'''


# ESTRUTURA DE DADOS

# AULA 46. Introdução a listas:

#Variaveis são usadas para armazenar alguma informação na memória.


# Criar uma lista de cidades brasileiras.
# Todas as listas começa e finaliza com conchete []


'''

cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador']

print(cidades)
'''
# Quando temos uma grande quantidade de dados para manter em uma só variável, é usado listas!

# AULA 47. Manipulando Listas 

# Como pegar apenas 1 item de 1 lista e modificar este item.

# Listas elas podem ser números também

'''
cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador']
numeros = [2, 4, 6]

print(cidades)
print(numeros)
'''


'''
cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']
#                 0               1           2           3  

# print(cidades[I N D E X])
print(cidades[-3])
'''
# PARA MUDAR UM PRODUTO
'''
cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']
#                 0               1           2           3  
cidades[3] = 'Brasilia'
# print(cidades[I N D E X])
print(cidades)
'''
# ACESSAR A DOCUMENTAÇÃO PYTHON, LISTA DE FUNÇÕES.
# AULA 48. FUNÇÕES DENTRO DE LISTAS
'''
cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']
#                 0               1           2           3  

#cidades.append('Santa Catarina')
# APPEND vai pegar o valor informado e levar para o final da lista.

#cidades.remove('Salvador')
#remove = remove o item na lista 

#cidades.insert(1, 'Santa Catarina')
# INSERT = Inserir com base na posição requerida um valor.

#cidades.pop(0)
# POP = Retira a posição conforme informado

cidades.sort()
# SORT = Organizar em ordem alfabetica 
print(cidades)
'''
# AULA 49. CONCATENANDO LISTAS 

# COLOCAR 2 LISTAS JUNTAS / COLOCAR UMA LISTA DENTRO DA OUTRA. 

# Armazenas mais de uma informações em variáveis
# Manter a sequencia dos dados em uma variável
'''
numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

final = numeros + letras
#final = numeros * 8

print(final)
'''

'''
numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

numeros.extend(letras)

print(numeros)
'''
#listas dentro de listas 
'''
numeros = [1, 2, 3, 4]
print(numeros[0])
#I N D E X: 
'''
#               0                   1
'''itens =['item1', 'item2'], ['item3', 'item4']'''
#         0         1         0         1
# É possível buscar itens dentro destas posições.
#print(itens)
'''
print(itens[1][1])
'''

# AULA 50. EXTRAINDO VARIÁVEIS/DADOS DE LISTAS

'''
produtos = ['arroz', 'feijão', 'laranja', 'banana']
#              0        1          2         3
item1 = produtos[0]
item2 = produtos[1]
item3 = produtos[2]
item4 = produtos[3]


print(item1)
print(item2)
print(item3)
print(item4)
'''
# como reduzir o código acima:
'''
produtos = ['arroz', 'feijão', 'laranja', 'banana']
#              0        1          2         3

item1, item2, item3, item4  = produtos

print(item1)
print(item2)
print(item3)
print(item4)
'''
'''
produtos = ['arroz', 'feijão', 'laranja', 'banana', 4, 5, 6]
#              0        1          2         3

item1, item2, *outros, item5  = produtos

print(item1)
print(item2)
print(item5)
print(outros)
'''
# AULA 51. Looping dentro de uma lista 

# Armazenar mais de uma informação em variáveis
# Manter a sequencia dos dados em uma variável

'''
valores = [50, 80, 110, 150, 170]

for x in valores:
    print(f' O valor final do produto é de R${x}.')
'''
# AULA 52. Verificando itens em uma lista 
'''

cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
    print('Em estoque')
else:
    print('Não temos esta cor em estoque!')


'''
# lower() = Sempre permitirá que o usuário possa buscar a informação independente se a for em caixa alta ou não, obs. no código a lista deve conter as informações sempre em cx baixa.


# AULA 53. Agregando duas listas com Zip
'''
cores = ['amarelo', 'verde', 'azul', 'vermelho']
#           0          1       2         3     
valores = [10, 20, 30, 40]
#           0   1   2   3
'''
'''
Agrupando cor dentro do valor, retorna dessa forma:
amarelo|10
verde|20
'''
# Como extrair uma lista de uma string 

#var = ´['c', 'o', 'm',]...
'''
var = list('comprar')
print(var)
'''
'''
duas_listas = zip(cores, valores)
print(list(duas_listas))
'''
# AULA 54. Input em uma lista

# Armazenar mais de uma informação em variáveis

# Manter a sequencia dos dados em uma variável 

# Criar uma lista de frutas a partir do input fornecido pelo usuário.abs 
'''
frutas_usuario = input('Digite o nome das frutas separados por virgula: ')

frutas_usuario = frutas_usuario.split(', ')


print(frutas_usuario)

['banana', 'maca', 'abacate']

'''
# AULA 55. ENTENDENDO SOBRE TUPLES

# Qual a diferença entre listas e tuples? quando devo usar a lista e quando devo usar um tuples? 

# Armazenar mais de uma informação em variáveis

# Manter a sequencia dos dados em uma variável

# Não podem ser alteradas (Immutable)

# lista como identificar: sempre será identificada por [] e tuples pelo: ()
'''
cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

cores_list.append('Roxo')

print(cores_list)
'''
'''
print(type(cores_list))
print(type(cores_tuple))

duas_listas = cores_list * 2
print(duas_listas)
'''
# Usando o Tuple,  não é possível adicionar itens como é adicionado dentro de uma lista.

'''
Com lista isto é permitido:

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

cores_list.append('Roxo')

print(cores_list)

Com Tuples não é permitido 

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

cores_tuples.append('Roxo')

print(cores_list)

Lista que pode ser alterado, então usar list
se não, então tuples. 
list gasta um espaço maior que tuples e tuples é mais rápido que a list, então se for criar uma lista que não vai preciar ser alterada usar tuples. 

'''

# Aula 56. Trabalhando com Arrays 

# Usar o Arrays, que for uma lista grande então usar Arrays e podendo alterar os dados armazenados. 

# Array (Matriz)
# Similar a lista 
# Melhor performance
'''
from array import array

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd'])
letras = array('i', [10, 20, 30, 40])
letras = array('f', [1.2, 2.2, 3.2])

print(letras)
print(numeros_i)
print(numeros_f)
'''
# Aula 57. Criando Sets 
# Set (Listas)
#Similares a listas
#Evita itens duplicados
#Não utiliza Index 
'''
list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]


num1 = set(list1)
num2 = set(list2)

print(num1 | num2)# Union 
print(num1 - num2)# Differernce
print(num1 ^ num2)# Symetric Differernce
print(num1 & num2)# And


print(len(num1))
#  |  --> retira o valor repetido 

'''
# Aula 58 Funções em sets 
'''
list1 = set([1, 2, 3, 4, 5])
s1 = {1, 2, 3, 4, 5}
s1.add(7) ou .update[]
s1.remove(1) --> ele gera erro se o item não existir na lista
s1.discard(3) --> não gera erro em tela
# Se estiver com algum número duplicado, usando o SET ele não vai retornar em tela o item duplicado.

print(list1)
print(s1)
print(type(list1))
print(type(s1))
'''
# Aula 59. Sets com Strings 
'''
set1 = {'a', 'b', 'c', 'd'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.difference(set3)
#intersection
#symetric_difference

print(set4)

'''

# Aula 60. Introdução a Dicionário 

#Utiliza o index no formato de Keys e Values
#Aceita String, Integer, Flot, Boolean...
'''
aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

print(aluno['nome'])
'''

'''
import pandas as pd
import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.basketball-reference.com/leagues/NBA_2018_totals.html')
if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content

soup = BeautifulSoup(content, 'html.parser')
table = soup.find(name='table')

table_str = str(table)


table = soup.find(name='table', attrs={'id':'confs_standings_W'})


'''

'''
import pandas as pd
import requests
from bs4 import BeautifulSoup
#import matplotlib.pyplot as plt
import seaborn as sns
sns.barplot(x='Year', y='3PA')


def scrape_stats(base_url, order_start, order_end):
    order_start = range(order_start,order_end+1,1)

    final_df = pd.DataFrame()

    for year in order_start:
        print('Extraindo order {}'.format(order_start))
        req_url = base_url.format(order_start)
        req = requests.get(req_url)
        soup = BeautifulSoup(req.content, 'html.parser')
        table = soup.find('table', {'id':'totals_stats'})
        df = pd.read_html(str(table))[1]
        df['Order'] = order_end
        final_df = final_df.append(df)
    return final_df
url = 'https://www.bing.com/search?q=paises+do+mundo&cvid=566a93097a2442e59613d8f9c71db04d&aqs=edge.0.0j69i57j0l5.4118j0j1&pglt=803&FORM=ANNTA1&PC=U531'
df = scrape_stats(url, 1, 195)
numeric_cols = df.columns.drop(['Player','Pos','Tm'])
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)
'''
'''
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.head()
df.info()
df.columns
df.values
df.loc[1]
df.set_index('PassengerId', inplace=True)
df.head(12)
df.loc[[1,2,3]]
df.loc[[1,2], ['Name','Sex','Age']]
df.loc[10:20]
df.loc[10:30:2]
df.loc[10:]
df.loc[1:10, ['Name','Sex','Age']]
df.query('Age > 20').head()
df.query('Age > 20 & Sex=="male"').head(10)
df.query('Age > 20 | Sex=="male"').head(10)
df.query('Embarked in ["C","Q"]', inplace=True)
df.head()
df.select_dtypes(include=['object'])
df.select_dtypes(include=['float'])
'''



# Aula 61. Atualizando listas dentro do Dicionário
'''
aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}
'''
# aluno['nome'] = 'Jose' altera o keys ou aluno.update({}) permite atualizar mais de um campo ao mesmo tempo.
#aluno.update({'nome': 'Maria', 'idade': 30})

#print(aluno)

#print(aluno.get('endereço'))
# Com o GET pode ser manipulado os dados adicinando ou buscando informações Keys 
'''
del aluno['idade']
# del vai remover o kay informado 
print(aluno)
'''
# Aula 62. Looping dentro de um Dicionário

# Dicionários
# Utiliza Index no formato de Keys e Values
# Aceita strings, integer, float, boolean...
'''
aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

for keys, values in aluno.items():
    print(keys, values)
'''

# Aula 63. Visualizando itens, keys e values 

'''
aluno = {
    'nome': 'Ana', 
    'idade': 16, 
    'nota_final': 'A', 
    'aprovação': True, 
    'Materias': ['Fisica', 'Matematica', 'Ingles']
}

print(aluno)
# adicionando mais VALORES
print(aluno.get('Materias'))
print(len(aluno)) # faz contagem de Keys

print(aluno.items())
print(aluno.keys())
print(aluno.values())

'''
# Aula 64. Conhecendo a Função lambda

# É uam função (pequena) sem nome: ou seja, não precisa dar um nome pra ela, é possível associar a uma variável.
# Pode ter vários argumentos mas somente 1 expressão
# Muito utilizada dentro de outras funções
# Código mais "clean" (limpo)

#Existe a possibilidade de reduzir o código abaixo:

#def somar(x):
#    return x + 10
#print(somar(2))
# com 1 linha é possível fazer o calculo.
#somar10 = lambda x: x + 10
#print(somar10(2))
# para mais de 1 expressão:
#somar10 = lambda x,y: x + y + 10
#print(somar10(2, 4))

# Aula 65. lambda dentro de uma função/outra função
'''
def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

print(somar(2))    
'''

# AULA 66. Função MAP em uma LISTA 
# A função MAP é do Python, foi criada pro py. então não precisa ser importada pra usar.

# VERFICIAR NA WEB -> Built-in Function : são as funções pré construidas do py e não precisam ser importadas. 

# Map Function (Mapear funções)
# Muito utilizado com listas 
# Aplicar uma função a um Iterable, por ite. (list, tuple, dic, etc.)
'''
lista1 = [1, 2, 3, 4]

def multi(x):
    return x * 2

#print(multi(2))    

lista2 = map(multi, lista1)

print(list(lista2))
'''
# com o map é possível fazer com que uma função seja aplicada a itens dentro de uma lista 

# AULA 67. FUNÇÃO MAP COM LAMBDA 

# Map Function (Mapear funções)
# Muito utilizado com listas 
# Aplicar uma função a um Iterable, por ite. (list, tuple, dic, etc.)

#lista1 = [1, 2, 3, 4]

#def multi(x):
#    return x * 2
#lista2 = map(lambda x: x * 2, lista1)

#print(list(map(lambda x: x * 2, lista1)))
#test
'''
lista3 = [190, 208, 3330, 46660, 540, 60, 77770, 83330, 92220, 150]
print(list(map(lambda x: x + 5 * 30, lista3)))
'''
# AULA 68.  FUNÇÃO FILTER

# FAZ O MESMO QUE O MAP, NO SENTIDO DE RODAR UMA FUNÇÇAO DENTRO DE UMA LISTA FILTRANDO OS RESULTADOS. 
'''
valores = [10, 12, 43, 44, 57]
'''
#def remover20(x):
 #   return x > 20


#print(list(filter(remover20, valores)))
'''
print(list(filter(lambda x: x > 20, valores)))
'''

# AULA 69. ENTENDENDO LIST COMPREHENSION COM STRINGS
# Mais simples de se escrever
# Utilizado quando você precisa criar uma nova lista a partir de uma existente 
# [expressao for iten in itens]
# Criando listas com for loop, selecionando frutas com a letra B
'''
frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
frutas2 = []

for iten in frutas1:
    if 'c' in iten:
        frutas2.append(iten)

print(frutas2)        
'''
# Como obter o mesmo resultado dentro de 1 linha de código:
'''
frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
frutas2 = [iten for iten in frutas1 if 'c' in iten]
print(frutas2) 
'''
# AULA 70. ENTENDENDO LIST COMPREHENSION COM NÚMEROS 

# Loja, gerar uma lista onde custo sobe de 10 em 10 $, mostrando os vlaores 0, 10, 20, 30, 40 e 50.
'''
valores = []

for x in range(6):
    valores.append(x * 10)


print(valores)
'''
'''
valores = [x * 10 for x in range(6)]
print(valores)
'''

# AULA 71. Lista e Generator Expressions  
# Generator Expressions 
    # Uma forma mais rápida paraListas, Dicinários e etc.
        # Menos memória alocada.
            # Valores em bytes
'''
from sys import getsizeof

numeros = [x * 1 for x in range(1000000)]            
print(type(numeros))

print(getsizeof(numeros))

print('====')

numeros = (x * 2 for x in range(1000000))
print(type(numeros))

print(getsizeof(numeros))

# SE FOR PRECISO CRIAR LISTA E GERAR VALORES DENTRO DA LISTA, USAR O Generator Expressions  

'''
# AULA 72. O que são erros...

# AULA 73. Trabalhando com o Try e Except com uma lista 

#Como isolar uma função, para o código continuar:
'''
try:
    letras = ['a', 'b', 'c']
   # Index    0    1    2

    print(letras[3])
except IndexError:
    print('Index não existe')
'''
 # AULA 74.  Trabalhando com o Try e Except com o input
'''
try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)

except ValueError:
    print('Favor digitar o valor em número')

print('mais codigo abaixo')
'''
# AULA 75. Adicionando Else e Finally
'''
try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)

except ValueError:
    print('Favor digitar o valor em número')

finally:
    print('codigo Ok')

else:
    print('Usuario digitou um valor correto!')
    resultado = valor * 2
    print(resultado)



print('mais codigo abaixo')

'''
# AULA 76. Conhecendo Classes 
# Programação orientada a objetos 

# Python Object-Oriented Programming

# Classes 
    # Utilizadas para criar Objetos (Instances)
    # Objetos são partes dentro de uma class (Instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
    # ====
    # Class: Frutas
    # Objects: Abacata, Banana...


'''
Criar função:

sempre:

def _______ ():
    ______
    ______
def _______ ():
    ______
    ______  

Com o Class, o sistema gera um grupo e tudo que for criado, todas as funções e etc será pertencente a uma determinada Classe:

class ________:

def _______ (): # Funções 
    ______ # Dados
    ______ # Dados
def _______ (): # Funções
    ______ # Dados
    ______ # Dados 

nome = 'Andressa'
nome_lower = nome.lower() # sempre que adicionado um . significa que estamos trabalhando com métodos. 
print(nome_lower)
'''
# Criar um sistema pra uma empresa, onde sera armazenado os dados dos funcionários.

# Depois de criado, começar a adionar valores. que não constam no programa, e tudo desenvolvido dentro de classes. 

# AULA  77. Criarndo a 1ª class

# Python Object-Oriented Programming

# Classes 
    # Utilizadas para criar Objetos (Instances)
    # Objetos são partes dentro de uma class (Instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
    # ====EXEMPLO:
    # Class: Frutas
    # Objects: Abacata, Banana...


 # SEMPRE QUANDO CRIAR CLASSES A 1ª LETRA DEVE SER EM CX ALTA E SEMPRE TERMINA COM : 
# Criando classes com dados:
'''
class Funcionarios:
    nome = 'Elena'
    sobrenome = 'Cabral'

Funcionarios()    # para chamar a classe
'''

'''
class Funcionarios:
    nome = 'Elena'
    sobrenome = 'Cabral'
    data_nascimento = '01/08/1995'

usuario1 = Funcionarios()

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)
'''

# A melhor forma de  usar classes é usando funções. 

# AULA  78. Criarndo Objetos dentro de uma Classe 

# Python Object-Oriented Programming

# Classes 
    # Utilizadas para criar Objetos (Instances)
    # Objetos são partes dentro de uma class (Instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar

# Criar objetos e associar aos parametros 
'''

# Criar a classe
class Funcionarios:
    pass

# Criar o objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

# Criar os paramentros do usuario1
usuario1.nome = 'Andressa'
usuario1.sobrenome = 'Titoneli'
usuario1.data_nascimento = '01/08/1995'

# Criar os paramentros do usuario2
usuario2.nome = 'Jacqueline'
usuario2.sobrenome = 'Soares'
usuario2.data_nascimento = '07/09/1986'

# Print
print(usuario1.nome)
print(usuario2.sobrenome)

'''

# AULA  79. Criando Contrutores 

# O objetivo dos contrutores é reduzir a passagem de parametros, apresentando os argumentos e passando os parametros de forma mais simples. 

'''
# Criar a classe
class Funcionarios:
#Mandatorio sempre com init porque estamos trabalhando com construtor || Todos os construtor utilizam o SELF, o self significa que ele vai utilizar os objetos. 
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self = data_nascimento = data_nascimento
# então o self sempre será, exemplo: objeto.argumento ou seja, usuario1.nome e quando ele terminar ele passa para o próximo.

# Para passar os paramentro devemos colocar dentro dos ( )
# Criar o objeto
usuario1 = Funcionarios('Andressa', 'Titoneli', '01/08/1995')
usuario2 = Funcionarios('Jacqueline', 'Soares', '07/09/1986')
usuario3 = Funcionarios('Monique', 'Bezerra', '29/01/1993')

# Print
print(usuario1.sobrenome)
print(usuario2.sobrenome)
print(usuario3.nome)

#...  nome, sobrenome, data_nascimento) <--- Argumentos que são paramentro 

'''

# AULA 80. Adicionando mais funções a classe 

# Com 1 classe é possível trabalhar com várias funções. 
# Classes 
    # Utilizadas para criar Objetos (Instances)
    # Objetos são partes dentro de uma class (Instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
'''
# Criar a classe
class Funcionarios:
#Mandatorio sempre com init porque estamos trabalhando com construtor || Todos os construtor utilizam o SELF, o self significa que ele vai utilizar os objetos. 
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self = data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + '  ' + self.sobrenome
# então o self sempre será, exemplo: objeto.argumento ou seja, usuario1.nome e quando ele terminar ele passa para o próximo.

# Para passar os paramentro devemos colocar dentro dos ( )
# Criar o objeto
usuario1 = Funcionarios('Andressa', 'Titoneli', '01/08/1995')
usuario2 = Funcionarios('Jacqueline', 'Soares', '07/09/1986')
usuario3 = Funcionarios('Monique', 'Bezerra', '29/01/1993')

# Print
# Existe a possibilidade de reduzir este ProcessLookupError

print(usuario1.nome + '  ' + usuario1.sobrenome)
print(usuario2.nome + '  ' + usuario2.sobrenome)
print(usuario3.nome + '  ' + usuario3.sobrenome)

# Print
# print(usuario1.nome + '  ' + usuario1.sobrenome)
print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario2))
'''
# AULA 81. Calculando a Idade do Funcionário. 

# Criar uma nova função, dentro da class que calcula a idade 
'''
# Criar a classe
from datetime import datetime 
class Funcionarios:

   def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

   def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

   def idade_funcionario(self):
       ano_atual = datetime.now().year
       self.ano_nascimento = int(ano_atual - self.ano_nascimento)
       return self.ano_nascimento

# Criar o objeto
usuario1 = Funcionarios('Andressa', 'Titoneli', 1995)
usuario2 = Funcionarios('Jacqueline', 'Soares', 1986)
usuario3 = Funcionarios('Monique', 'Bezerra', 1993)

# Print
#print(usuario1.nome + ' ' +usuario1.sobrenome)
#print(usuario1.nome_completo())
print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))
print(Funcionarios.idade_funcionario(usuario3))
'''
# AULA 82. Criando 1 Modulo 
# criar modulos, pegando partes de códigos a partir de outros arquivos. 

# cada arquivo tem sua caracteristicas
# pra cada modulo, adicionar arquivos pertinentes ao mesmo.

# AULA 83. Importando um modulo.
# importar com import
# importar com from 
'''
import funcoes

funcoes.somar()
funcoes.multi()

'''

'''
from funcoes import somar, multi

somar()
multi()

'''
# AULA 84. Criando e Importando Packages 
'''
from funcoes import somar
from funcoes import multi
from items.cadastro import cliente

somar()
multi()
cliente()
'''
# AULA 85. Aplicando um modulo
'''
from funcoes import find_index

list1 = ['a', 'b', 'c', 'd', 'e']

var1 = find_index(list1, 'e')
print(var1)
'''

# AULA 86. Desafios/explicando como funciona.

# AULA 87. If Else - Ponto do Steak 



Dividir o valor total da área (parede) pelo valor de rendimento

o valor corresponde a quantidade de tinta necessária


8 / 3,685
































































































