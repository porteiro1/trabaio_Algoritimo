# Manipulação de Dados com Listas Compostas e Arquivos em Python

## Objetivo

Demonstrar o uso de **listas compostas (listas aninhadas)** e **manipulação de arquivos de texto em Python**, integrando ambos os conceitos em um sistema simples de cadastro de alunos.

---

# Parte 1 – Listas Compostas

Uma **lista composta** é uma lista que contém outras listas. Ela é muito utilizada para armazenar registros com múltiplas informações, como alunos, produtos, filmes ou funcionários.

## Exemplo 1 – Estrutura Básica

```python
alunos = [
    ["Ana", 8.5],
    ["Bruno", 7.0],
    ["Carlos", 9.2]
]

print(alunos)
```

---

## Exemplo 2 – Inserindo Dados com `append()`

```python
alunos = []

alunos.append(["Ana", 8.5])
alunos.append(["Bruno", 7.0])
alunos.append(["Carlos", 9.2])

print(alunos)
```

---

## Exemplo 3 – Entrada do Usuário

```python
nome = input("Nome: ")
nota = float(input("Nota: "))

alunos.append([nome, nota])
```

---

## Atualização e Remoção de Dados

```python
# Atualizando a nota de Bruno
alunos[1][1] = 8.0

# Removendo Carlos
alunos.remove(["Carlos", 9.2])

print(alunos)
```

---

## Percorrendo uma Lista Composta

```python
for aluno in alunos:
    print(f"Nome: {aluno[0]}")
    print(f"Nota: {aluno[1]}")
    print("-" * 20)
```

### Explicação

O laço `for` percorre cada elemento da lista principal. Cada elemento é outra lista contendo os dados do aluno.

---

# Parte 2 – Manipulação de Arquivos TXT

O comando `with open()` é a forma recomendada para trabalhar com arquivos em Python, pois garante o fechamento automático do arquivo.

## Estrutura Básica

```python
with open("arquivo.txt", "modo") as arquivo:
    # operações
```

---

## Leitura de Arquivos (`r`)

```python
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
```

---

## Leitura Linha por Linha

```python
with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

---

## Escrita e Inclusão de Dados

### Criando ou sobrescrevendo um arquivo (`w`)

```python
with open("dados.txt", "w") as arquivo:
    arquivo.write("Ana\n")
    arquivo.write("Bruno\n")
```

### Adicionando informações ao final do arquivo (`a`)

```python
with open("dados.txt", "a") as arquivo:
    arquivo.write("Carlos\n")
```

### Diferença entre os modos

| Modo | Função |
|--------|--------|
| `w` | Apaga o conteúdo anterior e grava novos dados |
| `a` | Mantém o conteúdo existente e adiciona novas informações |

---

## Alteração de Dados

```python
with open("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()

for i in range(len(linhas)):
    if linhas[i].strip() == "Bruno":
        linhas[i] = "Bruno Silva\n"

with open("dados.txt", "w") as arquivo:
    arquivo.writelines(linhas)
```

---

# Parte 3 – Integração: Sistema de Cadastro de Alunos

Agora será criado um pequeno sistema que utiliza **listas compostas** e **arquivos TXT** juntos.

## Lista de Alunos

```python
alunos = [
    ["Ana", 18, 8.5],
    ["Bruno", 20, 7.0],
    ["Carlos", 19, 9.2]
]
```

---

## Salvando no Arquivo

```python
with open("alunos.txt", "w") as arquivo:
    for nome, idade, nota in alunos:
        arquivo.write(f"{nome};{idade};{nota}\n")
```

### Conteúdo gerado em `alunos.txt`

```txt
Ana;18;8.5
Bruno;20;7.0
Carlos;19;9.2
```

---

## Reconstruindo a Lista na Memória

```python
alunosRecuperados = []

with open("alunos.txt", "r") as arquivo:
    for linha in arquivo:
        nome, idade, nota = linha.strip().split(";")

        alunosRecuperados.append([
            nome,
            int(idade),
            float(nota)
        ])
```

---

## Exibindo os Dados Recuperados

```python
for nome, idade, nota in alunosRecuperados:
    print(nome, idade, nota)
```

### Saída

```txt
Ana 18 8.5
Bruno 20 7.0
Carlos 19 9.2
```

---

# Fluxo do Sistema

```text
Cadastro dos Alunos
        ↓
Lista Composta
        ↓
Salvar em Arquivo TXT
        ↓
Ler Arquivo TXT
        ↓
Reconstruir Lista
        ↓
Utilizar Dados
```

---

# Conclusão

Neste trabalho foram apresentados os conceitos fundamentais de **listas compostas** e **manipulação de arquivos em Python**.

Também foi demonstrada a integração entre essas técnicas por meio de um sistema de cadastro de alunos, permitindo **salvar** e **recuperar** informações de forma permanente.

Esses conceitos servem como base para o desenvolvimento de sistemas mais complexos e para o uso futuro de **bancos de dados**, tornando o armazenamento de informações mais eficiente e organizado.
