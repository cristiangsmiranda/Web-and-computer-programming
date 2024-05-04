country = input('what country do you live? ')
if country.lower() == 'brasil':
    states = input('what states do you live in? ')
    if states in('São Paulo' , 'Rio de Jsneiro' , 'Minas Gerais'):
        tax = 22.12
    elif states in('Bahia' , 'Pernambuco'):
        tax = 27.32
    elif states in('paraná' , 'Espírito Santo'):
        tax = 18.36
    else:
        tax = 26.89
else:
    tax = 0
print(tax)

first = int(input('what is the first number? '))
second = int(input('what is the second number? '))
if first < second:
    print('the first number is not greatest')
else:
    print('the first number is greatest')
if first == second:
    print('the number are iqual')
else:
    print('the number are not iqual')
if second < first:
    print('the second nnumber is not greatest')
else:
    print('the second number is greatest')
print()
animal = input('what is your favorite animal? ')
if animal.lower() == 'cat':
    print('that is my favorite animal too!')
else:
    print('that one is not my favorite.')



#Escreva um programa para determinar se deve emprestar dinheiro com base nas seguintes regras.
emprestimo = int(input('qual o valor do emprestimo? '))
credito = int(input('qual a quantidade do seu histórico de crédito? '))
renda = int(input('qual o valor da sua renda? '))
entrada = int(input('qual o valor da sua entreda? '))
devo_emprestar = True
if emprestimo >= 5:
    if credito >= 7 and renda >= 7:
        devo_emprestar = True
    elif credito >= 7 or renda >= 7:
        if entrada >= 5:
            devo_emprestar = True
        else:
            devo_emprestar = False
    else:
        devo_emprestar = False
    if credito < 4:
        devo_emprestar = False
    else:
        if renda >=7 or entrada >= 7:
            devo_emprestar = True
        elif renda >= 4 or entrada >= 4:
            devo_emprestar = True
        else:
            devo_emprestar = False
if devo_emprestar:
    print('Sim, faremos um emprestimo! ')
else:
    print('não, não faremos o emprestimo! ')

    

#Primeiro, solicite uma classificação de 1 a 10 para os seguintes itens:
#Qual é o valor do empréstimo?
#Qual é a qualidade do seu histórico de crédito?
#Qual é o valor de sua renda?
#Qual é o valor de sua entrada?

#Em seguida, você criará uma variável booleana para saber se deve emprestar o dinheiro,
#que será definida como True (verdadeiro) ou False (falso). Configure uma série de instruções if para
#decidir se sua decisão de emprestar é "sim" ou "não", de acordo com as seguintes regras:

#Primeiro, verifique se o tamanho do empréstimo é de pelo menos 5. Se for, use as seguintes regras:
#Se o histórico de crédito e a renda forem ambos de pelo menos 7, então a decisão é "sim"

#Se o histórico de crédito ou a renda forem de pelo menos 7, verifique se a entrada é
#de pelo menos 5; se for, a decisão é "sim"; se não for, a decisão é "não"

#Caso contrário (se nem o histórico de crédito nem a renda forem de pelo menos 7), a decisão é "não"
#Caso contrário (se o empréstimo não for igual ou superior a 5), use estas regras:
#Se o crédito for menor que 4, a decisão será "não"
#Caso contrário, verifique o seguinte:
#Se a renda ou o pagamento da entrada for de pelo menos 7, a decisão será "sim"
#Se tanto a renda quanto a entrada forem de pelo menos 4, a resposta será "sim"
#Caso contrário, a decisão é "não"
#Por fim, exiba a decisão para o usuário.