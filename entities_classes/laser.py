import pygame

class Laser:
    def __init__(self, pos, direction):
        self.pos = pygame.Vector2(pos)           # Position actuelle du laser
        self.direction = direction               # Direction (vecteur normalisé)
        self.speed = 1000                        # Vitesse en unités/seconde
        self.life = 0                            # Durée de vie écoulée
        self.lifetime = 1.5                      # Durée de vie max en secondes

    def update(self, dt):
        # Avance dans la direction, en tenant compte du temps écoulé
        self.pos += self.direction * self.speed * dt
        self.life += dt

    def is_expired(self):
        # Le laser est détruit après 1.5 secondes
        return self.life > self.lifetime

    def draw(self, surface, offset):
        # Calcul de la position à l’écran
        screen_pos = self.pos - offset
        pygame.draw.line(surface, (255, 80, 80), screen_pos, screen_pos + self.direction * 20, 3)
    def collides_with(self, enemy):
        # Collision simple: si le laser est assez proche de l'ennemi
        return self.pos.distance_to(enemy.pos) < 20    