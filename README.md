# ⚽ Sistema de Gerenciamento de Times e Campeonatos

Projeto em **Python** para gerenciar **times, jogadoras e campeonatos fictícios**.  
Ele simula menus de **usuários** e **administradores**, permitindo criar times, cadastrar jogadoras e organizar campeonatos.

---

## 📌 Funcionalidades

### 👤 Usuário
- Cadastrar conta.  
- Fazer login.  
- Criar **um time** por usuário.  
- Gerenciar jogadoras:  
  - Adicionar até **11 jogadoras** (nome e posição).  
  - Editar ou remover jogadoras existentes.  
- Visualizar o **time completo**.  
- Ver as **chaves de campeonatos** fictícias.

### 🛠️ Administrador
- Login com credenciais fixas (`admin / 123`).  
- Criar campeonatos.  
- Listar campeonatos já criados.  
- Ver as chaves de um campeonato específico.

---

## 📂 Estrutura do Código

O sistema foi dividido em **módulos simples** para facilitar a leitura:

- `login/` → Funções de cadastro e login (`cadastrar`, `fazer_login`, `login_admin`).  
- `jogadoras/` → Funções de gerenciamento do time (`criar_time`, `adicionar_jogadoras`, `editar_jogadoras`, `deletar_jogadoras`).  
- `campeonatos/` → Funções para criar e visualizar campeonatos (`criar_campeonato`, `ver_campeonatos`, `ver_chaves`, `ver_chaves_campeonato`).  
- `main.py` → Ponto de entrada do programa com os **menus principais**.

### Principais Funções do `main.py`
- `main()` → Inicia o programa exibindo o menu principal.  
- `menu_usuario()` → Fluxo para usuários comuns.  
- `menu_time()` → Opções para gerenciar o time.  
- `menu_admin()` → Opções para administradores.  
- `mostrar_time()` → Exibe o time e suas jogadoras.  
- `pedir_opcao()` → Valida a entrada de menus (ajuda a evitar erros de digitação).  

---

## 🚀 Como Executar

1. Instale o **Python 3.x**.  
2. Clone este repositório ou baixe os arquivos.  
3. No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

Você verá o **menu principal** com três opções:  
1. Entrar como usuário.  
2. Entrar como administrador.  
0. Sair.  

---

## 🔑 Credenciais do Administrador

```text
Usuário: admin
Senha: 123
```

---

## 📌 Observações Importantes
- Cada usuário só pode ter **um time**.  
- Máximo de **11 jogadoras** por time.  
- Dados (usuários, times e campeonatos) são **armazenados apenas em memória**.  
  - Ou seja, ao encerrar o programa, tudo é perdido.  
- Futuramente, pode ser expandido para **arquivos** ou **banco de dados**.

---

## 👨‍💻 Autores
- Beatriz Cortez - RM561431  
- Bruno Alves - RM563986  
- Gabriel Augusto - RM564126  
- Gustavo Moura - RM566190  
- Pedro Henrique - RM563281  