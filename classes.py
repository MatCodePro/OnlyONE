class PLAYER:
    playersList = []
    order = 0
    def _dec_incr_order(init):
        def wrapper(cls, *args, **kwargs):
            result = init(cls, *args, **kwargs)
            cls.next_order()
            return result
        return wrapper
    @classmethod
    def next_order(cls):
        cls.order += 1
    @_dec_incr_order
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.order = PLAYER.order
        PLAYER.playersList.append(self.name)
    def __str__(self) -> str:
        return f"{self.name}"
    def say_uno (self):
        print(f"{self.name} ha cantado UNO")
    def play (self, card):
        pass
    def passing (self):
        pass
    def challenge (self, defiant, player):
        print(f"{defiant} ha desafiado a {player}")