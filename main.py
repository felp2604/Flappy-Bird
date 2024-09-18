import pygame as py
from config import getScreenSize, getFlappyBirdRect, getBackground, Pipe
import math
import random

def main():
  py.init()

  clock = py.time.Clock()
  FPS = 60

  SCREEN_WIDTH, SCREEN_HEIGHT = getScreenSize()
  Y_GRAVITY = 0.5
  JUMP_HEIGHT = 9
  Y_VELOCITY = -6

  screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  py.display.set_caption("Flappy Bird")

  pipes = []
  pipe_timer = 0

  # game variables
  jumping_surface, down_surface, bird_rect = getFlappyBirdRect()

  background = getBackground()
  background_width = background.get_width()

  tiles = math.ceil(SCREEN_WIDTH / background_width) + 1
  scroll = 0

  # gravity
  flap_distance = 7
  jumping = False  

  show_downflap = True 

  pipe_image = py.image.load("assets/pipe-green.png")
  floor_image = py.image.load("assets/base.png")  

  running = True

  while running:
    clock.tick(FPS)

    for event in py.event.get():
      if event.type == py.QUIT:
        running = False   

    # draw scrolling background
    for i in range(0, tiles):
      screen.blit(background, (i * background_width + scroll, 0))

    # scroll background    
    scroll -= 3

    # reset scroll
    if abs(scroll) > background_width:
      scroll = 0

    pipe_timer += 1
    if pipe_timer > 90:
      pipe_y = random.randint(100, 300)
      pipes.append(Pipe(640, pipe_y, pipe_image))
      pipe_timer = 0

    for pipe in pipes[:]:
      pipe.update()
      pipe.draw(screen)
      if pipe.is_off_screen():
        pipes.remove(pipe)

    if show_downflap:
      screen.blit(down_surface, bird_rect)

    bird_rect.y += flap_distance

    keys_pressed = py.key.get_pressed()
    if keys_pressed[py.K_SPACE]:
      jumping = True

    if jumping:
      show_downflap = False
      bird_rect.y -= Y_VELOCITY
      Y_VELOCITY -= Y_GRAVITY
      if Y_VELOCITY < -JUMP_HEIGHT:
        jumping = False
        Y_VELOCITY = JUMP_HEIGHT
        show_downflap = True
      bird_rect = down_surface.get_rect(topleft=(bird_rect.x, bird_rect.y - JUMP_HEIGHT))
      screen.blit(jumping_surface, bird_rect)

    if bird_rect.top < 0:
      bird_rect.y = 0

    if bird_rect.y > 609 - bird_rect.height:
      bird_rect.y = 609 - bird_rect.height

    for pipe in pipes:
      if bird_rect.colliderect(pipe.top_rect) or bird_rect.colliderect(pipe.bottom_rect): 
        running = False 


    screen.blit(floor_image, (0, 609 ))

    py.display.update()

  py.quit()

if __name__ == "__main__":
  main()
