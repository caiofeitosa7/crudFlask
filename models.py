class Jogo:
    def __init__(self, nome: str, categoria: str, console: str, id = None):
        self.nome = nome
        self.categoria = categoria
        self.console = console
        self.id = id


class Usuario:
    def __init__(self, id_user: str, nome: str, senha: str):
        self.id = id_user
        self.nome = nome
        self.senha = senha