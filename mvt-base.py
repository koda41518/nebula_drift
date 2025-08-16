
#code compacte de

import pygame
import math
import random

# Initialisation globale du jeu
pygame.init()
WIDTH, HEIGHT = 1300, 900  # Taille de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nebula Drift")  # Titre de la fenêtre
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)  # Police pour le texte



high_score = 0  # Meilleur score stocké en mémoire

def main():
    global high_score
    paused = False  # État de pause du jeu

    # Variables du joueur (vaisseau)
    ship_pos = pygame.Vector2(0, 0)
    ship_angle = 90
    ship_speed = pygame.Vector2(0, 0)
    acceleration = 0.15
    rotation_speed = 3
    friction = 0.99

    camera_pos = ship_pos.copy()
    score = 0
    player_health = 100
    enemy_damage = 25
    laser_damage_radius = 20
    laser_speed = 1000  # Vitesse du laser
    laser_lifetime = 1.5  # Durée de vie du laser en secondes
    damage_flash_timer = 0  # Durée du flash rouge en cas de dégâts

    # Listes des objets du jeu
    enemies = []
    lasers = []
    repairs = []
    repair_timer = 0

    # Génération aléatoire des étoiles de fond
    stars = [pygame.Vector2(random.randint(-3000, 3000), random.randint(-3000, 3000)) for _ in range(1000)]

    # Fonction pour faire apparaître un ennemi autour du joueur
    def spawn_enemy():
        angle = random.uniform(0, 2 * math.pi)
        distance = random.randint(800, 1200)
        offset = pygame.Vector2(math.cos(angle), math.sin(angle)) * distance
        return {"pos": ship_pos + offset, "speed": 1.2}

    # Fonction pour faire apparaître un point de réparation
    def spawn_repair():
        angle = random.uniform(0, 2 * math.pi)
        distance = random.randint(800, 1600)
        offset = pygame.Vector2(math.cos(angle), math.sin(angle)) * distance
        return {"pos": ship_pos + offset}

    spawn_timer = 0
    running = True
    game_over = False

    # Boucle principale du jeu
    while running:
        dt = clock.tick(60) / 1000  # Temps écoulé depuis la dernière frame
        screen.fill((10, 10, 30))  # Fond bleu nuit

        # Gestion des événements (clavier, souris)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused  # Basculer entre pause et jeu
                elif event.key == pygame.K_SPACE and not paused:
                    # Création d'un laser dans la direction du vaisseau
                    angle_rad = math.radians(ship_angle)
                    direction = pygame.Vector2(math.cos(angle_rad), -math.sin(angle_rad))
                    lasers.append({"pos": pygame.Vector2(ship_pos), "dir": direction, "life": 0.0})

        # Affichage en cas de pause
        if paused:
            pause_text = font.render("JEU EN PAUSE - Appuie sur ÉCHAP pour reprendre", True, (255, 255, 100))
            screen.blit(pause_text, (WIDTH // 2 - 300, HEIGHT // 2))
            pygame.display.flip()
            continue

        # Contrôles de mouvement du vaisseau
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ship_angle += rotation_speed
        if keys[pygame.K_RIGHT]:
            ship_angle -= rotation_speed
        if keys[pygame.K_UP]:
            angle_rad = math.radians(ship_angle)
            direction = pygame.Vector2(math.cos(angle_rad), -math.sin(angle_rad))
            ship_speed += direction * acceleration

        # Mise à jour de la position du vaisseau
        ship_speed *= friction
        ship_pos += ship_speed
        camera_pos += (ship_pos - camera_pos) * 0.05  # Caméra à suivi progressif
        offset = camera_pos - pygame.Vector2(WIDTH // 2, HEIGHT // 2)

        # Affichage du fond étoilé
        for star in stars:
            screen_pos = star - offset
            if 0 <= screen_pos.x < WIDTH and 0 <= screen_pos.y < HEIGHT:
                pygame.draw.circle(screen, (255, 255, 255), (int(screen_pos.x), int(screen_pos.y)), 2)

        # Apparition des ennemis
        spawn_timer += dt
        if spawn_timer >= 2:
            enemies.append(spawn_enemy())
            spawn_timer = 0

        # Apparition des points de réparation
        repair_timer += dt
        if repair_timer >= 5:
            repairs.append(spawn_repair())
            repair_timer = 0

        # Déplacement et collision des ennemis
        for enemy in enemies[:]:
            enemy["pos"] += (ship_pos - enemy["pos"]).normalize() * enemy["speed"]
            if enemy["pos"].distance_to(ship_pos) < 30:
                player_health -= enemy_damage
                damage_flash_timer = 0.3
                enemies.remove(enemy)
                continue
            screen_pos = enemy["pos"] - offset
            pygame.draw.circle(screen, (255, 50, 50), (int(screen_pos.x), int(screen_pos.y)), 12)

        # Déplacement et collisions des lasers
        for laser in lasers[:]:
            laser["pos"] += laser["dir"] * laser_speed * dt
            laser["life"] += dt

            for enemy in enemies[:]:
                if laser["pos"].distance_to(enemy["pos"]) < laser_damage_radius:
                    enemies.remove(enemy)
                    if laser in lasers:
                        lasers.remove(laser)
                    score += 1
                    break

            screen_pos = laser["pos"] - offset
            if laser["life"] > laser_lifetime or not (0 <= screen_pos.x < WIDTH and 0 <= screen_pos.y < HEIGHT):
                if laser in lasers:
                    lasers.remove(laser)
            else:
                pygame.draw.line(screen, (255, 80, 80), screen_pos, screen_pos + laser["dir"] * 20, 3)

        # Affichage et gestion des points de réparation
        for repair in repairs[:]:
            if ship_pos.distance_to(repair["pos"]) < 30:
                player_health = min(player_health + 20, 100)
                repairs.remove(repair)
                continue
            screen_pos = repair["pos"] - offset
            pygame.draw.circle(screen, (50, 255, 50), (int(screen_pos.x), int(screen_pos.y)), 10)

        # Dessin du vaisseau
        def draw_ship(pos, angle):
            angle_rad = math.radians(angle)
            direction = pygame.Vector2(math.cos(angle_rad), -math.sin(angle_rad))
            perp = direction.rotate(90)
            p1 = pos + direction * 20
            p2 = pos - direction * 10 + perp * 10
            p3 = pos - direction * 10 - perp * 10
            pygame.draw.polygon(screen, (200, 200, 255), [p1, p2, p3])

        draw_ship(ship_pos - offset, ship_angle)

        # Flash rouge en cas de dégâts
        if damage_flash_timer > 0:
            damage_flash_timer -= dt
            flash_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            alpha = int(255 * (damage_flash_timer / 0.3))
            alpha = max(0, min(255, alpha))
            flash_surface.fill((255, 0, 0, alpha))
            screen.blit(flash_surface, (0, 0))

        # Interface : vitesse, vie, score
        screen.blit(font.render(f"Vitesse : {ship_speed.length():.2f}", True, (255, 255, 255)), (10, 10))
        screen.blit(font.render(f"Vie : {player_health}", True, (255, 50, 50)), (10, 40))
        screen.blit(font.render(f"Score : {score}", True, (255, 255, 255)), (10, 70))

        # Mini-carte
        minimap_size = 200
        minimap_scale = 0.05
        minimap_surface = pygame.Surface((minimap_size, minimap_size))
        minimap_surface.fill((20, 20, 40))
        center = pygame.Vector2(minimap_size // 2, minimap_size // 2)
        pygame.draw.circle(minimap_surface, (200, 200, 255), center, 5)

        for enemy in enemies:
            rel_pos = (enemy["pos"] - ship_pos) * minimap_scale
            map_pos = center + rel_pos
            if 0 <= map_pos.x < minimap_size and 0 <= map_pos.y < minimap_size:
                pygame.draw.circle(minimap_surface, (255, 60, 60), (int(map_pos.x), int(map_pos.y)), 3)

        for repair in repairs:
            rel_pos = (repair["pos"] - ship_pos) * minimap_scale
            map_pos = center + rel_pos
            if 0 <= map_pos.x < minimap_size and 0 <= map_pos.y < minimap_size:
                pygame.draw.circle(minimap_surface, (60, 255, 60), (int(map_pos.x), int(map_pos.y)), 3)

        screen.blit(minimap_surface, (WIDTH - minimap_size - 20, HEIGHT - minimap_size - 20))

        pygame.display.flip()

        # Condition de fin de partie
        if player_health <= 0:
            game_over = True
            if score > high_score:
                high_score = score
            break

    # Écran de fin de partie
    if game_over:
        button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 80, 200, 50)
        while True:
            screen.fill((0, 0, 0))
            screen.blit(font.render("GAME OVER", True, (255, 0, 0)), (WIDTH // 2 - 100, HEIGHT // 2 - 80))
            screen.blit(font.render(f"Score : {score} ennemis détruits", True, (255, 255, 255)), (WIDTH // 2 - 140, HEIGHT // 2 - 20))
            screen.blit(font.render(f"Meilleur score : {high_score}", True, (200, 200, 255)), (WIDTH // 2 - 140, HEIGHT // 2 + 20))
            screen.blit(font.render("Clique sur 'Rejouer' ou ferme la fenêtre", True, (180, 180, 180)), (WIDTH // 2 - 180, HEIGHT // 2 + 50))
            pygame.draw.rect(screen, (255, 255, 255), button_rect)
            screen.blit(font.render("Rejouer", True, (0, 0, 0)), (button_rect.x + 50, button_rect.y + 10))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if button_rect.collidepoint(event.pos):
                        main()
                        return

# Lancement initial du jeu
main()
pygame.quit()