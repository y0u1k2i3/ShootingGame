import pygame
from pygame import mixer
from variable import SCREEN_WIDTH, SCREEN_HEIGHT
from explosion import Explosion
from pygame.locals import *

def music_change(music):
    mixer.music.stop()
    mixer.music.unload()
    mixer.music.load(music)
    mixer.music.play(-1)

def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ')for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x,y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x,y))
            x += word_width + space 
        x= pos[0]
        y += word_height


name_screen = pygame.display.set_mode((1600, 900))

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
        name_screen.blit(text_surface, (input_box.x + 500, input_box.y + 200))
        pygame.display.flip()