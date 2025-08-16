import pygame
import random

class StarField:
    def __init__(self, num_stars=1000, bounds=3000):
        self.stars = [
            pygame.Vector2(random.randint(-bounds, bounds), random.randint(-bounds, bounds))
            for _ in range(num_stars)
        ]

    def draw(self, screen, offset, screen_size):
        width, height = screen_size
        for star in self.stars:
            screen_pos = star - offset
            if 0 <= screen_pos.x < width and 0 <= screen_pos.y < height:
                pygame.draw.circle(screen, (255, 255, 255), (int(screen_pos.x), int(screen_pos.y)), 2)