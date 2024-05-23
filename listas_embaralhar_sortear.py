import random 
alunos=['João', 'Maria', 'Ana','lucas','Lucas', 'Mariana']
print(f"Listas: {alunos}")
# Embaralhar a Lista
random.shuffle(alunos)
print(f"Lista embaralhada: {alunos}")
# Escolhe um aluno aleatoriamente
aluno_sorteado = random.choice(alunos)
print(f"Aluno sorteado: {aluno_sorteado}")
