
import pygame

class Camera:
    def __init__(self, initial_pos: pygame.Vector2):
        self.pos = initial_pos

    def update(self, target_pos: pygame.Vector2, lerp_factor: float = 0.05):
        """Fait suivre la caméra à une position cible (souvent le joueur)."""
        self.pos += (target_pos - self.pos) * lerp_factor

    def get_offset(self, screen_size: tuple[int, int]) -> pygame.Vector2:
        """Retourne le décalage à appliquer à tous les objets pour compenser la position de la caméra."""
        return self.pos - pygame.Vector2(screen_size[0] // 2, screen_size[1] // 2)