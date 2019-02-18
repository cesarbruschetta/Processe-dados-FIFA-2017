# coding: utf-8
# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

import csv

def parcer_file():
    data = []
    with open("./data.csv") as f:
        records = csv.DictReader(f)
        for row in records:
            data.append(row)
    return data

DATA = parcer_file()

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
def q_1():
    nationality = [d['nationality'] for d in DATA]
    return len(set(nationality))

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    club = [d['club'] for d in DATA]
    return len(set(club))

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    full_name = [d['full_name'] for d in DATA[:20]]
    return full_name

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    new_data = sorted(DATA, key=lambda k: float(k['eur_wage']), reverse=True)
    full_name = [d['full_name'] for d in new_data[:10]]
    return full_name

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    new_data = sorted(DATA, key=lambda k: k['age'], reverse=True) 
    full_name = [d['full_name'] for d in new_data[:10]]
    return full_name

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    
    result = {}
    for item in DATA:
        
        count = result.setdefault(int(item['age']), 0)
        result[int(item['age'])] = count +1
    
    return result
