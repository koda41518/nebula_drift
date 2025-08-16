import pygame
class HUD:
    def __init__(self, font):
        self.font = font

    def draw(self, screen, ship_speed, player_health, score):
        screen.blit(self.font.render(f"Vitesse : {ship_speed.length():.2f}", True, (255, 255, 255)), (10, 10))
        screen.blit(self.font.render(f"Vie : {player_health}", True, (255, 50, 50)), (10, 40))
        screen.blit(self.font.render(f"Score : {score}", True, (255, 255, 255)), (10, 70))

