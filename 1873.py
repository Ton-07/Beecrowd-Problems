def pedra_papel_tesoura_lagarto_spock(c, escolhas):
    regras = {
        "tesoura": ["papel", "lagarto"],
        "papel": ["pedra", "spock"],
        "pedra": ["lagarto", "tesoura"],
        "lagarto": ["spock", "papel"],
        "spock": ["tesoura", "pedra"]
    }
    resultados = []
    for i in range(c):
        rajesh, sheldon = escolhas[i]
        if rajesh == sheldon:
            resultados.append('empate')
        elif sheldon in regras[rajesh]:
            resultados.append('rajesh')
        else:
            resultados.append("sheldon")
    return resultados

caso_testes = int(input())
jogos = []
for _ in range(caso_testes):
    jogo = input().split()
    jogos.append(jogo)
resultados = pedra_papel_tesoura_lagarto_spock(caso_testes, jogos)

for resultado in resultados:
    print(resultado)
