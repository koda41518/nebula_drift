# ui/main_menu.py

import pygame

class MainMenu:
    def __init__(self, width, height, font):
        self.width = width
        self.height = height
        self.font = font

    def draw(self, screen):
        screen.fill((10, 10, 30))  # fond bleu nuit

        title = self.font.render("PEW PEW PEW 🚀", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.width // 2, self.height // 2 - 100))
        screen.blit(title, title_rect)

        subtitle = self.font.render("Un jeu de survie dans l'espace", True, (200, 200, 200))
        subtitle_rect = subtitle.get_rect(center=(self.width // 2, self.height // 2 - 50))
        screen.blit(subtitle, subtitle_rect)

        # Bouton "JOUER"
        button_rect = pygame.Rect(self.width // 2 - 100, self.height // 2 + 20, 200, 60)
        pygame.draw.rect(screen, (255, 255, 255), button_rect, border_radius=10)

        text_surface = self.font.render("JOUER", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

        return button_rect

    def handle_event(self, event, button_rect):
        if event.type == pygame.QUIT:
            return "quit"
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                return "start"
        return None