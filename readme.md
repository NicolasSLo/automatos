# Implementação de Autômatos Finito Determinístico (AFD) e de Pilha Determinístico (APD)

Este projeto demonstra a implementação de um Autômato Finito Determinístico (AFD) e um Autômato de Pilha Determinístico (APD) simulados em linguagem de programação Python. O objetivo é aplicar os fundamentos teóricos da computação de forma prática.

## Estrutura do Projeto

O projeto é composto por um único arquivo Python que permite ao usuário escolher qual autômato deseja testar.

## Autômato Finito Determinístico (AFD)

### Descrição da Linguagem

[cite_start]O AFD implementado reconhece cadeias binárias que representam números inteiros divisíveis por 4[cite: 9]. [cite_start]Um número binário é múltiplo de 4 se o seu sufixo for `00` (termina com dois zeros)[cite: 9]. [cite_start]O autômato simula a leitura desses números bit a bit e verifica se a palavra atende a essa regra[cite: 9].

**Exemplos de palavras aceitas:**
* [cite_start]`100` [cite: 11]
* [cite_start]`1000` [cite: 12]
* [cite_start]`1100` [cite: 13]
* [cite_start]`10000` [cite: 14]

**Exemplos de palavras rejeitadas:**
* [cite_start]`1` [cite: 16]
* [cite_start]`10` [cite: 17]
* [cite_start]`11` [cite: 18]
* [cite_start]`101` [cite: 19]
* [cite_start]`111` [cite: 20]

### Função de Transição (AFD)

[cite_start]A função de transição do AFD é a seguinte[cite: 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137]:

* $\delta(q1, 0) = q1$
* $\delta(q1, 1) = q2$
* $\delta(q2, 1) = q2$
* $\delta(q2, 0) = q3$
* $\delta(q3, 1) = q2$
* $\delta(q3, 0) = q4$
* $\delta(q4, 1) = q2$
* $\delta(q4, 0) = q4$

O estado inicial é $q1$. O estado de aceitação é $q4$.

### Exemplo de Execução (AFD)

[cite_start]**Palavra: `100`** [cite: 309]
* [cite_start]Estado atual: q1, lê `1` $\rightarrow$ vai para q2 [cite: 310, 311]
* [cite_start]Estado atual: q2, lê `0` $\rightarrow$ vai para q3 [cite: 312, 313]
* [cite_start]Estado atual: q3, lê `0` $\rightarrow$ vai para q4 [cite: 314, 315]
* [cite_start]Estado final: q4 (estado de aceitação) [cite: 316]
* [cite_start]**Resultado: Aceita** [cite: 317]

[cite_start]**Palavra: `101`** [cite: 318]
* [cite_start]Estado atual: q1, lê `1` $\rightarrow$ vai para q2 [cite: 319, 320]
* [cite_start]Estado atual: q2, lê `0` $\rightarrow$ vai para q3 [cite: 321, 322]
* [cite_start]Estado atual: q3, lê `1` $\rightarrow$ vai para q2 [cite: 323, 324]
* [cite_start]Estado final: q2 (não é estado de aceitação) [cite: 325]
* [cite_start]**Resultado: Rejeitada** [cite: 326]

## Autômato de Pilha Determinístico (APD)

### Descrição da Linguagem

[cite_start]O APD reconhece o conjunto de todas as palavras palíndromas de comprimento par, formadas pelos símbolos 'a' e 'b'[cite: 23]. [cite_start]Uma palavra palíndroma pode ser lida da esquerda para a direita ou da direita para a esquerda com o mesmo resultado[cite: 24]. [cite_start]Este APD rejeita automaticamente palavras de tamanho ímpar, mesmo que sejam palíndromos, pois o símbolo central não encontra correspondência[cite: 25].

[cite_start]Durante a execução, o autômato empilha e desempilha após comparar os símbolos opostos da palavra (por exemplo, o primeiro símbolo com o último, o segundo com o penúltimo e assim por diante)[cite: 26]. [cite_start]Se, ao final da execução, não restar nada na pilha e a palavra tiver sido totalmente lida, significa que ela foi aceita pelo autômato[cite: 27].

**Exemplos de palavras aceitas:**
* [cite_start]`aa` [cite: 29]
* [cite_start]`abba` [cite: 31]
* [cite_start]`baab` [cite: 32]
* [cite_start]`aabbaa` [cite: 33]

**Exemplos de palavras rejeitadas:**
* [cite_start]`a` (ímpar) [cite: 35]
* [cite_start]`aba` (ímpar, apesar de ser palíndromo) [cite: 36]
* [cite_start]`abb` (não é palíndromo par) [cite: 37]
* [cite_start]`abab` (não é palíndromo) [cite: 38]

### Exemplo de Execução (APD)

[cite_start]**Palavra: `abba`** [cite: 328]
* [cite_start]Lê 'a' (posição 1) $\rightarrow$ empilha 'A' $\rightarrow$ Pilha: [A] [cite: 331]
* [cite_start]Lê 'a' (posição 4, reversa) $\rightarrow$ corresponde $\rightarrow$ desempilha $\rightarrow$ Pilha: [ ] [cite: 332, 333]
* [cite_start]Lê 'b' (posição 2) $\rightarrow$ empilha 'B' $\rightarrow$ Pilha: [B] [cite: 334]
* [cite_start]Lê 'b' (posição 3, reversa) $\rightarrow$ corresponde $\rightarrow$ desempilha $\rightarrow$ Pilha: [ ] [cite: 335, 336]

[cite_start]**Resultado final:** [cite: 337]
* [cite_start]Palavra: $\lambda\lambda\lambda\lambda$ [cite: 338] (representa a palavra vazia após processamento)
* [cite_start]Pilha: [ ] [cite: 339] (pilha vazia)
* [cite_start]Palavra é par e a pilha ficou vazia. [cite: 340]
* [cite_start]**Resultado: Aceita** [cite: 341]

[cite_start]**Palavra: `aba`** [cite: 342]
* [cite_start]Lê 'a' (posição 1) $\rightarrow$ empilha 'A' $\rightarrow$ Pilha: [A] [cite: 344]
* [cite_start]Lê 'a' (posição 3, reversa) $\rightarrow$ corresponde $\rightarrow$ desempilha $\rightarrow$ Pilha: [ ] [cite: 345, 349]

[cite_start]**Resultado final:** [cite: 346]
* [cite_start]Palavra: `λbλ` [cite: 347] (o 'b' do meio permanece, representado como $\lambda$ nos exemplos)
* [cite_start]Pilha: [ ] [cite: 348] (A pilha fica vazia após a comparação dos caracteres opostos 'a'. O caractere central 'b' é o que determina se a palavra é ímpar)
* [cite_start]Palavra é ímpar e sobrou um símbolo (o do meio), logo ela será rejeitada. [cite: 350]
* [cite_start]**Resultado: Rejeitada** [cite: 350]

## Como Executar

Para executar o programa, você precisa ter Python instalado.

1. Clone este repositório:
   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   cd <NOME_DO_SEU_REPOSITORIO>
