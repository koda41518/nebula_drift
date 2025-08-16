import pygame

class PauseScreen:
    def __init__(self, width, height, font):
        self.width = width
        self.height = height
        self.font = font
        self.message = "JEU EN PAUSE - Appuie sur ÉCHAP pour reprendre"
        self.bg_color = (0, 0, 0, 150)  # Transparence directe ici
        self.text_color = (255, 255, 100)

    def draw(self, screen):
        """
        Affiche un overlay de pause semi-transparent et le message de pause.
        """
        # Overlay semi-transparent noir
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill(self.bg_color)
        screen.blit(overlay, (0, 0))

        # Texte centré
        pause_text = self.font.render(self.message, True, self.text_color)
        text_rect = pause_text.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(pause_text, text_rect)

        # On "force" le rendu ici car c’est en mode pause
        pygame.display.flip()

    def handle_event(self, event, paused):
        """
        Retourne True ou False selon si le joueur appuie sur ÉCHAP.
        """
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return not paused
        return paused