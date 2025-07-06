import pygame
import math
import random

# Initialisation
pygame.init()

pygame.font.init()
font = pygame.font.SysFont("Arial", 24)

WIDTH, HEIGHT = 1300, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nebula Drift")
clock = pygame.time.Clock()

# Vaisseau
ship_pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
ship_angle = 0  # degrés
ship_speed = pygame.Vector2(0, 0)
acceleration = 0.15
rotation_speed = 3
friction = 0.99  # pour ralentir naturellement

# Fond étoilé
stars = [pygame.Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(100)]

# Boucle principale
running = True
while running:
    dt = clock.tick(60) / 1000  # temps entre chaque frame
    screen.fill((10, 10, 30))  # fond spatial

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Contrôles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship_angle += rotation_speed  # tourne à gauche
    if keys[pygame.K_RIGHT]:
        ship_angle -= rotation_speed  # tourne à droite
    if keys[pygame.K_UP]:
        # Appliquer une poussée dans la direction du vaisseau
        angle_rad = math.radians(ship_angle)
        direction = pygame.Vector2(math.cos(angle_rad), -math.sin(angle_rad))
        thrust = direction * acceleration
        ship_speed += thrust

    # Appliquer la friction pour ralentir
    ship_speed *= friction

    # Mise à jour de la position
    ship_pos += ship_speed

    # Écran torique (wrap-around)
    ship_pos.x %= WIDTH
    ship_pos.y %= HEIGHT

    # Dessiner les étoiles
    for star in stars:
        pygame.draw.circle(screen, (255, 255, 255), (int(star.x), int(star.y)), 1)

    # Fonction pour dessiner le vaisseau
    def draw_ship(pos, angle):
        angle_rad = math.radians(angle)
        direction = pygame.Vector2(math.cos(angle_rad), -math.sin(angle_rad))
        perp = direction.rotate(90)

        # Triangle : avant, arrière gauche, arrière droite
        p1 = pos + direction * 20
        p2 = pos - direction * 10 + perp * 10
        p3 = pos - direction * 10 - perp * 10

        pygame.draw.polygon(screen, (200, 200, 255), [p1, p2, p3])

    # Dessiner le vaisseau
    draw_ship(ship_pos, ship_angle)



    # Affichage de la vitesse
    speed_value = ship_speed.length()  # longueur du vecteur = vitesse
    speed_text = font.render(f"Vitesse : {speed_value:.2f} px/s", True, (255, 255, 255))
    screen.blit(speed_text, (10, 10))  # Affiche en haut à gauche
    # Actualiser l'affichage
    pygame.display.flip()

pygame.quit()