import pygame

class PauseScreen:
    def __init__(self, width, height, font):
        self.width = width
        self.height = height
        self.font = font
        self.message = "JEU EN PAUSE - Appuie sur ÉCHAP pour reprendre"
        self.bg_color = (0, 0, 0)
        self.text_color = (255, 255, 100)

    def draw(self, screen):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))

        pause_text = self.font.render(self.message, True, self.text_color)
        text_rect = pause_text.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(pause_text, text_rect)
        pygame.display.flip()

    def handle_event(self, event, paused):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return not paused
        return paused
    