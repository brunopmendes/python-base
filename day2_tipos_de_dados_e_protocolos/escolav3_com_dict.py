'''Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
'''

___version___ = '0.1.2'

# Dados
sala1 = ['Erik', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana']
sala2 = ['Joao', 'Antonio', 'Carlos', 'Maria', 'Isolda']

aula_ingles = ['Erik', 'Maia', 'Joana', 'Carlos', 'Antonio']
aula_musica = ['Erik', 'Carlos', 'Maria']
aula_danca = ['Gustavo', 'Sofia', 'Joana', 'Antonio']

sala = {
    1: ['Erik', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana'],
    2: ['Joao', 'Antonio', 'Carlos', 'Maria', 'Isolda']
}

aula = {
    'Inglês': ['Erik', 'Maia', 'Joana', 'Carlos', 'Antonio'],
    'Música': ['Erik', 'Carlos', 'Maria'],
    'Dança': ['Gustavo', 'Sofia', 'Joana', 'Antonio']
}

# Listar alunos em cada atividade por sala
for chave, valor in aula.items(): #items precisa ser utilizado para acessar valores do dicionário

    print(f"Alunos da aula de {chave}\n")

    # sala1 que tem interseção com a atividade
    atividade_sala1 = set(sala[1]) & set(valor) # OU set(sala1).intersection(set(atividade))
    atividade_sala2 = set(sala[2]) & set(valor) # OU set(sala2).intersection(set(atividade))

    print(f'Sala 1: ', atividade_sala1)
    print(f'Sala 2: ', atividade_sala2)
    print("-" * 50)