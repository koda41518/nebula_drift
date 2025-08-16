import pygame
import math
import random

class Repair:
    def __init__(self, pos):
        self.pos = pygame.Vector2(pos)

    def draw(self, screen, offset):
        screen_pos = self.pos - offset
        offset_y = math.sin(pygame.time.get_ticks() / 300) * 3
        pygame.draw.circle(screen, (50, 255, 50), (int(screen_pos.x), int(screen_pos.y + offset_y)), 10)
    @staticmethod
    def spawn_near(center_pos, min_dist=800, max_dist=1600):
        angle = random.uniform(0, 2 * math.pi)
        distance = random.randint(min_dist, max_dist)
        offset = pygame.Vector2(math.cos(angle), math.sin(angle)) * distance
        return Repair(center_pos + offset)