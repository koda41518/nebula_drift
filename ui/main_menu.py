# ui/main_menu.py

import pygame
import random

class MainMenu:
    def __init__(self, width, height, font):
        self.width = width
        self.height = height
        self.font = font
        self.small_font = pygame.font.SysFont("Arial", 20)
        self.title_font = pygame.font.SysFont("Arial", 48)

        # Pour un fond étoilé animé
        self.stars = [pygame.Vector2(random.randint(0, width), random.randint(0, height)) for _ in range(100)]

    def draw(self, screen):
        screen.fill((10, 10, 30))  # Fond bleu nuit

        # ⭐ Animation des étoiles
        for star in self.stars:
            pygame.draw.circle(screen, (255, 255, 255), (int(star.x), int(star.y)), 1)
            star.y += 0.5
            if star.y > self.height:
                star.y = 0
                star.x = random.randint(0, self.width)

        # 🎮 Titre
        title = self.title_font.render("PEW PEW PEW 🚀", True, (255, 255, 100))
        screen.blit(title, title.get_rect(center=(self.width // 2, 100)))

        subtitle = self.small_font.render("Un jeu de survie dans l'espace", True, (180, 180, 180))
        screen.blit(subtitle, subtitle.get_rect(center=(self.width // 2, 150)))

        # 🎯 Bouton JOUER
        play_rect = pygame.Rect(self.width // 2 - 100, self.height // 2 - 20, 200, 50)
        self.draw_button(screen, play_rect, "JOUER")

        # ❌ Bouton QUITTER
        quit_rect = pygame.Rect(self.width // 2 - 100, self.height // 2 + 50, 200, 50)
        self.draw_button(screen, quit_rect, "QUITTER")

        # 🧾 Instructions
        controls = [
            "↑ : Avancer",
            "← / → : Tourner",
            "Espace : Tirer",
            "Échap : Pause",
        ]
        for i, text in enumerate(controls):
            info = self.small_font.render(text, True, (200, 200, 200))
            screen.blit(info, (20, self.height - 110 + i * 20))

        # Retourne les deux boutons pour gestion des événements
        return {"play": play_rect, "quit": quit_rect}

    def draw_button(self, screen, rect, text):
        # Effet hover
        mouse_pos = pygame.mouse.get_pos()
        color = (200, 200, 255) if rect.collidepoint(mouse_pos) else (255, 255, 255)
        pygame.draw.rect(screen, color, rect, border_radius=10)

        text_surface = self.font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, text_surface.get_rect(center=rect.center))

    def handle_event(self, event, buttons):
        if event.type == pygame.QUIT:
            return "quit"
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if buttons["play"].collidepoint(event.pos):
                return "start"
            if buttons["quit"].collidepoint(event.pos):
                return "quit"
        return None