import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health -amount > amount:
            self.health -= amount 
        else:
            self.game.game_over()

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        back_bar_color = (60, 63, 60)
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 7]
        back_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 7]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_projectile (self):
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)

    def move_right(self):
        if not self.game.check_collision (self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
