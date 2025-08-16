import pygame
import math
import random

class Enemy:
    def __init__(self, pos, speed=1.2, damage=25):
        self.pos = pygame.Vector2(pos)
        self.speed = speed
        self.damage = damage

    def update(self, target_pos, dt):
        direction = (target_pos - self.pos).normalize()
        self.pos += direction * self.speed

    def draw(self, screen, offset):
        screen_pos = self.pos - offset
        pygame.draw.circle(screen, (255, 50, 50), (int(screen_pos.x), int(screen_pos.y)), 12)

    def check_collision_with_ship(self, ship):
        if self.pos.distance_to(ship.pos) < 30:
            ship.take_damage(self.damage)
            return True
        return False

    @staticmethod
    def spawn_near(center_pos, min_dist=800, max_dist=1200):
        angle = random.uniform(0, 2 * math.pi)
        distance = random.randint(min_dist, max_dist)
        offset = pygame.Vector2(math.cos(angle), math.sin(angle)) * distance
        return Enemy(center_pos + offset)