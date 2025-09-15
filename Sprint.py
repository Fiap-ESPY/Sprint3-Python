# Dicionário com credenciais de administrador (usuário: senha)
admin = {"admin": "123"}

# Dicionário para armazenar usuários cadastrados
usuarios = {}

# Estrutura do time do usuário (nome e jogadoras)
Time = {'Nome': ''}

# Lista de campeonatos criados
campeonatos = []


def cadastrar():
    """Cadastra um novo usuário no sistema."""
    usuario = input("Novo usuário: ")
    senha = input("Nova senha: ")
    usuarios[usuario] = senha
    print("Cadastro realizado com sucesso!")


def fazer_login():
    """Realiza login de um usuário comum."""
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario in usuarios and usuarios[usuario] == senha:
        print(f"Bem-vindo, {usuario}!")
        return True
    else:
        print("Usuário ou senha incorretos!")
        return False


def login_admin():
    """Realiza login como administrador, validando usuário e senha."""
    usuario = input("Admin: ")
    senha = input("Senha: ")
    if usuario in admin and admin[usuario] == senha:
        print(f"Bem-vindo ADMIN, {usuario}!")
        return True
    else:
        print("Usuário ou senha de ADMIN incorretos!")
        return False


def adicionar_jogadoras():
    """Adiciona jogadoras ao time, até o limite de 11 jogadoras."""
    total_jogadoras = 11
    while True:
        slot = 1
        while f"jogadora_{slot}" in Time:
            slot += 1

        if slot > total_jogadoras:
            print("Todos os slots de jogadoras estão preenchidos.")
            break

        print(f"\nSlot disponível: jogadora_{slot}")
        nome = input("Digite o nome da jogadora (ou '0' para sair): ")
        if nome == '0':
            break
        posicao = input("Digite a posição da jogadora: ")

        Time[f"jogadora_{slot}"] = {"nome": nome, "posição": posicao}
        print(f"Jogadora {nome} adicionada no slot {slot}.")


def deletar_jogadoras():
    """Permite deletar uma jogadora existente do time."""
    while True:
        jogadoras_existentes = [k for k in Time if k.startswith("jogadora_")]
        if not jogadoras_existentes:
            print("Não há jogadoras para deletar.")
            break

        print("\nJogadoras atuais:")
        for key in jogadoras_existentes:
            print(f"{key}: {Time[key]['nome']} - {Time[key]['posição']}")

        escolha = input("Digite o número da jogadora que deseja deletar (ou '0' para sair): ")
        if escolha == '0':
            break

        chave_jogadora = f"jogadora_{escolha}"
        if chave_jogadora in Time:
            nome_deletado = Time[chave_jogadora]['nome']
            del Time[chave_jogadora]
            print(f"Jogadora {nome_deletado} deletada!")
        else:
            print("Jogadora inválida. Tente novamente.")


def editar_jogadoras():
    """Permite editar os dados (nome e posição) de uma jogadora já cadastrada."""
    while True:
        jogadoras_existentes = [k for k in Time if k.startswith("jogadora_")]
        if not jogadoras_existentes:
            print("Não há jogadoras para editar.")
            break

        print("\nJogadoras atuais:")
        for key in jogadoras_existentes:
            print(f"{key}: {Time[key]['nome']} - {Time[key]['posição']}")

        escolha = input("Digite o número da jogadora que deseja editar (ou '0' para sair): ")
        if escolha == '0':
            break

        chave_jogadora = f"jogadora_{escolha}"
        if chave_jogadora in Time:
            nome_novo = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
            posicao_nova = input("Digite a nova posição (ou pressione Enter para manter a atual): ")

            if nome_novo:
                Time[chave_jogadora]['nome'] = nome_novo
            if posicao_nova:
                Time[chave_jogadora]['posição'] = posicao_nova

            print(f"Jogadora {chave_jogadora} atualizada!")
        else:
            print("Jogadora inválida. Tente novamente.")


def mostrar_time():
    """Exibe o nome do time e todas as jogadoras cadastradas."""
    print("\n=== Time Atual ===")
    print(f"Time: {Time['Nome']}")
    for key in Time:
        if key.startswith("jogadora_"):
            print(f"{key}: {Time[key]['nome']} - {Time[key]['posição']}")


def gerar_chaves():
    """Gera chaves de jogos fictícias, incluindo o time do usuário."""
    return [
        "Time1 x Time2",
        "Time3 x Time4",
        "Time5 x Time6",
        f"Time7 x {Time['Nome']}"
    ]


def criar_time():
    """Cria o time do usuário, caso ainda não exista."""
    if Time['Nome'] == '':
        Time['Nome'] = input("Digite o nome do seu time: ")
        print(f"Time '{Time['Nome']}' criado com sucesso!")
    else:
        print(f"Time já existe: {Time['Nome']}")


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


# ---------------- Programa Principal ----------------
while True:
    # Menu inicial de escolha
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Entrar como Usuário")
    print("2 - Entrar como Admin")
    print("0 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        # Submenu para usuários comuns
        print("\n=== MENU DE LOGIN USUÁRIO ===")
        print("1 - Cadastrar Usuário")
        print("2 - Fazer Login")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            if fazer_login():
                criar_time()
                while True:
                    # Submenu de gerenciamento do time
                    print("\n=== MENU DO TIME ===")
                    print("1 - Ver time completo")
                    print("2 - Ver chaves (do seu time)")
                    print("0 - Sair do menu do time")
                    opcao_time = input("Escolha uma opção: ")

                    if opcao_time == "1":
                        mostrar_time()
                    elif opcao_time == "2":
                        print("\n=== Suas Chaves ===")
                        for jogo in gerar_chaves(Time['Nome']):
                            print(jogo)
                    elif opcao_time == "0":
                        break
                    else:
                        print("Opção inválida!")
        elif opcao == "0":
            continue

    elif escolha == "2":
        # Submenu do administrador
        if login_admin():
            while True:
                print("\n=== MENU ADMIN ===")
                print("1 - Ver Campeonatos")
                print("2 - Criar Campeonato")
                print("3 - Ver Chaves de um Campeonato")
                print("0 - Sair do menu admin")
                opcao_admin = input("Escolha uma opção: ")

                if opcao_admin == "1":
                    ver_campeonatos()
                elif opcao_admin == "2":
                    criar_campeonato()
                elif opcao_admin == "3":
                    ver_chaves_campeonato()
                elif opcao_admin == "0":
                    break
                else:
                    print("Opção inválida!")

    elif escolha == "0":
        # Encerra o programa
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")
