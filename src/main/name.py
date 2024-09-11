import pygame
from pygame.locals import *

pygame.init()
name_screen = pygame.display.set_mode((640, 480))

def get_player_name():
    name = ""
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(220, 200, 200, 32)
    active = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    return name
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode

        name_screen.fill((255, 255, 255))
        pygame.draw.rect(name_screen, (0, 0, 0), input_box, 2)
        text_surface = font.render(name, True, (0, 0, 0))
        name_screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()

player_name = get_player_name()