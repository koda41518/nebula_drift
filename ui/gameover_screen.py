import pygame

class GameOverScreen:
    def __init__(self, width, height, font):
        self.width = width
        self.height = height
        self.font = font
        self.bg_color = (0, 0, 0)

    def draw(self, screen, score, high_score):
        """
        Dessine l'écran de fin de partie avec les scores et le bouton rejouer.
        Retourne le rectangle du bouton pour gérer les événements.
        """
        button_rect = pygame.Rect(self.width // 2 - 100, self.height // 2 + 80, 200, 50)

        screen.fill(self.bg_color)
        screen.blit(self.font.render("GAME OVER", True, (255, 0, 0)), (self.width // 2 - 100, self.height // 2 - 80))
        screen.blit(self.font.render(f"Score : {score} ennemis détruits", True, (255, 255, 255)), (self.width // 2 - 140, self.height // 2 - 20))
        screen.blit(self.font.render(f"Meilleur score : {high_score}", True, (200, 200, 255)), (self.width // 2 - 140, self.height // 2 + 20))
        screen.blit(self.font.render("Clique sur 'Rejouer' ou ferme la fenêtre", True, (180, 180, 180)), (self.width // 2 - 180, self.height // 2 + 50))

        pygame.draw.rect(screen, (255, 255, 255), button_rect)
        screen.blit(self.font.render("Rejouer", True, (0, 0, 0)), (button_rect.x + 50, button_rect.y + 10))

        return button_rect

    def handle_event(self, event, button_rect):
        """
        Gère les événements utilisateur sur l'écran de fin de jeu.
        Retourne une chaîne : 'quit', 'replay' ou None selon l'action.
        """
        if event.type == pygame.QUIT:
            return "quit"
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                return "replay"
        return None