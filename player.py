import pygame
from projectile import Projectile

#creer une premiere classe qui va representer notre joueur
#Un sprite, element visible de notre jeux
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        #vitesse
        self.velocity = 5
        #Les projectile du joueur sont rangé dans ce Group()
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        #Coordonnées (deplacement)
        self.rect = self.image.get_rect()

        self.rect.x = 400
        self.rect.y = 500

    def launch_projectile(self):
        #créer une nouvelle instance de la classe projectile
        self.all_projectile.add(Projectile(self))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

