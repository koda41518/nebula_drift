import pygame
import math

class Ship:
    def __init__(self, pos, sprites):
        """
        Initialise le vaisseau avec position, orientation, vitesse, sprites, et santé.
        """
        self.pos = pygame.Vector2(pos)
        self.angle = 0
        self.speed = pygame.Vector2(0, 0)
        self.acceleration = 0.15
        self.rotation_speed = 3
        self.friction = 0.99

        self.health = 100
        self.max_health = 100

        self.sprites = sprites
        self.current_sprite = pygame.image.load(sprites["idle"]).convert_alpha()

    def update(self, keys):
        """
        Met à jour la position et l'orientation du vaisseau selon les entrées clavier.
        """
        if keys[pygame.K_LEFT]:
            self.angle += self.rotation_speed
        if keys[pygame.K_RIGHT]:
            self.angle -= self.rotation_speed
        if keys[pygame.K_UP]:
            angle_rad = math.radians(self.angle)
            direction = pygame.Vector2(math.cos(angle_rad), -math.sin(angle_rad))
            self.speed += direction * self.acceleration
            self.current_sprite = pygame.image.load(self.sprites["move"]).convert_alpha()
        else:
            self.current_sprite = pygame.image.load(self.sprites["idle"]).convert_alpha()

        self.speed *= self.friction
        self.pos += self.speed

    def draw(self, surface, offset):
        """
        Dessine le sprite avec rotation et offset caméra.
        """
        rotated_img = pygame.transform.rotate(self.current_sprite, self.angle)
        rect = rotated_img.get_rect(center=(self.pos - offset))
        surface.blit(rotated_img, rect)

    def take_damage(self, amount):
        """
        Réduit la santé du vaisseau. Retourne True si le vaisseau est détruit.
        """
        self.health = max(0, self.health - amount)
        return self.health <= 0

    def heal(self, amount):
        """
        Restaure de la santé au vaisseau.
        """
        self.health = min(self.max_health, self.health + amount)

    def is_alive(self):
        return self.health > 0