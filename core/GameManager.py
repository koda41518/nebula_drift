import time

class GameManager:
    def __init__(self, ship, settings):
        self.ship = ship
        self.settings = settings
        self.score = 0
        self.high_score = 0
        self.kill_count = 0
        self.last_enemy_spawn = time.time()
        self.last_repair_spawn = time.time()
        self.is_game_over = False

    def update(self):
        # Vérifie la vie du vaisseau
        if self.ship.health <= 0:
            self.is_game_over = True
            self.update_high_score()

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

    def add_kill(self):
        self.kill_count += 1
        self.score += 1

    def should_spawn_enemy(self):
        return time.time() - self.last_enemy_spawn >= self.settings["ENEMY_SPAWN_INTERVAL"]

    def mark_enemy_spawned(self):
        self.last_enemy_spawn = time.time()

    def should_spawn_repair(self):
        return time.time() - self.last_repair_spawn >= self.settings["REPAIR_SPAWN_INTERVAL"]

    def mark_repair_spawned(self):
        self.last_repair_spawn = time.time()

    def reset(self):
        self.score = 0
        self.kill_count = 0
        self.last_enemy_spawn = time.time()
        self.last_repair_spawn = time.time()
        self.is_game_over = False