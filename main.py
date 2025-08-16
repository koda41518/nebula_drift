import pygame
import math
import random

from settings import WIDTH, HEIGHT, FPS, screen, clock, font, ship_idle_img, ship_move_img, ship_thrust_img, ship_boost_img
from entities_classes import Ship, Enemy, Laser, Repair, Camera

from entities_classes.ship import Ship
from entities_classes.enemies import Enemy
from entities_classes.laser import Laser
from entities_classes.repair import RepairPoint
from ui.hud import HUD
from ui.pause_screen import PauseScreen
from ui.minimap import MiniMapUI
from ui.gameover_screen import GameOverScreen
# + settings, etc.

def main():
    # Init du jeu
    ship = Ship()
    enemies = []
    repairs = []
    lasers = []

    hud = HUD(font)
    pause_screen = PauseScreen(WIDTH, HEIGHT, font)
    minimap = MiniMapUI()
    gameover = GameOverScreen(WIDTH, HEIGHT, font)

    paused = False
    game_over = False
    # etc.

    while running:
        handle_events()
        if paused:
            pause_screen.draw(screen)
            continue
        
        ship.update()
        for enemy in enemies:
            enemy.update(ship)
            enemy.draw(screen)
        for laser in lasers:
            laser.update()
            laser.check_collisions(enemies)

        # etc.
        hud.draw(...)
        minimap.draw(...)