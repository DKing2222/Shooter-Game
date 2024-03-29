import pygame
from comet import Comet

class CometFallEvent:

    def __init__(self,game) -> None:
        self.game = game
        self.percent = 0
        self.percent_speed = 30

        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed/100

    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # Apparaitre une premiere boule de feu
        self.all_comets.add(Comet(self))
        self.all_comets.add(Comet(self))
        self.all_comets.add(Comet(self))


    def attempt_fall(self):
        if self.is_full_loaded():
            print("Pluit de Cometes")
            self.meteor_fall()
            self.reset_percent()

    def update_bar(self, surface):
        self.add_percent()

        # Essayer de declencher la pluie
        self.attempt_fall()

        # barre noir (en arriere plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0,# l'axe des x
            surface.get_height()-10, # l'axe des y
            surface.get_width(),# Longueur de la fenetre
            10 #epaisseur de la barre
        ])

        # barre rouge (en jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,# l'axe des x
            surface.get_height()-10, # l'axe des y
            (surface.get_width() / 100) * self.percent,# Longueur de la fenetre
            10 #epaisseur de la barre
        ])