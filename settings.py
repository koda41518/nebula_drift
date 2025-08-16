# Dimensions de la fenêtre
WIDTH = 1300
HEIGHT = 900

# Couleurs
BACKGROUND_COLOR = (10, 10, 30)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
SHIP_COLOR = (200, 200, 255)
LASER_COLOR = (255, 80, 80)

# Vaisseau
ACCELERATION = 0.15
ROTATION_SPEED = 3
FRICTION = 0.99
SHIP_START_HEALTH = 100

# Laser
LASER_SPEED = 1000
LASER_LIFETIME = 1.5
LASER_DAMAGE_RADIUS = 20

# Ennemis
ENEMY_DAMAGE = 25
ENEMY_SPEED = 1.2
ENEMY_SPAWN_INTERVAL = 2  # secondes


# Réparations
REPAIR_HEAL = 20
REPAIR_COOLDOWN = 5  # secondes

# Mini-carte
MINIMAP_SIZE = 200
MINIMAP_SCALE = 0.05

#Etoiles
STAR_COUNT = 1000  # nombre d’étoiles

DAMAGE_FLASH_DURATION = 0.3  # secondes

# Autres
FPS = 60
SHIP_SPRITES = {
    "idle": "assets/ship-sprit/vaisseau-1-arret.png",
    "move": "assets/ship-sprit/vaisseau-1.png",
    "thrust": "assets/ship-sprit/vaisseau-1-mvt.png",
    "boost": "assets/ship-sprit/vaisseau-1-boost.png",
}