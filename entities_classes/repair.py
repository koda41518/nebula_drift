import pygame
import math
import random
import settings

class Repair:
    def __init__(self, pos):
        self.pos = pygame.Vector2(pos)

        try:
            # Charge le sprite depuis settings
            self.image = pygame.image.load(settings.ITEM_SPRITES["repair"]).convert_alpha()
        except FileNotFoundError:
            # Si le sprite est introuvable, cercle vert par défaut
            self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (60, 255, 60), (20, 20), 20)

    def draw(self, screen, offset):
        screen_pos = self.pos - offset
        offset_y = math.sin(pygame.time.get_ticks() / 300) * 3

        # Applique l’offset vertical (flottement)
        screen_pos.y += offset_y

        rect = self.image.get_rect(center=screen_pos)
        screen.blit(self.image, rect)

    @staticmethod
    def spawn_near(center_pos, min_dist=800, max_dist=1600):
        angle = random.uniform(0, 2 * math.pi)
        distance = random.randint(min_dist, max_dist)
        offset = pygame.Vector2(math.cos(angle), math.sin(angle)) * distance
        return Repair(center_pos + offset)