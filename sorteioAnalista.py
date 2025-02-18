# variável que armazena os dias
votos_segunda = 0
votos_terca = 0
votos_quarta = 0
votos_quinta = 0
votos_sexta = 0

# coleta de votos
colaboradores = int(input("Informe a quantidade colaboradores: "))
for i in range(colaboradores):
    dia_semana = input("Qual o melhor dia da semana para realizar as lives ? (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ")

    while dia_semana not in ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira']:
        print("Dia inválido, tente novamente.")
        dia_semana = input("Qual o melhor dia da semana para realizar as lives? (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira ): ")

    if dia_semana == 'segunda-feira':
        votos_segunda += 1
    elif dia_semana == 'terça-feira':
        votos_terca += 1
    elif dia_semana == 'quarta-feira':
        votos_quarta += 1
    elif dia_semana == 'quinta-feira':
        votos_quinta += 1
    else:
        votos_sexta += 1

# soma dos votos
total_votos = votos_segunda

if votos_terca > total_votos:
    total_votos = votos_terca
if votos_quarta > total_votos:
    total_votos = votos_quarta
if votos_quinta > total_votos:
    total_votos = votos_quinta
if votos_sexta > total_votos:
    total_votos = votos_sexta

# validação do empate
empate = 0
if votos_segunda == total_votos:
    empate += 1
if votos_terca == total_votos:
    empate += 1
if votos_quarta == total_votos:
    empate += 1
if votos_quinta == total_votos:
    empate += 1
if votos_sexta == total_votos:
    empate += 1

if empate > 1:
    print("Houve um empate entre os dias.")
else:
    if total_votos == votos_segunda:
        print("O dia escolhido para as lives é: segunda-feira")
    elif total_votos == votos_terca:
        print("O dia escolhido para as lives é: terça-feira")
    elif total_votos == votos_quarta:
        print("O dia escolhido para as lives é: quarta-feira")
    elif total_votos == votos_quinta:
        print("O dia escolhido para as lives é: quinta-feira")
    elif total_votos == votos_sexta:
        print("O dia escolhido para as lives é: sexta-feira")
