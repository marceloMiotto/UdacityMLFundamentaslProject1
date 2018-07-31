# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop
# para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for ind in range(1, 21):
    print(data_list[ind])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for ind in range(20):
    print(data_list[ind][6])


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as
# colunas(features) por índices. Mas ainda é difícil pegar uma coluna
# em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista
# em outra lista, na mesma ordem


def column_to_list(data, index):
    """
    Função para criar uma nova lista a partir de uma coluna especifica
    de outra lista .
    Argumentos:
        data..: lista original
        index.: indice da coluna a ser copiada
    Retorna:
        Uma lista com os valores da coluna especifica
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a
    # feature pelo seu índice, e dar append para uma lista
    for line in data:
        column_list.append(line[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando
# (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])
# verificando o tamanho retornado
print(len(column_to_list(data_list, -2)))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male
# (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
gen_list = column_to_list(data_list, -2)
male = 0
female = 0
for gender_line in gen_list:
    if gender_line == "Male":
        male += 1
    else:
        if gender_line == "Female":
            female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female]
# (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)


def count_gender(data_list):
    """
    Função para contar a quantidade de ocorrencias dos generos
    Masculino e Feminino
    Argumentos:
        datalist: lista contento os registros a serem contados
    Retorna:
        Uma lista com um unico registro com a contagem dos generos
        Masculino e Feminino
    """
    gen_list = column_to_list(data_list, -2)
    male = 0
    female = 0
    for gender_line in gen_list:
        if gender_line == "Male":
            male += 1
        else:
            if gender_line == "Female":
                female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero
# como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.


def most_popular_gender(data_list):
    """
    Função para identificar qual o genero com o maior numero de ocorrencia ou
    se ambos sao iguais
    Argumentos:
        datalist: lista contento os registros a serem contados
    Retorna:
        Uma string com a identificacao do genero com o maior numero de
        ocorrencias "Masculino" "Feminino" ou "Igual"
    """
    gender = count_gender(data_list)
    if(gender[0] == gender[1]):
        answer = "Igual"
    else:
        if(gender[0] > gender[1]):
            answer = "Masculino"
        else:
            answer = "Feminino"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda
# está correta.
print("\nTAREFA 7: Verifique o gráfico!")
# funcao para contar os tipos


def count_type(data_list):
    """
    Função para contar o tipo de usuario
    Argumentos:
        datalist: lista contento os registros a serem contados
    Retorna:
        Uma lista com um unico registro com a contagem dos tipos
        customer ou subscriber
    """
    type_list = column_to_list(data_list, -3)
    customer = type_list.count("Customer")
    subscriber = type_list.count("Subscriber")
    return [customer, subscriber]

type_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]

quantity = count_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print(male)
print(female)
print(len(data_list))
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = ("Os valores sao diferentes porque muitos registros nao possuem " +
          "valor para a coluna genero.")
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora.
# Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
# valor minimo
min_trip = 9999999.
for trip_min in trip_duration_list:
    trip_min_f = float(trip_min)
    if trip_min_f < min_trip:
        min_trip = trip_min_f
print("Min: " + str(min_trip))

# valor minimo
max_trip = 0.
for trip_max in trip_duration_list:
    trip_max_f = float(trip_max)
    if trip_max_f > max_trip:
        max_trip = trip_max_f
print("Max: " + str(max_trip))

trip_mean_f = 0.
trip_qtd = 0
for trip_mean in trip_duration_list:
    trip_mean_f += float(trip_mean)
    trip_qtd += 1
mean_trip = trip_mean_f/trip_qtd
print(str(trip_mean_f))
print(str(trip_qtd))
print(str(mean_trip))

# nova lista
trip_wo_null = []
# remover valores nulos criando uma lista com valores inteiros
for trip_duration_line in trip_duration_list:
    # print(trip_duration_line)
    if not trip_duration_line:
        null
    else:
        # print(trip_duration_line)
        trip_wo_null.append(int(trip_duration_line))

print("Primeiro valor da lista sem nulls: " + str(trip_wo_null[0]))

# ordenar a lista
trip_wo_null.sort()

# verificar impar ou par
list_len = len(trip_wo_null)
list_even = 0
list_odd = 0
if list_len/2 == 0:
    list_even = 1
else:
    list_odd = 1

# realizar o calculo da mediana
if list_even == 1:
    list_index = list_len/2
    median_trip = ((trip_wo_null[round(list_index)] +
                    trip_wo_null[list_index+1]) / 2)
else:
    median_trip = trip_wo_null[round(list_len / 2)]

print(str(median_trip))


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print(("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip,
       "Mediana: ", median_trip))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a
# start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
# nova lista com estacoes iniciais
start_station_list = column_to_list(data_list, 3)
user_types = set(start_station_list)

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções.
# Explique os parâmetros de entrada, a saída, e o que a função faz.
# Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
Função de exemplo com anotações.
Argumentos:
    param1: O primeiro parâmetro.
    param2: O segundo parâmetro.
Retorna:
    Uma lista de valores x.

"""
input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"


def count_items(column_list):
    """
    Função para contar os tipos contidos na lista
    Argumentos:
        column_list..: lista de dados
    Retorna:
        Duas listas sendo a primeira com os tipos de dados e a segunda com a
        contagem dos tipos encontrados
    """
    item_types = []
    count_items = []
    list_types = set(column_list)
    print(list_types)
    item_types = list(list_types)
    print(item_types)
    ind = 0
    for item in item_types:
        count_items.append(column_list.count(item))
    print(count_items)
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
