import pygame

class Enemy:
    def __init__(self, pos, speed):
        self.pos = pygame.Vector2(pos)
        self.speed = speed

    def update(self, target_pos):
        direction = (target_pos - self.pos).normalize()
        self.pos += direction * self.speed

    def draw(self, surface, offset):
        screen_pos = self.pos - offset
        pygame.draw.circle(surface, (255, 50, 50), (int(screen_pos.x), int(screen_pos.y)), 12)

    def is_colliding(self, pos, radius):
        return self.pos.distance_to(pos) < radius

