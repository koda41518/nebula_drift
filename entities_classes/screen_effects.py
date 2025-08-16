import pygame
from settings import WIDTH, HEIGHT, DAMAGE_FLASH_DURATION

class ScreenEffects:
    def __init__(self):
        self.damage_flash_timer = 0

    def trigger_flash(self):
        self.damage_flash_timer = DAMAGE_FLASH_DURATION

    def update(self, dt):
        if self.damage_flash_timer > 0:
            self.damage_flash_timer -= dt

    def draw_flash(self, surface):
        if self.damage_flash_timer > 0:
            alpha = int(255 * (self.damage_flash_timer / DAMAGE_FLASH_DURATION))
            alpha = max(0, min(255, alpha))
            flash_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            flash_surface.fill((255, 0, 0, alpha))
            surface.blit(flash_surface, (0, 0))


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