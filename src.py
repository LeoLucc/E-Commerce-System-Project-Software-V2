class Usuario:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def autenticar(self, username, password):
        return self.username == username and self.password == password


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, produto):
        self.itens.append(produto)
        print(f"{produto.nome} foi adicionado ao carrinho!")

    def visualizar(self):
        if not self.itens:
            print("\nSeu carrinho está vazio!\n")
            return
        print("\n=== Carrinho de Compras ===")
        total = sum(item.preco for item in self.itens)
        for i, item in enumerate(self.itens, start=1):
            print(f"{i} - {item.nome} | R${item.preco}")
        print(f"\nTotal da compra: R${total}")

    def comprar_tudo(self):
        if self.itens:
            print("\nCompra finalizada! Você comprou:")
            for item in self.itens:
                print(f"- {item.nome} por R${item.preco}")
            self.itens.clear()
            print("\nObrigado por comprar conosco!\n")
        else:
            print("\nSeu carrinho está vazio!\n")

    def remover_item(self, index):
        if 0 <= index < len(self.itens):
            removido = self.itens.pop(index)
            print(f"{removido.nome} foi removido do carrinho.")

    def esvaziar(self):
        self.itens.clear()
        print("\nTodos os itens foram removidos do carrinho.\n")


class Loja:
    def __init__(self):
        self.produtos = [
            Produto("Notebook", 3500),
            Produto("Smartphone", 2000),
            Produto("Tênis", 300)
        ]
        self.usuarios = {
            "admin": Usuario("admin", "admin123", is_admin=True),
            "gestor": Usuario("gestor", "gestor123", is_admin=True)
        }

    def cadastrar_usuario(self, username, password):
        if username in self.usuarios:
            print("Usuário já existe!")
        else:
            self.usuarios[username] = Usuario(username, password)
            print("Usuário cadastrado com sucesso!")

    def autenticar_usuario(self, username, password):
        usuario = self.usuarios.get(username)
        if usuario and usuario.autenticar(username, password):
            return usuario
        return None

    def listar_produtos(self):
        print("\nLista de Produtos Disponíveis:")
        for i, produto in enumerate(self.produtos, start=1):
            print(f"{i} - Nome: {produto.nome}, Preço: R${produto.preco}")

    def adicionar_produto(self, nome, preco):
        self.produtos.append(Produto(nome, preco))
        print(f"Produto {nome} adicionado ao inventário!")

    def editar_produto(self, index, nome, preco):
        if 0 <= index < len(self.produtos):
            self.produtos[index] = Produto(nome, preco)
            print(f"Produto {nome} foi atualizado!")
        else:
            print("Produto não encontrado!")

    def remover_produto(self, index):
        if 0 <= index < len(self.produtos):
            removido = self.produtos.pop(index)
            print(f"Produto {removido.nome} foi removido!")


def menu_principal():
    loja = Loja()
    carrinho = Carrinho()
    usuario_atual = None

    while True:
        print("\n=== Menu ===")
        print("1 - Fazer Login")
        print("2 - Cadastrar Usuário")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            username = input("Usuário: ")
            password = input("Senha: ")
            usuario_atual = loja.autenticar_usuario(username, password)
            
            if usuario_atual:
                print("Login bem-sucedido!")
                while True:
                    print("\n=== Menu do Usuário ===")
                    print("1 - Ver Produtos")
                    print("2 - Comprar ou Adicionar ao Carrinho")
                    print("3 - Ver Carrinho")
                    if usuario_atual.is_admin:
                        print("4 - Acessar Menu de Administração")
                    print("5 - Logout")

                    opcao_usuario = input("Escolha uma opção: ")
                    if opcao_usuario == "1":
                        loja.listar_produtos()
                    elif opcao_usuario == "2":
                        loja.listar_produtos()
                        escolha = int(input("Digite o número do produto desejado: ")) - 1
                        if 0 <= escolha < len(loja.produtos):
                            print("1 - Adicionar ao carrinho")
                            print("2 - Comprar agora")
                            acao = input("Escolha uma opção: ")
                            if acao == "1":
                                carrinho.adicionar(loja.produtos[escolha])
                            elif acao == "2":
                                print(f"\nVocê comprou: {loja.produtos[escolha].nome} por R${loja.produtos[escolha].preco}!")
                        else:
                            print("Opção inválida!")
                    elif opcao_usuario == "3":
                        carrinho.visualizar()
                    elif opcao_usuario == "4" and usuario_atual.is_admin:
                        print("\n=== Menu de Administração ===")
                        print("1 - Adicionar Produto")
                        print("2 - Editar Produto")
                        print("3 - Remover Produto")
                        print("4 - Voltar")
                        opcao_admin = input("Escolha uma opção: ")
                        if opcao_admin == "1":
                            nome = input("Nome do Produto: ")
                            preco = float(input("Preço: R$"))
                            loja.adicionar_produto(nome, preco)
                        elif opcao_admin == "2":
                            loja.listar_produtos()
                            index = int(input("Número do Produto: ")) - 1
                            nome = input("Novo Nome: ")
                            preco = float(input("Novo Preço: R$"))
                            loja.editar_produto(index, nome, preco)
                        elif opcao_admin == "3":
                            loja.listar_produtos()
                            index = int(input("Número do Produto: ")) - 1
                            loja.remover_produto(index)
                        elif opcao_admin == "4":
                            continue
                    elif opcao_usuario == "5":
                        print("Você saiu da conta.")
                        usuario_atual = None
                        break
                    else:
                        print("Opção inválida!")
            else:
                print("Usuário ou senha incorretos!")
        elif opcao == "2":
            username = input("Usuário: ")
            password = input("Senha: ")
            loja.cadastrar_usuario(username, password)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu_principal()
