import pygame

class ShieldPickup:
    def __init__(self, pos):
        self.pos = pygame.Vector2(pos)
        self.radius = 20

    def draw(self, surface, offset):
        screen_pos = self.pos - offset
        pygame.draw.circle(surface, (100, 200, 255), screen_pos, self.radius)

    def check_collision(self, ship):
        return self.pos.distance_to(ship.pos) < self.radius + 20  # hitbox