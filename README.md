# ⚽ Sistema de Gerenciamento de Times e Campeonatos

Este projeto é um sistema simples em Python para gerenciar **times, jogadoras e campeonatos fictícios**.  
Ele permite que usuários criem times com até 11 jogadoras e que administradores cadastrem campeonatos e organizem as chaves.

---

## 📌 Funcionalidades

### 👤 Usuário Comum
- **Cadastro e Login** de usuário.  
- **Criação de time** (apenas um por usuário).  
- **Gerenciamento de jogadoras**:
  - Adicionar até 11 jogadoras com nome e posição.
  - Editar jogadoras existentes.
  - Deletar jogadoras do time.
- **Exibição do time** completo.
- **Visualização de chaves de jogos fictícias** (com o time do usuário incluído).

### 🛠️ Administrador
- **Login com credenciais fixas** (`admin:123`).  
- **Gerenciamento de campeonatos**:
  - Criar campeonatos.
  - Listar campeonatos existentes.
  - Visualizar as chaves de um campeonato específico.

---

## 📂 Estrutura do Código

- `admin`: dicionário com credenciais do administrador.  
- `usuarios`: dicionário com usuários cadastrados.  
- `Time`: dicionário que armazena o nome do time e suas jogadoras.  
- `campeonatos`: lista de campeonatos criados.  

### Principais Funções
- `cadastrar()` → Cadastra um novo usuário.  
- `fazer_login()` → Login de usuário comum.  
- `login_admin()` → Login do administrador.  
- `criar_time()` → Cria o time do usuário.  
- `adicionar_jogadoras()` → Adiciona jogadoras ao time.  
- `editar_jogadoras()` → Edita jogadoras existentes.  
- `deletar_jogadoras()` → Remove jogadoras do time.  
- `mostrar_time()` → Mostra o time completo.  
- `gerar_chaves()` → Gera confrontos fictícios.  
- `criar_campeonato()` → Cria novo campeonato.  
- `ver_campeonatos()` → Lista campeonatos criados.  
- `ver_chaves_campeonato()` → Exibe chaves de um campeonato específico.  

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3.x** instalado.  
2. Salve o código em um arquivo, por exemplo: `main.py`.  
3. No terminal, execute:

```bash
python main.py
Use o menu principal para escolher entre:
Entrar como usuário.
Entrar como administrador.
Encerrar o programa.

```

---

 ##  🔑 Credenciais do Administrador
    Usuário: admin
    Senha: 123

---

##  📌 Observações
- Cada usuário pode criar apenas um time.

- O limite máximo de jogadoras por time é 11.

- Os campeonatos criados são armazenados apenas em memória (serão apagados ao encerrar o programa).

- O projeto pode ser expandido para salvar dados em arquivos ou um banco de dados.

--- 

## 👨‍💻 Autores
- Beatriz Cortez - RM561431
- Bruno Alves - RM563986
- Gabriel Augusto - RM564126
- Gustavo Moura - RM566190
- Pedro Henrique - RM563281