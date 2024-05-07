print(f"Programa de empréstimo\n"
      f"Responda: (0-não ou 1-sim)")
nome_negativado=int(input('Possui nome negativado?:'))
if nome_negativado ==1:
    print('não pode realizar empréstimo')
else:
    carteira_assinada=(input('Possui carteira assinada?'))
    if carteira_assinada == 0:
        print('não pode realizar empréstimo')
    else:
     casa_propria=int(input('Possui casa pópria?:'))
    if casa_propria ==0:
       print('não pode realizar empréstimo')
    else:
       print('conceder empréstimo')    