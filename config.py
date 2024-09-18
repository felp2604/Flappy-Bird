import pygame as py
from random import choice

def getScreenSize():
  return (422, 750)

def getFlappyBirdRect():  
  jumping_surface = py.image.load("assets/yellowbird-upflap.png")
  down_surface = py.image.load("assets/yellowbird-downflap.png")
  jumping_rect = jumping_surface.get_rect()
  bird_rect = down_surface.get_rect()

  # initial position
  bird_rect.topleft = (200, 250)
  return jumping_surface, down_surface, bird_rect


def getBackground():
  return py.image.load("assets/background-day.png")

class Pipe:
  def __init__(self, x, y, pipe_image, pipe_gap=200):
    self.image = pipe_image
    self.pipe_gap = pipe_gap
    
    self.top_rect = self.image.get_rect(topleft=(x, y - self.image.get_height()))
    self.bottom_rect = self.image.get_rect(topleft=(x, y + self.pipe_gap))

  def update(self):
    self.top_rect.x -= 4
    self.bottom_rect.x -= 4

  def draw(self, screen):
    screen.blit(self.image, self.top_rect)
    screen.blit(self.image, self.bottom_rect)

  def is_off_screen(self):
    return self.top_rect.right < 0

