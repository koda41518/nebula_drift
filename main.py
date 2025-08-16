import pygame
import sys

#  Import des modules du projet
from core.GameManager import GameManager
from entities_classes.ship import Ship
from entities_classes.camera import Camera
from entities_classes.background import StarField
from entities_classes.screen_effects import DamageFlash

from ui.hud import HUD
from ui.pause_screen import PauseScreen
from ui.gameover_screen import GameOverScreen
from ui.minimap import MiniMapUI

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
    background = StarField()                  # Étoiles
    flash = DamageFlash()                      # Flash rouge lors des dégâts
    manager = GameManager()                    # Gère ennemis, réparations, tirs, etc.
    minimap = MiniMapUI()
    hud = HUD(pygame.font.SysFont("Arial", 24))
    pause_screen = PauseScreen(settings.WIDTH, settings.HEIGHT, hud.font)
    gameover_screen = GameOverScreen(settings.WIDTH, settings.HEIGHT, hud.font)

    paused = False
    running = True
    high_score = 0
    button_rect = None

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

            if manager.game_over and button_rect:
                action = gameover_screen.handle_event(event, button_rect)
                if action == "replay":
                    manager.reset()
                    ship.reset((0, 0))
                    paused = False

        # === Mise à jour logique ===
        if not paused and not manager.game_over:
            keys = pygame.key.get_pressed()
            ship.update(keys)
            camera.update(ship.pos, lerp_factor=0.15)
            manager.update(ship, dt)
            flash.update(dt)

        # === Rendu visuel ===
        screen.fill(settings.BACKGROUND_COLOR)

        # Offset de la caméra (à soustraire à toutes les positions)
        offset = camera.get_offset((settings.WIDTH, settings.HEIGHT))

        background.draw(screen, camera.pos, (settings.WIDTH, settings.HEIGHT))

        # Dessin des entités avec offset
        for laser in manager.lasers:
            laser.draw(screen, offset)
        for enemy in manager.enemies:
            enemy.draw(screen, offset)
        for repair in manager.repairs:
            repair.draw(screen, offset)

        ship.draw(screen, offset)
        flash.draw(screen)

        # === UI ===
        minimap.draw(screen, ship.pos, manager.enemies, manager.repairs)
        hud.draw(screen, ship.speed, ship.health, manager.score)

        # Écrans spéciaux
        if paused:
            pause_screen.draw(screen)
        elif manager.game_over:
            if manager.score > high_score:
                high_score = manager.score
            button_rect = gameover_screen.draw(screen, manager.score, high_score)

        # Actualise l’écran
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()