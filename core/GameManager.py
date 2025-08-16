import pygame
import random
import math
from entities_classes.enemies import Enemy
from entities_classes.repair import Repair
from entities_classes.laser import Laser 
from entities_classes.screen_effects import DamageFlash
import settings
import time


class GameManager:
    def __init__(self):
        self.enemies = []
        self.repairs = []
        self.lasers = []

        self.last_enemy_spawn = time.time()
        self.last_repair_spawn = time.time()
        self.enemy_spawn_delay = 2.5
        self.repair_spawn_delay = 8

        self.score = 0
        self.game_over = False

    def update(self, ship, dt):
        now = time.time()

        # Spawn d’ennemis
        if now - self.last_enemy_spawn > self.enemy_spawn_delay:
            self.enemies.append(Enemy.spawn_near(ship.pos))
            self.last_enemy_spawn = now

        # Spawn de réparateurs
        if now - self.last_repair_spawn > self.repair_spawn_delay:
            self.repairs.append(Repair.spawn_near(ship.pos))
            self.last_repair_spawn = now

        # MAJ ennemis
        for enemy in self.enemies[:]:
            enemy.update(ship.pos, dt)
            if enemy.check_collision_with_ship(ship):
                self.enemies.remove(enemy)

        # MAJ lasers + collision
        for laser in self.lasers[:]:
            laser.update(dt)
            for enemy in self.enemies[:]:
                if laser.collides_with(enemy):
                    self.enemies.remove(enemy)
                    if laser in self.lasers:
                        self.lasers.remove(laser)
                    self.score += 1
                    break

        # MAJ réparateurs
        for repair in self.repairs[:]:
            if ship.pos.distance_to(repair.pos) < 30:
                ship.heal()
                self.repairs.remove(repair)

        # Nettoyage des lasers expirés
        self.lasers = [l for l in self.lasers if not l.expired()]

        # Check game over
        if ship.health <= 0:
            self.game_over = True

    def reset(self):
        self.enemies.clear()
        self.repairs.clear()
        self.lasers.clear()
        self.score = 0
        self.game_over = False
        self.last_enemy_spawn = time.time()
        self.last_repair_spawn = time.time()

    def fire_laser(self, pos, direction):
        self.lasers.append(Laser(pos, direction))
