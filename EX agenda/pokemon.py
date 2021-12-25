class Pokemon:
    def __init__(self, tipo, especie, level=1, nome=None):
        self.tipo = tipo
        self.especie = especie
        self.level = level

        if nome :
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return "{} ({})".format(self.especie, self.tipo)

    def atacar(self):
        print("O pokemon atacou")


meu_pokemon = Pokemon("Fogo", "charmander", nome="Jose")

print(meu_pokemon)