# E-Commerce-System-Project-Software-V2

## Visão Geral

Este projeto é um sistema de e-commerce desenvolvido em Python utilizando Programação Orientada a Objetos (POO) e modularização. O sistema permite que usuários autentiquem-se, adicionem produtos ao carrinho e façam compras. Além disso, há um painel administrativo para gerenciamento de produtos.

Classes Implementadas e implementações futuras

1. Usuário

Classe responsável por representar um usuário do sistema.

Atributos:

nome (str): Nome do usuário.

email (str): Endereço de e-mail do usuário. (futura)

senha (str): Senha do usuário.

tipo (str): Define se o usuário é "cliente" ou "admin".

Métodos:

autenticar(username: str, password: str) -> bool: Verifica se o nome de usuário e a senha fornecidos correspondem aos armazenados. 

2. Produto

Classe que representa um produto disponível para compra no e-commerce.

Atributos:

id_produto (int): Identificador único do produto. (futura)

nome (str): Nome do produto.

preco (float): Preço do produto.

quantidade (int): Quantidade disponível no estoque. (futura)

Métodos:

atualizar_estoque(quantidade: int): Atualiza a quantidade disponível do produto. (futura)

exibir_info() -> str: Retorna uma string formatada com as informações do produto. (futura)

3. Carrinho

Classe que representa o carrinho de compras de um usuário.

Atributos:

itens (dict): Dicionário que armazena os produtos e suas respectivas quantidades.

Métodos:

adicionar_produto(produto: Produto, quantidade: int): Adiciona um produto ao carrinho.

remover_produto(produto: Produto): Remove um produto do carrinho.

calcular_total() -> float: Retorna o valor total da compra.

exibir_carrinho() -> str: Retorna uma string com os produtos e preços no carrinho.

4. Admin (futura)

Classe específica para administração do sistema.

Atributos:

usuario (Usuário): Instância do usuário com permissão de administrador.

produtos (list): Lista de produtos disponíveis no sistema.

Métodos:

adicionar_produto(produto: Produto): Adiciona um novo produto ao sistema.

remover_produto(id_produto: int): Remove um produto do sistema pelo seu ID.

listar_produtos() -> str: Lista todos os produtos disponíveis no sistema.

## Como Usar

### Autenticação

Os usuários devem autenticar-se com email e senha para acessar funcionalidades específicas.

### Adicionar Produtos ao Carrinho

Após a autenticação, os clientes podem adicionar produtos ao carrinho e visualizar o total da compra.

### Painel Administrativo

Usuários com permissão de administrador podem adicionar e remover produtos do sistema.

