# Implementação de Autômatos Finito Determinístico (AFD) e de Pilha Determinístico (APD)

Este projeto demonstra a implementação de um Autômato Finito Determinístico (AFD) e um Autômato de Pilha Determinístico (APD) simulados em linguagem de programação Python. O objetivo é aplicar os fundamentos teóricos da computação de forma prática.

## Estrutura do Projeto

O projeto é composto por um único arquivo Python que permite ao usuário escolher qual autômato deseja testar.

## Autômato Finito Determinístico (AFD)

### Descrição da Linguagem

[cite_start]O AFD implementado reconhece cadeias binárias que representam números inteiros divisíveis por 4. [cite_start]Um número binário é múltiplo de 4 se o seu sufixo for `00` (termina com dois zeros). [cite_start]O autômato simula a leitura desses números bit a bit e verifica se a palavra atende a essa regra.

**Exemplos de palavras aceitas:**
* `100`
* `1000`
* `1100`
* `10000`

**Exemplos de palavras rejeitadas:**
* `1`
* `10`
* `11`
* `101`
* `111`

### Função de Transição (AFD)

A função de transição do AFD é a seguinte:

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

**Palavra: `100`**
* Estado atual: q1, lê `1` $\rightarrow$ vai para q2
* Estado atual: q2, lê `0` $\rightarrow$ vai para q3
* Estado atual: q3, lê `0` $\rightarrow$ vai para q4
* Estado final: q4 (estado de aceitação)
* **Resultado: Aceita**

[cite_start]**Palavra: `101`**
* Estado atual: q1, lê `1` $\rightarrow$ vai para q2
* Estado atual: q2, lê `0` $\rightarrow$ vai para q3
* Estado atual: q3, lê `1` $\rightarrow$ vai para q2
* Estado final: q2 (não é estado de aceitação)
* **Resultado: Rejeitada**

## Autômato de Pilha Determinístico (APD)

### Descrição da Linguagem

O APD reconhece o conjunto de todas as palavras palíndromas de comprimento par, formadas pelos símbolos 'a' e 'b'. Uma palavra palíndroma pode ser lida da esquerda para a direita ou da direita para a esquerda com o mesmo resultado. Este APD rejeita automaticamente palavras de tamanho ímpar, mesmo que sejam palíndromos, pois o símbolo central não encontra correspondência.

Durante a execução, o autômato empilha e desempilha após comparar os símbolos opostos da palavra (por exemplo, o primeiro símbolo com o último, o segundo com o penúltimo e assim por diante). Se, ao final da execução, não restar nada na pilha e a palavra tiver sido totalmente lida, significa que ela foi aceita pelo autômato.

**Exemplos de palavras aceitas:**
* `aa`
* `abba`
* `baab`
* `aabbaa`

**Exemplos de palavras rejeitadas:**
* `a` (ímpar)
* `aba` (ímpar, apesar de ser palíndromo)
* `abb` (não é palíndromo par)
* `abab` (não é palíndromo)

### Exemplo de Execução (APD)

**Palavra: `abba`**
* Lê 'a' (posição 1) $\rightarrow$ empilha 'A' $\rightarrow$ Pilha: [A]
* Lê 'a' (posição 4, reversa) $\rightarrow$ corresponde $\rightarrow$ desempilha $\rightarrow$ Pilha: [ ] 32, 
* Lê 'b' (posição 2) $\rightarrow$ empilha 'B' $\rightarrow$ Pilha: [B]
* Lê 'b' (posição 3, reversa) $\rightarrow$ corresponde $\rightarrow$ desempilha $\rightarrow$ Pilha: [ ] 35, 

**Resultado final:**
* Palavra: $\lambda\lambda\lambda\lambda$ (representa a palavra vazia após processamento)
* Pilha: [ ] (pilha vazia)
* Palavra é par e a pilha ficou vazia.
* **Resultado: Aceita**

**Palavra: `aba`**
* Lê 'a' (posição 1) $\rightarrow$ empilha 'A' $\rightarrow$ Pilha: [A]
* Lê 'a' (posição 3, reversa) $\rightarrow$ corresponde $\rightarrow$ desempilha $\rightarrow$ Pilha: [ ] 45, 

**Resultado final:**
* Palavra: `λbλ` (o 'b' do meio permanece, representado como $\lambda$ nos exemplos)
* Pilha: [ ] (A pilha fica vazia após a comparação dos caracteres opostos 'a'. O caractere central 'b' é o que determina se a palavra é ímpar)
* Palavra é ímpar e sobrou um símbolo (o do meio), logo ela será rejeitada.
* **Resultado: Rejeitada**

## Como Executar

Para executar o programa, você precisa ter Python instalado.

1. Clone este repositório:
   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   cd <NOME_DO_SEU_REPOSITORIO>
