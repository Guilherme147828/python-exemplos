import random
alunos=['João', 'Maria', 'Ana','lucas','Lucas', 'Mariana']
print(f"Listas: {alunos}")
# Embaralhar a listas
random.shuffle(alunos)
print(f"Listas embaralhada: {alunos}")
# Ordena a Lista Crescente
alunos.sort()
print(f"Lista crescente: {alunos}")
# Ordena a Lista Decrescente
alunos.sort(reverse=True)
print(f"Listas decresente: {alunos}")