import re

class CadastroSystem:
    def __init__(self):
        self.usuarios = []

    def validar_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def cadastrar_usuario(self, nome, email, senha):
        if not nome or not email or not senha:
            raise ValueError("Nome, email e senha são obrigatórios.")

        if not self.validar_email(email):
            raise ValueError("Email inválido.")

        usuario = {
            'nome': nome,
            'email': email,
            'senha': senha
        }

        self.usuarios.append(usuario)
        return usuario