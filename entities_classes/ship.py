
import pygame
import math

class Ship:
    def __init__(self, pos, sprites):
        """
        Initialise le vaisseau avec une position, une orientation initiale, 
        une vitesse nulle et les sprites à utiliser.
        """
        self.pos = pygame.Vector2(pos)
        self.angle = 0
        self.speed = pygame.Vector2(0, 0)
        self.acceleration = 0.15
        self.rotation_speed = 3
        self.friction = 0.99

        self.sprites = sprites
        self.current_sprite = pygame.image.load(sprites["idle"]).convert_alpha()

    def update(self, keys):
        """
        Met à jour la position et l'orientation du vaisseau en fonction des touches pressées.
        Applique la friction pour ralentir progressivement le vaisseau.
        """
        if keys[pygame.K_LEFT]:
            self.angle += self.rotation_speed
        if keys[pygame.K_RIGHT]:
            self.angle -= self.rotation_speed
        if keys[pygame.K_UP]:
            # Calcul du vecteur direction selon l'angle
            angle_rad = math.radians(self.angle)
            direction = pygame.Vector2(math.cos(angle_rad), -math.sin(angle_rad))
            self.speed += direction * self.acceleration
            self.current_sprite = pygame.image.load(self.sprites["move"]).convert_alpha()
        else:
            self.current_sprite = pygame.image.load(self.sprites["idle"]).convert_alpha()

        # Appliquer la friction et mettre à jour la position
        self.speed *= self.friction
        self.pos += self.speed

    def draw(self, surface, offset):
        """
        Dessine le sprite du vaisseau avec rotation, centré sur la position actuelle moins l’offset caméra.
        """
        rotated_img = pygame.transform.rotate(self.current_sprite, self.angle)
        rect = rotated_img.get_rect(center=(self.pos - offset))
        surface.blit(rotated_img, rect)