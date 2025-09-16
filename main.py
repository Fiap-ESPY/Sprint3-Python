# --- Imports do seu projeto ---
from campeonatos.campeonatos import (
    ver_chaves,
    ver_campeonatos,
    criar_campeonato,
    ver_chaves_campeonato,
)
from jogadoras.jogadoras import (
    editar_jogadoras,
    deletar_jogadoras,
    adicionar_jogadoras,
    criar_time, Time,
)
from login.login import login_admin, cadastrar, fazer_login


# ------------------ Helpers simples ------------------
def pedir_opcao(msg, opcoes_validas):
    """Pede uma opção até vir uma válida (tudo em string)."""
    while True:
        opc = input(msg).strip()
        if opc in opcoes_validas:
            return opc
        print("Opção inválida! Tente novamente.")


def mostrar_time():
    print("\n=== Time Atual ===")
    print(f"Time: {Time.get('Nome', '')}")
    for k, v in Time.items():
        if k.startswith("jogadora_") and isinstance(v, dict):
            print(f"{k}: {v.get('nome', '-')} - {v.get('posição', '-')}")


# ------------------ Menus ------------------
def menu_time():
    while True:
        print("\n=== MENU DO TIME ===")
        print("1 - Adicionar jogadoras")
        print("2 - Deletar jogadoras")
        print("3 - Editar jogadoras")
        print("4 - Ver time completo")
        print("5 - Ver chaves")
        print("0 - Voltar")
        opc = pedir_opcao("Escolha uma opção: ", {"1", "2", "3", "4", "5", "0"})

        if opc == "1":
            adicionar_jogadoras()
        elif opc == "2":
            deletar_jogadoras()
        elif opc == "3":
            editar_jogadoras()
        elif opc == "4":
            mostrar_time()
        elif opc == "5":
            ver_chaves()
        else:  # "0"
            return


def menu_usuario():
    print("\n=== MENU DE LOGIN USUÁRIO ===")
    print("1 - Cadastrar Usuário")
    print("2 - Fazer Login")
    print("0 - Voltar")
    opc = pedir_opcao("Escolha uma opção: ", {"1", "2", "0"})

    if opc == "1":
        cadastrar()
    elif opc == "2":
        if fazer_login():
            criar_time()  # sua função; pode preencher Time["Nome"] etc.
            menu_time()
    # "0" só volta


def menu_admin():
    if not login_admin():
        return

    while True:
        print("\n=== MENU ADMIN ===")
        print("1 - Ver Campeonatos")
        print("2 - Criar Campeonato")
        print("3 - Ver Chaves de um Campeonato")
        print("0 - Voltar")
        opc = pedir_opcao("Escolha uma opção: ", {"1", "2", "3", "0"})

        if opc == "1":
            ver_campeonatos()
        elif opc == "2":
            criar_campeonato()
        elif opc == "3":
            ver_chaves_campeonato()
        else:  # "0"
            return


# ------------------ Programa principal ------------------
def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Entrar como Usuário")
        print("2 - Entrar como Admin")
        print("0 - Sair")
        opc = pedir_opcao("Escolha uma opção: ", {"1", "2", "0"})

        if opc == "1":
            menu_usuario()
        elif opc == "2":
            menu_admin()
        else:
            print("Encerrando o programa...")
            break


if __name__ == "__main__":
    main()