import pygame
import random
import math
import os
import settings

class ShieldPickup:
    def __init__(self, pos):
        self.pos = pygame.Vector2(pos)
        try:
            # On essaie de charger le sprite
            self.image = pygame.image.load(settings.ITEM_SPRITES["shield_pickup"]).convert_alpha()
        except FileNotFoundError:
            # Sinon on crée un cercle bleu
            self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (100, 200, 255), (20, 20), 20)

    def draw(self, screen, offset):
        screen_pos = self.pos - offset
        screen.blit(self.image, self.image.get_rect(center=screen_pos))

    @staticmethod
    def spawn_near(ship_pos):
        angle = random.uniform(0, 2 * math.pi)
        distance = random.randint(600, 1200)
        offset = pygame.Vector2(math.cos(angle), math.sin(angle)) * distance
        return ShieldPickup(ship_pos + offset)
    