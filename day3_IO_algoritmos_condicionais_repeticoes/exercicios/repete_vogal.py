"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras
e imprime cada uma das palavras com suas vogais duplicadas.
"""
        
words = []
while True:
    word = input('Digite uma palavra (ou enter para sair): ').strip()

    if not word: # condição de parada
        break
    
    final_word = ''
    for letter in word:
        # TODO: Remover acentuação usando função
        if letter.lower() in 'aeiouãâáêéîíôó':
            final_word += letter * 2
        else:
            final_word += letter
    words.append(final_word)

print(*words, sep="\n")