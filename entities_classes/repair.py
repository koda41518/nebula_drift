import pygame

class Repair:
    def __init__(self, pos):
        self.pos = pygame.Vector2(pos)

    def draw(self, surface, offset):
        screen_pos = self.pos - offset
        pygame.draw.circle(surface, (50, 255, 50), (int(screen_pos.x), int(screen_pos.y)), 10)

    def is_colliding(self, pos, radius):
        return self.pos.distance_to(pos) < radius
