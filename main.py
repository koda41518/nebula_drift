import pygame
import sys
from entities_classes.camera import Camera
from entities_classes.background import Background
from entities_classes.ship import Ship
from core.GameManager import GameManager
from ui.hud import draw_hud
from ui.pause_screen import draw_pause
from ui.gameover_screen import draw_gameover
from ui.minimap import draw_minimap  # si t'as fait une minimap
import settings

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("Nebula Drift")
clock = pygame.time.Clock()

# === Instances principales ===
ship = Ship()
camera = Camera(ship)
bg = Background()
game_manager = GameManager()

# === Variables d'état ===
paused = False
running = True

# === Boucle de jeu ===
while running:
    dt = clock.tick(settings.FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused

            elif event.key == pygame.K_SPACE and not paused and not game_manager.game_over:
                direction = ship.get_direction()
                game_manager.fire_laser(ship.pos, direction)

    if not paused and not game_manager.game_over:
        ship.update(dt)
        camera.update()
        game_manager.update(ship, dt)

    # === Affichage ===
    screen.fill((0, 0, 0))
    bg.draw(screen, camera.pos)
    ship.draw(screen, camera.pos)

    for enemy in game_manager.enemies:
        enemy.draw(screen, camera.pos)
    for repair in game_manager.repairs:
        repair.draw(screen, camera.pos)
    for laser in game_manager.lasers:
        laser.draw(screen, camera.pos)

    draw_hud(screen, ship, game_manager)

    if paused:
        draw_pause(screen)

    if game_manager.game_over:
        draw_gameover(screen, game_manager.score)

    pygame.display.flip()

pygame.quit()
sys.exit()