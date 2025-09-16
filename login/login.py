# Dicionário com credenciais de administrador (usuário: senha)
admin = {"admin": "123"}

usuarios = {}


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
