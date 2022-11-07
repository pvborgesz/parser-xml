class Player:
    def __init__(self, name, itens):
        self.name = name
        self.itens = itens

    def __str__(self):
        return print(f"Player: {self.name} - Itens: {self.itens}")