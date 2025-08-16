import pygame



class MiniMapUI:
    def __init__(self, size=200, scale=0.05):
        self.size = size
        self.scale = scale

    def draw(self, screen, ship_pos, enemies, repairs):
        surface = pygame.Surface((self.size, self.size))
        surface.fill((20, 20, 40))
        center = pygame.Vector2(self.size // 2, self.size // 2)

        pygame.draw.circle(surface, (200, 200, 255), center, 5)

        for enemy in enemies:
            rel_pos = (enemy.pos - ship_pos) * self.scale
            map_pos = center + rel_pos
            if 0 <= map_pos.x < self.size and 0 <= map_pos.y < self.size:
                pygame.draw.circle(surface, (255, 60, 60), (int(map_pos.x), int(map_pos.y)), 3)

        for repair in repairs:
            rel_pos = (repair.pos - ship_pos) * self.scale
            map_pos = center + rel_pos
            if 0 <= map_pos.x < self.size and 0 <= map_pos.y < self.size:
                pygame.draw.circle(surface, (60, 255, 60), (int(map_pos.x), int(map_pos.y)), 3)

        screen.blit(surface, (screen.get_width() - self.size - 20, screen.get_height() - self.size - 20))
    