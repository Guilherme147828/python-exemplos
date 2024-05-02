#formatação de Strings
from datetime import datetime
ano_atual = datetime.now().year
clube = 'Karasuno'
ano_fundacao = 2014
campeonato_mundial = 3
print(f"{clube}) possui {campeonato_mundial} títulos mundiais.")
print(f"São {ano_atual - ano_fundacao} anos de exeistência.")