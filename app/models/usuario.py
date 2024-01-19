import json


class Usuario:
    def __init__(self, nome, email, senha, username):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.username = username

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "username": self.username,
        }


class Aluno(Usuario):
    def __init__(self, nome, email, senha, username, matricula):
        super().__init__(nome, email, senha, username)
        self.matricula = matricula

    def to_dict(self):
        user_dict = super().to_dict()
        user_dict["matricula"] = self.matricula
        return user_dict


class Professor(Usuario):
    def __init__(self, nome, email, senha, username, disciplina):
        super().__init__(nome, email, senha, username)
        self.disciplina = disciplina

    def to_dict(self):
        user_dict = super().to_dict()
        user_dict["disciplina"] = self.disciplina
        return user_dict
