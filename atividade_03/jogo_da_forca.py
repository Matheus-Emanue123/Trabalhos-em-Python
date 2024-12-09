import random

palavras = [
    'python', 'programacao', 'computador', 'teclado', 'mouse', 'monitor', 'internet', 'desenvolvimento',
    'jogo', 'forca', 'codigo', 'algoritmo', 'software', 'hardware', 'dados', 'variavel', 'funcao',
    'sintaxe', 'debug', 'compilador', 'interpretador', 'sistema', 'rede', 'servidor', 'cliente',
    'script', 'biblioteca', 'modulo', 'pacote', 'objeto', 'classe', 'metodo', 'heranca', 'polimorfismo',
    'encapsulamento', 'abstracao', 'estrutura', 'array', 'lista', 'dicionario', 'conjunto', 'pilha',
    'fila', 'grafo', 'arvore', 'no', 'raiz', 'folha', 'recursao', 'iteracao', 'busca', 'ordenacao',
    'insercao', 'exclusao', 'atualizacao', 'string', 'inteiro', 'float', 'booleano', 'arquivo',
    'diretorio', 'sistema_operacional', 'windows', 'linux', 'mac', 'processo', 'thread', 'concorrencia',
    'paralelismo', 'assincrono', 'sincrono', 'api', 'rest', 'json', 'xml', 'html', 'css', 'javascript',
    'framework', 'django', 'flask', 'sqlite', 'postgresql', 'mysql', 'oracle', 'mongodb', 'redis',
    'memcached', 'docker', 'kubernetes', 'virtualizacao', 'cloud', 'aws', 'azure', 'gcp', 'serverless',
    'evento'
]

palavra_secreta = random.choice(palavras)
letras_acertadas = ['_' for _ in palavra_secreta]
tentativas = 8
erros = 0
letras_erradas = []

print('Bem-vindo ao Jogo da Forca!')

while erros < 9 and '_' in letras_acertadas:
    print('\nPalavra: ' + ' '.join(letras_acertadas))
    print(f'Tentativas restantes: {8 - erros}')
    letra = input('Digite uma letra: ').lower()

    if letra in letras_acertadas or letra in letras_erradas:
        print('Você já tentou essa letra.')
        continue

    if letra in palavra_secreta:
        for idx, letra_secreta in enumerate(palavra_secreta):
            if letra == letra_secreta:
                letras_acertadas[idx] = letra
    else:
        erros += 1
        letras_erradas.append(letra)
        print('Letra incorreta!')

if '_' not in letras_acertadas:
    print('\nParabéns! Você acertou a palavra:', palavra_secreta)
else:
    print('\nVocê perdeu! A palavra era:', palavra_secreta)