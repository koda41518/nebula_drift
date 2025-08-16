import pygame
import random
import math
from entities_classes.enemies import Enemy
from entities_classes.repair import Repair
from entities_classes.laser import Laser 
from entities_classes.screen_effects import DamageFlash
import settings

class GameManager:
    def __init__(self, ship, camera):
        self.ship = ship
        self.camera = camera

        self.enemies = []
        self.lasers = []
        self.repairs = []

        self.spawn_timers = {
            "enemy": 0.0,
            "repair": 0.0,
        }

        self.score = 0
        self.high_score = 0
        self.damage_flash = DamageFlash()

    def update(self, dt):
        self.spawn_timers["enemy"] -= dt
        self.spawn_timers["repair"] -= dt

        for enemy in self.enemies:
            enemy.update(self.ship.pos, dt)

        for laser in self.lasers:
            laser.update(dt)

        self.damage_flash.update(dt)

        self.handle_collisions()
        self.cleanup_entities()

    def handle_collisions(self):
        # Collision laser vs ennemi
        for laser in self.lasers:
            for enemy in self.enemies:
                if laser.check_collision(enemy):  # suppose que laser a cette méthode
                    self.enemies.remove(enemy)
                    self.score += 1
                    break

        # Collision enemy vs ship
        for enemy in self.enemies:
            if enemy.check_collision_with_ship(self.ship):
                self.enemies.remove(enemy)
                self.damage_flash.trigger()

        # Collision repair vs ship
        for repair in self.repairs:
            if self.ship.check_pickup(repair):  # tu peux avoir une méthode ship.check_pickup
                self.repairs.remove(repair)

    def cleanup_entities(self):
        self.lasers = [l for l in self.lasers if l.alive()]  # s’il y a un `alive()` ou un `lifetime` dans laser

    def try_spawn_enemy(self):
        if self.spawn_timers["enemy"] <= 0:
            from entities_classes.enemies import Enemy
            self.enemies.append(Enemy.spawn_near(self.ship.pos))
            self.spawn_timers["enemy"] = 2.5

    def try_spawn_repair(self):
        if self.spawn_timers["repair"] <= 0:
            from entities_classes.repair import Repair
            self.repairs.append(Repair.spawn_near(self.ship.pos))
            self.spawn_timers["repair"] = 8.0