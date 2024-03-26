import pygame
from game import Game
pygame.init() 

pygame.display.set_caption("Shooter")
screen = pygame.display.set_mode((1080,720))

backround = pygame.image.load("assets/bg.jpg")

running = True

game = Game()

while running:
    screen.blit(backround, (0,-200))
    screen.blit(game.player.image, game.player.rect)
    game.player.update_health_bar(screen)

    for projectile in game.player.all_projectiles:
        projectile.move()
    game.player.all_projectiles.draw(screen)

    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)
    game.all_monsters.draw(screen)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width <= screen.get_width( ):
        game.player.move_right()

    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x >= 0:
        game.player.move_left()

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()
            print("Fermeture du jeu")

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False