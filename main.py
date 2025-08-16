import pygame
import math
import random

from settings import WIDTH, HEIGHT, FPS, screen, clock, font, ship_idle_img, ship_move_img, ship_thrust_img, ship_boost_img
from entities_classes import Ship, Enemy, Laser, Repair, Camera

def main():
    # === Initialisation des entités principales ===
    ship = Ship(start_pos=(0, 0), idle_img=ship_idle_img, move_img=ship_move_img,
                thrust_img=ship_thrust_img, boost_img=ship_boost_img)
    camera = Camera(initial_pos=ship.pos)

    enemies = []
    lasers = []
    repairs = []
    stars = [pygame.Vector2(random.randint(-3000, 3000), random.randint(-3000, 3000)) for _ in range(1000)]

    score = 0
    high_score = 0
    paused = False
    game_over = False
    spawn_timer = 0
    repair_timer = 0
    damage_flash_timer = 0

    running = True
    while running:
        dt = clock.tick(FPS) / 1000
        screen.fill((10, 10, 30))  # fond nuit

        # === Gestion des événements ===
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
                elif event.key == pygame.K_SPACE and not paused:
                    lasers.append(ship.fire_laser())

        # === Affichage pause ===
        if paused:
            pause_text = font.render("JEU EN PAUSE - Appuie sur ÉCHAP pour reprendre", True, (255, 255, 100))
            screen.blit(pause_text, (WIDTH // 2 - 300, HEIGHT // 2))
            pygame.display.flip()
            continue

        # === Contrôles vaisseau ===
        keys = pygame.key.get_pressed()
        ship.handle_input(keys)
        ship.update(dt)
        camera.update(ship.pos)

        offset = camera.offset

        # === Étoiles ===
        for star in stars:
            screen_pos = star - offset
            if 0 <= screen_pos.x < WIDTH and 0 <= screen_pos.y < HEIGHT:
                pygame.draw.circle(screen, (255, 255, 255), (int(screen_pos.x), int(screen_pos.y)), 2)

        # === Spawning ennemis et réparations ===
        spawn_timer += dt
        if spawn_timer >= 2:
            enemies.append(Enemy.spawn_near(ship.pos))
            spawn_timer = 0

        repair_timer += dt
        if repair_timer >= 5:
            repairs.append(Repair.spawn_near(ship.pos))
            repair_timer = 0

        # === Mise à jour et affichage entités ===
        for enemy in enemies[:]:
            enemy.update(dt, ship.pos)
            if enemy.check_collision(ship):
                ship.take_damage(enemy.damage)
                damage_flash_timer = 0.3
                enemies.remove(enemy)
            enemy.draw(screen, offset)

        for laser in lasers[:]:
            laser.update(dt)
            for enemy in enemies[:]:
                if laser.collides_with(enemy):
                    enemies.remove(enemy)
                    if laser in lasers:
                        lasers.remove(laser)
                    score += 1
                    break
            if laser.should_remove(WIDTH, HEIGHT, offset):
                lasers.remove(laser)
            else:
                laser.draw(screen, offset)

        for repair in repairs[:]:
            if repair.check_pickup(ship):
                ship.repair(20)
                repairs.remove(repair)
            else:
                repair.draw(screen, offset)

        # === Vaisseau ===
        ship.draw(screen, offset)

        # === Flash rouge si dégâts ===
        if damage_flash_timer > 0:
            damage_flash_timer -= dt
            alpha = int(255 * (damage_flash_timer / 0.3))
            flash_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            flash_surface.fill((255, 0, 0, alpha))
            screen.blit(flash_surface, (0, 0))

        # === UI ===
        screen.blit(font.render(f"Vitesse : {ship.speed.length():.2f}", True, (255, 255, 255)), (10, 10))
        screen.blit(font.render(f"Vie : {ship.health}", True, (255, 50, 50)), (10, 40))
        screen.blit(font.render(f"Score : {score}", True, (255, 255, 255)), (10, 70))

        # === Minimap (fonction à extraire si besoin) ===
        # TODO : à modulariser si tu veux
        # ...

        pygame.display.flip()

        # === Fin du jeu ===
        if ship.health <= 0:
            game_over = True
            if score > high_score:
                high_score = score
            break

    # === Écran de fin ===
    # TODO : écran de game over + bouton rejouer
    # Tu peux garder celui de ton ancien code ou l'encapsuler dans une fonction séparée

if __name__ == "__main__":
    main()
    pygame.quit()