# Estrutura do time do usuário (nome e jogadoras)
Time = {'Nome': ''}


def mostrar_time():
    """Exibe o nome do time e todas as jogadoras cadastradas."""
    print("\n=== Time Atual ===")
    print(f"Time: {Time['Nome']}")
    for key in Time:
        if key.startswith("jogadora_"):
            print(f"{key}: {Time[key]['nome']} - {Time[key]['posição']}")


def criar_time():
    """Cria o time do usuário, caso ainda não exista."""
    if Time['Nome'] == '':
        Time['Nome'] = input("Digite o nome do seu time: ")
        print(f"Time '{Time['Nome']}' criado com sucesso!")
    else:
        print(f"Time já existe: {Time['Nome']}")


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
