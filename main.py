import pygame
import sys

# 📦 Import des modules du projet
from core.GameManager import GameManager
from entities_classes.ship import Ship
from entities_classes.camera import Camera
from entities_classes.background import Background
from entities_classes.screen_effects import DamageFlash

from ui.hud import draw_hud
from ui.pause_screen import draw_pause_screen
from ui.gameover_screen import draw_gameover_screen
from ui.minimap import draw_minimap

import settings


def main():
    # === Initialisation générale ===
    pygame.init()
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("Nebula Drift")
    clock = pygame.time.Clock()

    # === Initialisation des objets ===
    ship = Ship((0, 0), settings.SHIP_SPRITES)  # Vaisseau du joueur
    camera = Camera(ship.pos)                  # Caméra qui suit le vaisseau
    background = Background()                  # Étoiles
    flash = DamageFlash()                      # Flash rouge lors des dégâts
    manager = GameManager()                    # Gère ennemis, réparations, tirs, etc.

    paused = False
    running = True

    # === Boucle principale ===
    while running:
        dt = clock.tick(settings.FPS) / 1000  # deltaTime : temps entre deux frames

        # === Gestion des événements clavier/souris ===
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused  # Toggle pause
                elif event.key == pygame.K_SPACE and not paused and not manager.game_over:
                    manager.fire_laser(ship.pos, ship.forward())  # Tir laser

        # === Mise à jour logique (si pas en pause ni game over) ===
        if not paused and not manager.game_over:
            keys = pygame.key.get_pressed()
            ship.update(keys)
            camera.update(ship.pos)
            manager.update(ship, dt)
            flash.update(dt)

        # === Rendu visuel ===
        screen.fill(settings.BACKGROUND_COLOR)
        background.draw(screen, camera.pos)

        # Dessin des entités
        for laser in manager.lasers:
            laser.draw(screen, camera.pos)
        for enemy in manager.enemies:
            enemy.draw(screen, camera.pos)
        for repair in manager.repairs:
            repair.draw(screen, camera.pos)

        # Vaisseau + effets visuels
        ship.draw(screen, camera.pos)
        flash.draw(screen)

        # === UI ===
        draw_minimap(screen, ship, manager.enemies, camera)
        draw_hud(screen, ship.speed, ship.health, manager.score)

        # Écrans spéciaux
        if paused:
            draw_pause_screen(screen)
        elif manager.game_over:
            draw_gameover_screen(screen, manager.score)

        # Actualise l'écran
        pygame.display.flip()

    # === Fermeture propre ===
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()