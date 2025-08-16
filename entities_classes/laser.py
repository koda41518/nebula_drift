import pygame

class Laser:
    def __init__(self, pos, direction):
        self.pos = pygame.Vector2(pos)
        self.direction = direction
        self.speed = 1000
        self.life = 0
        self.lifetime = 1.5

    def update(self, dt):
        self.pos += self.direction * self.speed * dt
        self.life += dt

    def is_expired(self):
        return self.life > self.lifetime

    def draw(self, surface, offset):
        screen_pos = self.pos - offset
        pygame.draw.line(surface, (255, 80, 80), screen_pos, screen_pos + self.direction * 20, 3)

