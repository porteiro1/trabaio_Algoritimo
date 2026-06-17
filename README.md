# Manipulação de Dados com Listas Compostas e Arquivos em Python

## Objetivo

Neste material você vai aprender dois conceitos que, juntos, formam a base de praticamente todo sistema que guarda informações: **listas compostas (listas aninhadas)** e **manipulação de arquivos de texto**. No final, vamos unir as duas ideias em um sistema simples de cadastro de alunos — exatamente como um banco de dados rudimentar funcionaria.

> 💡 **Por que isso importa?** Toda vez que você usa um app que "lembra" de algo depois que você fecha e abre de novo (uma lista de tarefas, um cadastro, um histórico), por trás existe alguma forma de salvar dados em disco e depois recarregá-los na memória. É exatamente isso que vamos construir aqui, em miniatura.

---

# Parte 1 – Listas Compostas

## 1.1 O que é uma lista composta?

Uma **lista composta** (ou lista aninhada) é simplesmente **uma lista que contém outras listas dentro dela**.

Pense em uma planilha do Excel: cada **linha** representa um registro (um aluno, por exemplo), e cada **coluna** dentro dessa linha é uma informação sobre ele (nome, idade, nota). Uma lista composta em Python representa exatamente essa estrutura:

- A **lista de fora** = a planilha inteira (todos os alunos)
- Cada **lista de dentro** = uma linha da planilha (um aluno específico)

```
alunos = [ [linha 1], [linha 2], [linha 3] ]
            ↑           ↑           ↑
         Ana, 8.5    Bruno, 7.0   Carlos, 9.2
```

## 1.2 Estrutura básica

```python
alunos = [
    ["Ana", 8.5],
    ["Bruno", 7.0],
    ["Carlos", 9.2]
]

print(alunos)
```

Aqui, `alunos` é uma lista com 3 elementos. Cada elemento, por sua vez, é **outra lista** com 2 informações: nome e nota.

**Como acessar um valor específico?** Use dois índices, um para a linha e outro para a coluna — assim como faria em coordenadas de uma matriz:

```python
print(alunos[0])       # ['Ana', 8.5]  -> a lista inteira do primeiro aluno
print(alunos[0][0])    # 'Ana'         -> o nome do primeiro aluno
print(alunos[0][1])    # 8.5           -> a nota do primeiro aluno
print(alunos[1][0])    # 'Bruno'       -> o nome do segundo aluno
```

> ⚠️ **Erro comum:** confundir a ordem dos índices. Lembre-se: `lista[indice_da_linha][indice_da_coluna]` — primeiro "qual aluno", depois "qual dado daquele aluno".

## 1.3 Inserindo dados com `append()`

Em vez de já escrever a lista completa, muitas vezes você vai construí-la durante a execução do programa, adicionando um aluno por vez com `append()`:

```python
alunos = []  # começa vazia

alunos.append(["Ana", 8.5])
alunos.append(["Bruno", 7.0])
alunos.append(["Carlos", 9.2])

print(alunos)
```

`append()` sempre adiciona o item **no final** da lista. Note que o que estamos adicionando é, em si, uma lista (`["Ana", 8.5]`) — é isso que torna a lista "composta".

## 1.4 Capturando dados digitados pelo usuário

Na prática, os dados normalmente vêm do próprio usuário, não estão escritos diretamente no código:

```python
nome = input("Nome: ")
nota = float(input("Nota: "))

alunos.append([nome, nota])
```

> 💡 **Atenção ao tipo de dado:** `input()` sempre retorna texto (`str`). Por isso convertemos a nota com `float()` — caso contrário, "8.5" seria tratado como texto e não poderíamos fazer cálculos com ela (como tirar uma média, por exemplo).

## 1.5 Atualizando e removendo dados

Como cada aluno é uma lista dentro da lista principal, podemos alterar um valor específico acessando-o pelos índices:

```python
# Atualizando a nota de Bruno (índice 1 = segundo aluno, índice 1 = segundo dado, a nota)
alunos[1][1] = 8.0

# Removendo Carlos (precisa passar a lista EXATAMENTE como ela está armazenada)
alunos.remove(["Carlos", 9.2])

print(alunos)
```

> ⚠️ **Cuidado com `remove()`:** ele procura por uma correspondência **exata**. Se a nota de Carlos já tivesse sido alterada para outro valor, `alunos.remove(["Carlos", 9.2])` não encontraria nada e geraria um erro, pois esse valor não existiria mais na lista.

## 1.6 Percorrendo uma lista composta

Para exibir ou processar todos os registros, usamos um laço `for`:

```python
for aluno in alunos:
    print(f"Nome: {aluno[0]}")
    print(f"Nota: {aluno[1]}")
    print("-" * 20)
```

**O que está acontecendo aqui, passo a passo:**

1. O `for` pega o **primeiro elemento** da lista `alunos` — que é a lista `["Ana", 8.5]` — e guarda na variável `aluno`.
2. Dentro do laço, `aluno[0]` é o nome e `aluno[1]` é a nota **daquele aluno específico**.
3. Ao terminar o bloco, o `for` avança para o próximo elemento (`["Bruno", 7.0]`) e repete o processo.
4. Isso continua até percorrer todos os elementos da lista.

### Exercício rápido 🧠

Antes de seguir, tente prever a saída deste código (depois confira executando):

```python
turmas = [
    ["Matemática", 30],
    ["História", 25]
]

for turma in turmas:
    print(f"{turma[0]} tem {turma[1]} alunos")
```

<details>
<summary>Ver resposta</summary>

```
Matemática tem 30 alunos
História tem 25 alunos
```
</details>

---

# Parte 2 – Manipulação de Arquivos TXT

## 2.1 Por que precisamos disso?

Tudo que vimos até aqui vive **na memória RAM** do computador. Isso significa que, quando o programa termina (ou o computador é reiniciado), a lista `alunos` desaparece para sempre.

Para que os dados **persistam** — ou seja, continuem existindo mesmo depois que o programa for fechado — precisamos salvá-los em algum lugar permanente: um **arquivo em disco**.

## 2.2 A forma recomendada: `with open()`

```python
with open("arquivo.txt", "modo") as arquivo:
    # operações
```

Por que usar `with` em vez de simplesmente `open()`? Porque o `with` garante que o arquivo será **fechado automaticamente** ao final do bloco, mesmo que ocorra um erro no meio do caminho. Sem isso, seria fácil esquecer de fechar o arquivo manualmente, o que pode causar perda de dados ou travamentos.

> 💡 **Analogia:** pense no `with` como pedir um livro emprestado em uma biblioteca com devolução automática — você usa o livro dentro do prazo (o bloco de código) e ele é devolvido sozinho ao final, sem você precisar lembrar.

## 2.3 Os modos de abertura

| Modo | Função |
|------|--------|
| `"r"` | **Leitura** — abre um arquivo já existente para ler seu conteúdo |
| `"w"` | **Escrita** — cria o arquivo (ou apaga todo o conteúdo anterior) e grava novos dados |
| `"a"` | **Acréscimo** (*append*) — mantém o conteúdo existente e adiciona novas informações ao final |

> ⚠️ **O erro mais comum de quem está aprendendo:** usar `"w"` pensando que vai apenas "adicionar" uma linha, e acabar apagando todo o arquivo sem querer. Sempre que a intenção for **manter** o que já existe, use `"a"`.

## 2.4 Lendo arquivos

### Lendo tudo de uma vez

```python
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
```

`arquivo.read()` traz o conteúdo inteiro do arquivo como uma única string.

### Lendo linha por linha

```python
with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

Aqui, o próprio arquivo pode ser percorrido com `for`, entregando uma linha por vez. Usamos `.strip()` para remover o caractere de quebra de linha (`\n`) que vem junto de cada linha lida — sem isso, sobraria uma linha em branco extra ao imprimir.

## 2.5 Escrevendo e adicionando dados

### Criando ou sobrescrevendo um arquivo (`w`)

```python
with open("dados.txt", "w") as arquivo:
    arquivo.write("Ana\n")
    arquivo.write("Bruno\n")
```

Note o `\n` no final de cada `write()` — ele é o responsável por criar a quebra de linha. Se você esquecer, "Ana" e "Bruno" ficariam colados na mesma linha: `AnaBruno`.

### Adicionando informações ao final do arquivo (`a`)

```python
with open("dados.txt", "a") as arquivo:
    arquivo.write("Carlos\n")
```

Como o modo é `"a"`, "Carlos" é adicionado **depois** de "Ana" e "Bruno", sem apagar o que já estava lá.

## 2.6 Alterando uma linha específica

E se quisermos modificar apenas uma linha no meio do arquivo, sem reescrever tudo manualmente? A estratégia é: **ler tudo para a memória, modificar na memória, e então reescrever o arquivo inteiro**.

```python
with open("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()

for i in range(len(linhas)):
    if linhas[i].strip() == "Bruno":
        linhas[i] = "Bruno Silva\n"

with open("dados.txt", "w") as arquivo:
    arquivo.writelines(linhas)
```

**Passo a passo:**

1. `readlines()` lê o arquivo inteiro e devolve **uma lista**, onde cada item é uma linha do arquivo (ainda com o `\n` no final).
2. O `for` percorre essa lista usando índices (`i`), procurando a linha que, sem o `\n` (por isso o `.strip()`), seja igual a "Bruno".
3. Quando encontra, substitui aquele item da lista por "Bruno Silva\n".
4. Por fim, abrimos o arquivo no modo `"w"` (que apaga o conteúdo anterior) e gravamos a lista atualizada inteira com `writelines()`.

> 💡 **Por que não dá para simplesmente "editar uma linha" diretamente no arquivo?** Arquivos de texto não funcionam como uma planilha editável: não existe um comando que diga "vá até a linha 3 e mude". A única forma confiável é reescrever o arquivo completo com o conteúdo já corrigido.

---

# Parte 3 – Integração: Sistema de Cadastro de Alunos

Agora vamos juntar as duas partes. A ideia é simples: usamos uma **lista composta** para trabalhar com os dados durante a execução do programa, e um **arquivo de texto** para guardá-los permanentemente.

```
Cadastro dos Alunos
        ↓
Lista Composta   (dados na memória)
        ↓
Salvar em Arquivo TXT   (dados no disco, permanentes)
        ↓
Ler Arquivo TXT
        ↓
Reconstruir Lista   (dados de volta na memória)
        ↓
Utilizar Dados
```

## 3.1 Lista de alunos

```python
alunos = [
    ["Ana", 18, 8.5],
    ["Bruno", 20, 7.0],
    ["Carlos", 19, 9.2]
]
```

Agora cada aluno tem três informações: nome, idade e nota.

## 3.2 Salvando no arquivo

```python
with open("alunos.txt", "w") as arquivo:
    for nome, idade, nota in alunos:
        arquivo.write(f"{nome};{idade};{nota}\n")
```

**Ponto-chave:** `for nome, idade, nota in alunos` é uma forma direta de **desempacotar** cada sublista em três variáveis de uma vez, em vez de usar `aluno[0]`, `aluno[1]`, `aluno[2]`. Funciona porque cada sublista tem exatamente 3 elementos, na mesma ordem das variáveis.

Usamos `;` como **separador** entre os campos. Esse caractere é importante: ele vai nos permitir, depois, separar nome, idade e nota de volta ao ler o arquivo.

### Conteúdo gerado em `alunos.txt`

```txt
Ana;18;8.5
Bruno;20;7.0
Carlos;19;9.2
```

> 💡 Esse formato (valores separados por um caractere fixo) é tão comum que tem nome: é a base do formato **CSV** (*Comma-Separated Values*), só que aqui usamos `;` em vez de `,`.

## 3.3 Reconstruindo a lista na memória

Esse é o passo inverso: ler o texto do arquivo e transformá-lo de volta em uma lista composta utilizável pelo Python.

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

**Passo a passo:**

1. `linha.strip()` remove o `\n` do final da linha.
2. `.split(";")` quebra a string em pedaços, usando `;` como ponto de corte. A linha `"Ana;18;8.5"` se transforma na lista `["Ana", "18", "8.5"]`.
3. Essa lista é desempacotada diretamente em três variáveis: `nome`, `idade`, `nota`.
4. **Atenção:** tudo que vem de um arquivo de texto é sempre string! Por isso convertemos `idade` para `int()` e `nota` para `float()` antes de guardar — caso contrário, não poderíamos fazer cálculos com esses valores depois (como somar idades ou calcular médias).
5. Os três valores, já convertidos, são reunidos em uma nova sublista e adicionados a `alunosRecuperados`.

## 3.4 Exibindo os dados recuperados

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

Note que o resultado é idêntico aos dados originais — só que agora eles vieram do arquivo, não da lista escrita diretamente no código. Isso prova que o ciclo completo funcionou: **memória → arquivo → memória**.

---

# Recapitulando

| Conceito | O que faz | Comando-chave |
|----------|-----------|---------------|
| Lista composta | Guarda múltiplos registros, cada um com várias informações | `lista[i][j]`, `append()` |
| Salvar em arquivo | Transforma dados da memória em texto permanente no disco | `open(..., "w")`, `write()` |
| Ler arquivo | Traz texto do disco de volta para o programa | `open(..., "r")`, `readlines()` |
| Reconstruir lista | Converte texto em dados utilizáveis novamente | `.split(";")`, `int()`, `float()` |

---

# Conclusão

Neste material foram apresentados os conceitos fundamentais de **listas compostas** e **manipulação de arquivos em Python**, sempre buscando explicar não apenas *como* o código funciona, mas *por que* cada decisão (como usar `with`, escolher o modo certo, ou converter tipos de dados) é necessária.

Também foi demonstrada a integração entre essas técnicas por meio de um sistema de cadastro de alunos, permitindo **salvar** e **recuperar** informações de forma permanente — o ciclo completo que sustenta praticamente qualquer sistema real de armazenamento de dados.

Esses conceitos servem como base para o desenvolvimento de sistemas mais complexos e para o uso futuro de **bancos de dados**, tornando o armazenamento de informações mais eficiente e organizado.
