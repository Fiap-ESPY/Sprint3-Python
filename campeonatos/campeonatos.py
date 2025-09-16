# Lista de campeonatos criados
from jogadoras.jogadoras import Time

campeonatos = []


def gerar_chaves():
    """Gera chaves de jogos fictícias, incluindo o time do usuário."""
    return [
        "Time1 x Time2",
        "Time3 x Time4",
        "Time5 x Time6",
        f"Time7 x {Time['Nome']}"
    ]


def ver_chaves():
    """Mostra as chaves de jogos fictícias."""
    print("\n=== Chaves dos Jogos ===")
    for jogo in gerar_chaves():
        print(jogo)


def ver_campeonatos():
    """Lista todos os campeonatos cadastrados."""
    if not campeonatos:
        print("Nenhum campeonato cadastrado.")
    else:
        print("\n=== Campeonatos Existentes ===")
        for i, camp in enumerate(campeonatos, start=1):
            print(f"{i} - {camp['nome']}")


def criar_campeonato():
    """Cria um novo campeonato, verificando se o nome já existe."""
    nome = input("Digite o nome do novo campeonato: ")
    # Verifica duplicidade
    for camp in campeonatos:
        if camp["nome"] == nome:
            print("Já existe um campeonato com esse nome!")
            return
    # Adiciona o campeonato à lista
    campeonatos.append({
        "nome": nome,
        "chaves": gerar_chaves()
    })
    print(f"Campeonato '{nome}' criado com sucesso!")


def ver_chaves_campeonato():
    """Mostra as chaves de um campeonato selecionado pelo nome."""
    ver_campeonatos()
    if not campeonatos:
        return
    nome = input("Digite o nome do campeonato que deseja ver: ")
    for camp in campeonatos:
        if camp["nome"] == nome:
            print(f"\n=== Chaves do Campeonato: {nome} ===")
            for jogo in camp["chaves"]:
                print(jogo)
            return
    print("Campeonato não encontrado.")
