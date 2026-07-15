def buscarAluno(array, nome):
    nota = array[nome]
    return nota

alunos = {'Ana': 8.5, 'Bruno':5.2, 'Carlos':7.9}
nome = input("Digite o nome do aluno que deseja encontrar: ")

try:
    nota = buscarAluno(alunos, nome)
except KeyError:
    print('Erro: Aluno não encontrado')
else:
    print(f"Nota do(a) {nome}:{nota}")
finally:
    print("Busca encerrada")