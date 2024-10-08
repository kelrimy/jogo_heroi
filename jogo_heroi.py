class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        elif self.tipo == "arqueiro":
            ataque = "usou arco e flecha" 
        elif self.tipo == "bárbaro":
            ataque = "usou força bruta"
        else:
            ataque = "não possui ataque definido"

        print(f"O {self.tipo} atacou usando {ataque}.")


