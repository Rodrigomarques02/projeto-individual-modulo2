
# Lista de candidatos Rodrigo , João , Rafa , Aline , Gustavo.
candidatos = [
    {'nome': 'Rodrigo', 'notas': {'e_': 7, 't_': 8, 'p_': 9, 's_': 8}},
    {'nome': 'João', 'notas': {'e_': 6, 't_': 7, 'p_': 8, 's_': 9}},
    {'nome': 'Rafa', 'notas': {'e_': 9, 't_': 7, 'p_': 6, 's_': 8}},
    {'nome': 'Aline', 'notas': {'e_': 8, 't_': 9, 'p_': 7, 's_': 7}},
    {'nome': 'Gustavo', 'notas': {'e_': 4, 't_': 4, 'p_': 8, 's_': 8}},
]

# Definindo a função de busca.
def buscar_candidatos_por_notas_minimas(lista_candidatos, notas_minimas):
    candidatos_filtrados = []
    for candidato in lista_candidatos:
        notas = candidato['notas']
        if notas['e_'] >= notas_minimas['e_'] and notas['t_'] >= notas_minimas['t_'] and notas['p_'] >= notas_minimas['p_'] and notas['s_'] >= notas_minimas['s_']:
            candidatos_filtrados.append(candidato)
    return candidatos_filtrados

#O usuário deve digitar as notas mínimas em cada prova.
notas_minimas = {}
notas_minimas['e_'] = int(input('Digite a nota mínima em E:'))
notas_minimas['t_'] = int(input('Digite a nota mínima em T:'))
notas_minimas['p_'] = int(input('Digite a nota mínima em P:'))
notas_minimas['s_'] = int(input('Digite a nota mínima em S:'))

# Buscando os candidatos que atendem aos critérios informados
candidatos_selecionados = buscar_candidatos_por_notas_minimas(candidatos, notas_minimas)

# Imprimindo os candidatos selecionados com as notas inseridas pelo usuário.
print('Candidatos selecionados:')
for candidato in candidatos_selecionados:
    notas = candidato['notas']
    print(candidato['nome'] + ' '+ 'e_' + str(notas['e_'])+ 't_' + str(notas['t_'])+ 'p_' + str(notas['p_'])+ 's_' + str(notas['s_']))
