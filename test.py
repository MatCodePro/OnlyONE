from classes import *

player = [PLAYER("Mati"), PLAYER("Jugador 2"), PLAYER("Jugador 3"), PLAYER("Jugador 4")]
for i in player:
    print(i.order)

""" # La función new_deck construye el mazo de cartas y lo entrega como recién salido de la caja
def new_deck():
    newDeck = []
    colours = ["Rojo", "Verde", "Amarillo", "Azul"]
    values = [0,1,2,3,4,5,6,7,8,9,"+2","Saltear","Giro"]
    wilds = ["Comodín","+4"]
    for colour in colours:
        for value in values:
            cardVal = f"{value} {colour}"
            newDeck.append(cardVal)
            if value != 0:
                newDeck.append(cardVal)
    for i in range(4):
        newDeck.append(wilds[0])
        newDeck.append(wilds[1])
    return newDeck

# La función shuffle recibe como parámetro el mazo, lo mezcla y entrega las cartas mezcladas
def shuffle(cards):
    random.shuffle(cards)
    return (cards) """
