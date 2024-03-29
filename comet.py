import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self,comet_event):
        super().__init__()
        self.comet_event = comet_event
        # Definir l'image associee a cette comette
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(80,1000)
        self.rect.y = - random.randint(150,300)
        self.velocity = random.randint(1,3)
        self.temps = 0

    def remove(self) -> None:
        self.comet_event.all_comets.remove(self)

    def fall(self):
        self.temps += 1
        temps = self.temps/1000
        self.rect.y = self.rect.y + 5*self.velocity*temps*temps

        if self.rect.y >=500:
            self.remove()

        if self.comet_event.game.check_collision(
            self, 
            self.comet_event.game.all_players
            ):
            self.remove()
            self.comet_event.game.player.damage(20)

