import pygame
from settings import MINIMAP_SIZE, MINIMAP_SCALE

class MiniMapUI:
    def __init__(self, size=MINIMAP_SIZE, scale=MINIMAP_SCALE):
        self.size = size
        self.scale = scale

    def draw(self, screen, ship_pos, enemies, repairs , shields):
        """
        Dessine une mini-carte en bas à droite de l'écran :
        - Le joueur est au centre
        - Les ennemis sont en rouge
        - Les réparateurs sont en vert
        """
        # Surface de la mini-carte
        surface = pygame.Surface((self.size, self.size))
        surface.fill((20, 20, 40))  # Fond sombre

        center = pygame.Vector2(self.size // 2, self.size // 2)

        # 🚀 Vaisseau joueur (centre)
        pygame.draw.circle(surface, (200, 200, 255), center, 5)

        # 👾 Ennemis
        for enemy in enemies:
            rel_pos = (enemy.pos - ship_pos) * self.scale
            map_pos = center + rel_pos
            if 0 <= map_pos.x < self.size and 0 <= map_pos.y < self.size:
                pygame.draw.circle(surface, (255, 60, 60), (int(map_pos.x), int(map_pos.y)), 3)

        # 🛠 Réparateurs
        for repair in repairs:
            rel_pos = (repair.pos - ship_pos) * self.scale
            map_pos = center + rel_pos
            if 0 <= map_pos.x < self.size and 0 <= map_pos.y < self.size:
                pygame.draw.circle(surface, (60, 255, 60), (int(map_pos.x), int(map_pos.y)), 3)

        #bouclier
        for shield in shields:
            rel_pos = (shield.pos - ship_pos) * self.scale
            map_pos = center + rel_pos
            if 0 <= map_pos.x < self.size and 0 <= map_pos.y < self.size:
                pygame.draw.circle(surface, (100, 200, 255), (int(map_pos.x), int(map_pos.y)), 3)
            
        # Affichage en bas à droite
        screen.blit(surface, (screen.get_width() - self.size - 20, screen.get_height() - self.size - 20))