# Lista de alunos
alunos = [
    ["Ana", 18, 8.5],
    ["Bruno", 20, 7.0],
    ["Carlos", 19, 9.2]
]

# Salvar os dados no arquivo
with open("alunos.txt", "w") as arquivo:
    for nome, idade, nota in alunos:
        arquivo.write(f"{nome};{idade};{nota}\n")

print("Dados salvos com sucesso!")

# Reconstruir a lista a partir do arquivo
alunosRecuperados = []

with open("alunos.txt", "r") as arquivo:
    for linha in arquivo:
        nome, idade, nota = linha.strip().split(";")

        alunosRecuperados.append([
            nome,
            int(idade),
            float(nota)
        ])

print("\nLista recuperada do arquivo:")
for nome, idade, nota in alunosRecuperados:
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota}")
    print("-" * 20)
