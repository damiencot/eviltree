import pygame

from game import Game

pygame.init()


#genere la fenetre de notre jeux
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

#arriere plan
background = pygame.image.load('assets/bg.jpg')


#charger notre jeux
game = Game()

running = True

#boucle tant que cette condition est vraie
while running:

    #appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    #recupere le projectiles du joueurs
    for projectile in game.player.all_projectile:
        projectile.move()

    #appliquer l'image de mon joueur et sa position
    screen.blit(game.player.image, game.player.rect)

    #applique l'ensemble des images de mon groupe de projectiles
    game.player.all_projectile.draw(screen)

    #verifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()



    #mettre a jour l'ecran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    # pygame.event.get() nous retourne une liste d'event
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("FERME")
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            #si la touche espace est enclenché pour lance notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

            # #quelle touche a ete utilisé
            # if event.key == pygame.K_RIGHT:
            #     game.player.move_right()
            # elif event.key == pygame.K_LEFT:
            #     game.player.move_left()
