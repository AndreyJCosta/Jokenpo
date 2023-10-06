print("   \\\\\\\\\\\\JOKENPÔ//////")

print(" Se prepare pro vale tudo!")
print()
jogador1=input("Digite o nome do primeiro jogador: ")
jogador2=input("Digite o nome do segundo jogador: ")
print()
print(f"Bem vindos {jogador1} e {jogador2}, preparados para começar a partida?")
print()
while True:
    resp_jogador1=input(f"{jogador1} Escolha Pedra, Papel ou Tesoura ? ")
    resp_jogador2=input(f"{jogador2} Escolha Pedra, Papel ou Tesoura ? ")
    while resp_jogador1 == resp_jogador2:
        print(f" {resp_jogador1} X {resp_jogador2} deu empate tente novamente!")
        resp_jogador1 = input(f"{jogador1} Escolha novamente Pedra, Papel ou Tesoura ? ")
        resp_jogador2 = input(f"{jogador2} Escolha novamente Pedra, Papel ou Tesoura ? ")
    if resp_jogador1=="pedra" and resp_jogador2=="papel":
        print(f"{resp_jogador1}X{resp_jogador2}, {resp_jogador2} enrola a {resp_jogador1} então {jogador2} VENCEEEU a partida!")
    elif resp_jogador1=="pedra" and resp_jogador2=="tesoura":
        print(f"{resp_jogador1}X{resp_jogador2}, {resp_jogador1} quebra a {resp_jogador2} então {jogador1} VENCEEEU a partida!")
    elif resp_jogador1 == "papel" and resp_jogador2 == "pedra":
        print(f"{resp_jogador1}X{resp_jogador2}, {resp_jogador1} enrola a {resp_jogador2} então {jogador1} VENCEEEU a partida!")
    elif resp_jogador1 == "papel" and resp_jogador2 == "tesoura":
        print(f"{resp_jogador1}X{resp_jogador2}, {resp_jogador2} corta o {resp_jogador1} então {jogador2} VENCEEEU a partida!")
    elif resp_jogador1 == "tesoura" and resp_jogador2 == "pedra":
        print(f"{resp_jogador1}X{resp_jogador2}, {resp_jogador2} quebra a {resp_jogador1} então {jogador2} VENCEEEU a partida!")
    elif resp_jogador1 == "tesoura" and resp_jogador2 == "papel":
        print(f"{resp_jogador1}X{resp_jogador2}, {resp_jogador1} corta o {resp_jogador2} então {jogador1} VENCEEEU a partida!")
    print()
    continuar = input("Você deseja continuar s/n ? ")
    print()
    if continuar in 'Nn':
        break
print("Foi otima a partida, te aguardo na próxima!!!!!!")



