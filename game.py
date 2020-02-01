from player import Player

#creer une second classe qui va representer notre jeu
class Game:

    def __init__(self):
        #genere notre joueur
        self.player = Player()
        #touche actuellement active par le joueur
        #dictionnaire vide
        self.pressed = {}