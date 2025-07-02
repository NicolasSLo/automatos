# Seletor de execução
escolha = input("Escolha o autômato:\n1 - AFD\n2 - APD\nDigite 1 ou 2:\n")
if escolha == "1":  # Caso o usuário escolha o AFD.
    # AFD de Nicolas Samuel
    # Exemplos:
    # – Aceitas: 100, 1000, 1100, 10000
    # – Rejeitadas: 1, 10, 11, 101, 111
    # Estado inicial = q1
    # Estado de aceitação = q4
    is_accepted = False  # Variável para identificar se a palavra foi aceita.

    def main():
        try:
            palavra = input("Digite a palavra (0, 1):\n")  # Entrada para o autômato ler a palavra.
            if len(palavra) > 0:
                afd(palavra)
            else:  # Caso o usuário não digite nada.
                print("Digite algo!")
                quit()
        except:
            print("Digite apenas 0 ou 1")  # Mensagem de erro para caso o usuário digite algo diferente de 0 ou 1.
            quit()

    def afd(palavra):
        vetor = [int(c) for c in palavra]  # Vetor com cada caractere da palavra.

        nao_aceita = []
        for i in vetor:
            if i not in {0, 1}:  # Caso a palavra tenha algum elemento diferente de 0 ou 1.
                nao_aceita.append(i)
        if len(nao_aceita) != 0:
            print(f"A palavra não pode conter {nao_aceita}!!!")
            quit()

        q1(vetor)  # Chamada do estado inicial.

        if is_accepted:  # Mensagem para mostrar se a palavra foi aceita ou não.
            print(f"A palavra {palavra} foi aceita")
            print("Programador: Nicolas Samuel 72300515")
        else:
            print(f"A palavra {palavra} foi rejeitada")
            print("Programador: Nicolas Samuel 72300515")

    # Estado inicial
    def q1(vetor):
        func_transicao()  # Imprime na tela a função de transição.
        if vetor:  # Verifica se a palavra já foi totalmente lida.
            if vetor[0] == 0:  # Identifica se o caractere é 0; se sim, volta para o estado inicial.
                print(get_palavra(vetor))
                print(f"δ(q1, {vetor[0]}) = q1")
                print(f"=======================")
                vetor.pop(0)
                q1(vetor)

            elif vetor[0] == 1:  # Identifica se o caractere é 1; se sim, passa para o próximo estado.
                print(get_palavra(vetor))
                print(f"δ(q1, {vetor[0]}) = q2")
                print(f"=======================")
                vetor.pop(0)
                q2(vetor)
        else:  # Se a palavra terminar aqui, ela é rejeitada, pois q1 não é um estado de aceitação.
            is_accepted = False

    def q2(vetor):
        global is_accepted

        if vetor:
            if vetor[0] == 1:  # Identifica se o caractere é 1; se sim, volta para o estado atual.
                print(get_palavra(vetor))
                print(f"δ(q2, {vetor[0]}) = q2")
                print(f"=======================")
                vetor.pop(0)
                q2(vetor)

            elif vetor[0] == 0:  # Se o caractere é 0, avança para o próximo estado.
                print(get_palavra(vetor))
                print(f"δ(q2, {vetor[0]}) = q3")
                print(f"=======================")
                vetor.pop(0)
                q3(vetor)

        else:  # Se a palavra terminar aqui, ela é rejeitada, pois q2 não é um estado de aceitação.
            is_accepted = False

    def q3(vetor):
        global is_accepted

        if vetor:
            if vetor[0] == 1:  # Identifica se o caractere é 1; se sim, volta para o estado q2.
                print(get_palavra(vetor))
                print(f"δ(q3, {vetor[0]}) = q2")
                print(f"=======================")
                vetor.pop(0)
                q2(vetor)

            elif vetor[0] == 0:  # Identifica se o caractere é 0; se sim, avança para o próximo estado.
                print(get_palavra(vetor))
                print(f"δ(q3, {vetor[0]}) = q4")
                print(f"=======================")
                vetor.pop(0)
                q4(vetor)

        else:  # Se a palavra terminar aqui, ela é rejeitada, pois q3 não é um estado de aceitação.
            is_accepted = False

    # Estado de aceitação
    def q4(vetor):
        global is_accepted

        if vetor:
            if vetor[0] == 0:  # Identifica se o caractere é 0; se sim, volta para o estado atual.
                print(get_palavra(vetor))
                print(f"δ(q4, {vetor[0]}) = q4")
                print(f"=======================")
                vetor.pop(0)
                q4(vetor)

            elif vetor[0] == 1:  # Identifica se o caractere é 1; se sim, volta para o estado q2.
                print(get_palavra(vetor))
                print(f"δ(q4, {vetor[0]}) = q2")
                print(f"=======================")
                vetor.pop(0)
                q2(vetor)
        else:  # Se a palavra terminar aqui (no estado q4), ela é aceita, pois q4 é um estado de aceitação.
            is_accepted = True

    def get_palavra(palavra):  # Função para converter a lista de caracteres de volta para uma string.
        palavra_inteira = ""
        for i in palavra:
            palavra_inteira += str(i)
        if palavra_inteira == "":
            return "λ"
        else:
            return palavra_inteira

    def func_transicao():  # Função para exibir a função de transição do AFD.
        print(f"+=======================+")
        print(f"Função de transição:")
        print("δ(q1, 0) = q1;")
        print("δ(q1, 1) = q2;")
        print("δ(q2, 1) = q2;")
        print("δ(q2, 0) = q3;")
        print("δ(q3, 1) = q2;")
        print("δ(q3, 0) = q4;")
        print("δ(q4, 1) = q2;")
        print("δ(q4, 0) = q4;")
        print(f"+=======================+")
    main()

elif escolha == "2":  # Caso o usuário escolha o APD.
    # APD de Nicolas Samuel
    # Exemplos:
    # – Aceitas: aa, abba, baab, aabbaa
    # – Rejeitadas: a, aba, abb, abab

    class Pilha:  # Classe da pilha.
        def __init__(self):  # Construtor.
            self.items = []

        def push(self, item):  # Empilha um item.
            self.items.append(item)

        def pop(self):  # Desempilha um item.
            if not self.esta_vazia():
                return self.items.pop()
            return None

        def topo(self):  # Retorna o elemento do topo da pilha.
            if not self.esta_vazia():
                return self.items[-1]
            return None

        def esta_vazia(self):  # Retorna True se a pilha estiver vazia, False caso contrário.
            return len(self.items) == 0

    def main():
        palavra = input("Digite uma palavra com tamanho par (a, b):\n")  # Entrada para o autômato ler a palavra.
        array = list(palavra)  # Array para separar cada caractere.
        if len(palavra) > 0:
            if not all(char in ('a', 'b') for char in array):  # Verifica se a palavra contém apenas 'a' ou 'b'.
                print("A palavra só pode conter 'a' ou 'b'!\n")
                quit()
            else:
                is_accepted = apd(array)  # Chama a execução do APD e armazena o resultado (True ou False).

            if is_accepted:  # Mensagem para mostrar se a palavra foi aceita ou não.
                print(f'A palavra "{palavra}" foi aceita!')
                print("Programador: Nicolas Samuel 72300515")
            else:
                print(f'A palavra "{palavra}" foi rejeitada!')
                print("Programador: Nicolas Samuel 72300515")
        else:  # Caso o usuário não digite nada.
            print("Digite algo!")
            quit()

    def apd(palavra):
        pilha = Pilha()  # Instancia a pilha.
        palavra_temp = palavra.copy()  # Cópia da palavra para fins de exibição.

        tamanho = len(palavra)
        # Variáveis para manipular a posição dos caracteres.
        posicao_atual = 0
        posicao_reversa = tamanho - 1

        print(f"Estado inicial (pilha vazia) [{get_palavra(palavra)},{pilha.items}]")
        print("=============================================================")

        while posicao_atual < posicao_reversa:  # Processa a palavra até que os ponteiros de posição se encontrem.

            if palavra[posicao_atual] == "a":  # Empilha 'A' se o caractere atual for 'a'.
                pilha.push("A")
                print("Empilha A")
                print(f"Palavra: {get_palavra(palavra_temp)}")
                palavra_temp[posicao_atual] = "λ"
                print(f"Lendo 'a' na posição {posicao_atual + 1} [{get_palavra(palavra_temp)},{pilha.items}]")
                print("=============================================================")
            else:
                pilha.push("B")  # Empilha 'B' se o caractere atual for 'b'.
                print("Empilha B")
                print(f"Palavra: {get_palavra(palavra_temp)}")
                palavra_temp[posicao_atual] = "λ"
                print(f"Lendo 'b' na posição {posicao_atual + 1} [{get_palavra(palavra_temp)},{pilha.items}]")
                print("=============================================================")


            if palavra[posicao_reversa] == "a" and pilha.topo() == "A":  # Desempilha se o caractere reverso corresponder.
                pilha.pop()
                print("Desempilha A")
                print(f"Palavra: {get_palavra(palavra_temp)}")
                palavra_temp[posicao_reversa] = "λ"
                print(f"Lendo 'a' na posição {posicao_reversa + 1} [{get_palavra(palavra_temp)},{pilha.items}]")
                print("=============================================================")

            elif palavra[posicao_reversa] == "b" and pilha.topo() == "B":  # Desempilha se o caractere reverso corresponder.
                pilha.pop()
                print("Desempilha B")
                print(f"Palavra: {get_palavra(palavra_temp)}")
                palavra_temp[posicao_reversa] = "λ"
                print(f"Lendo 'b' na posição {posicao_reversa + 1} [{get_palavra(palavra_temp)},{pilha.items}]")
                print("=============================================================")
            else:
                return False  # Se não corresponder, a palavra é rejeitada.

            # Atualiza os ponteiros de posição.
            posicao_atual += 1
            posicao_reversa -= 1

        # Se os ponteiros se encontram (posicao_atual == posicao_reversa),
        # significa que a palavra tem comprimento ímpar.
        if posicao_atual == posicao_reversa:
            return False  # Rejeita, pois a linguagem só aceita palavras de comprimento par.

        # Verifica se o caractere reverso corresponde.
        if palavra[posicao_atual] != palavra[posicao_reversa]:
            return False  # Retorna o resultado da aceitação.

        # Verifica se a pilha está vazia no final.
        if not pilha.esta_vazia():
            return False  # Retorna o resultado da aceitação.

        # Se a posição atual ultrapassou a reversa, a palavra foi lida por completo e é par.
        if posicao_atual > posicao_reversa:
            return True  # Retorna o resultado da aceitação.

    def get_palavra(palavra):  # Função para converter a lista de caracteres de volta para uma string.
        palavra_inteira = ""
        for i in palavra:
            palavra_inteira += i
        if palavra_inteira == "":
            return "λ"
        else:
            return palavra_inteira


    main()

elif len(escolha) <= 0:  # Caso o usuário não digite nada.
    print("Digite algo!")
    quit()
else:  # Caso o usuário digite algo diferente de 1 ou 2.
    print("Digite apenas 1 ou 2 para as escolhas!")
    quit()
