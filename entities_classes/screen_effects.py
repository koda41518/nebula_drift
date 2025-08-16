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