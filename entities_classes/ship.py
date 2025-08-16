import pygame
import math

class Ship:
    def __init__(self, pos, sprites):
        self.pos = pygame.Vector2(pos)
        self.angle = 0
        self.speed = pygame.Vector2(0, 0)
        self.acceleration = 0.15
        self.rotation_speed = 3
        self.friction = 0.99

        self.health = 100
        self.max_health = 100

        # 🔁 On charge les sprites UNE FOIS ici
        self.sprites = {
            "idle": pygame.image.load(sprites["idle"]).convert_alpha(),
            "move": pygame.image.load(sprites["move"]).convert_alpha()
        }
        self.current_sprite = self.sprites["idle"]

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.angle += self.rotation_speed
        if keys[pygame.K_RIGHT]:
            self.angle -= self.rotation_speed
        if keys[pygame.K_UP]:
            direction = self.forward()
            self.speed += direction * self.acceleration
            self.current_sprite = self.sprites["move"]
        else:
            self.current_sprite = self.sprites["idle"]

        self.speed *= self.friction
        self.pos += self.speed 
    def reset(self, pos):
        self.pos = pygame.Vector2(pos)
        self.angle = 0
        self.speed = pygame.Vector2(0, 0)
        self.health = self.max_health
        self.current_sprite = self.sprites["idle"]