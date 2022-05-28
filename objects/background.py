from loops.play_loop import *
from settings.states import *
import pygame
pygame.init()
class Camera:
    """
    Camera scrolling class
    """
    def __init__(self,x,y, max):
        self.max = max
        self.rect = pygame.Rect(x, y, 800, 600)

    def move(self, x):
        if self.rect[0] >= self.max:
            if x < 0:
                self.rect[0] += x
                return True
            else:
                self.rect[0] += 0
                return False
        elif self.rect[0] == 0:
            if x > 0:
                self.rect[0] += x
                return True
            else:
                self.rect[0] += 0
                return False
        else:
            self.rect[0] += x
            return True

#config.config_dict['pictures']['world'][5]'img/world/sky.png'








