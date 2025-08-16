import pygame
from settings import WIDTH, HEIGHT, DAMAGE_FLASH_DURATION

class DamageFlash:
    def __init__(self, duration=0.3):
        self.duration = duration
        self.timer = 0

    def trigger(self):
        self.timer = self.duration

    def update(self, dt):
        if self.timer > 0:
            self.timer -= dt

    def draw(self, screen):
        if self.timer <= 0:
            return
        alpha = int(255 * (self.timer / self.duration))
        flash_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        flash_surface.fill((255, 0, 0, alpha))
        screen.blit(flash_surface, (0, 0))