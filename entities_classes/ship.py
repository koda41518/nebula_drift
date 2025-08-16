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
            "idle": pygame.transform.scale(
                pygame.image.load(sprites["idle"]).convert_alpha(), (128, 128)
            ),
            "move": pygame.transform.scale(
                pygame.image.load(sprites["move"]).convert_alpha(), (128, 128)
            )
        }
        self.current_sprite = self.sprites["idle"]

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.angle -= self.rotation_speed
        if keys[pygame.K_RIGHT]:
            self.angle += self.rotation_speed
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
        
    def take_damage(self, amount):
        """
        Réduit la santé du vaisseau.
        """
        self.health = max(0, self.health - amount)
    
    def heal(self, amount):
        """Soigne le vaisseau d’un certain montant, sans dépasser la vie max."""
        self.health = min(self.max_health, self.health + amount)
        
    def is_alive(self):
        return self.health > 0
    
    

    def draw(self, screen, offset):
        rotated_img = pygame.transform.rotate(self.current_sprite, -self.angle)
        rect = rotated_img.get_rect(center=(self.pos - offset))
        screen.blit(rotated_img, rect)
    def forward(self):
        """
        Retourne un vecteur directionnel basé sur l'angle du vaisseau.
        Ici, angle 0 = vers le haut.
        """
        angle_rad = math.radians(self.angle)
        return pygame.Vector2(math.sin(angle_rad), -math.cos(angle_rad))