import pygame
from settings import WHITE, RED  # Bonus : si tu veux centraliser les couleurs

class HUD:
    def __init__(self, font):
        self.font = font

    def draw(self, screen, ship_speed, player_health, score):
        """
        Affiche les infos principales en haut à gauche :
        - Vitesse du vaisseau
        - Santé du joueur
        - Score
        """
        vitesse_txt = self.font.render(f"Vitesse : {ship_speed.length():.2f}", True, WHITE)
        vie_txt = self.font.render(f"Vie : {player_health}", True, RED)
        score_txt = self.font.render(f"Score : {score}", True, WHITE)

        screen.blit(vitesse_txt, (10, 10))
        screen.blit(vie_txt, (10, 40))
        screen.blit(score_txt, (10, 70))