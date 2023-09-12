from random import randint
from sys import exit
import pygame
from pygame.locals import *

pygame.init()

# Setting things up
SCREEN_WIDTH = 600
SCREEN_HEIGHT = SCREEN_WIDTH
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

points = 0

rect_side = 25
speed = 25
x_snake = SCREEN_WIDTH // 2
y_snake = SCREEN_HEIGHT // 2

x_move = speed
y_move = 0

x_apple = randint(0,23) * 25
y_apple = randint(0,23) * 25

font_setup = pygame.font.SysFont('montserratregular', 40)

snake_positions = []
snake_length = 5

def growSnake(snake_positions):
  for position in snake_positions:
    pygame.draw.rect(screen, ("green"), (position[0], position[1], rect_side, rect_side))

def restart():
  global points, snake_length, x_snake, y_snake, snake_positions, snake_head, x_apple, y_apple, running, hit
  points = 0
  snake_length = 5
  x_snake = SCREEN_WIDTH // 2
  y_snake = SCREEN_HEIGHT // 2
  snake_positions = []
  snake_head = []
  x_apple = randint(0,23) * 25
  y_apple = randint(0,23) * 25
  running = True
  hit = False

while running:
  clock.tick(10) # Limit of FPS
  screen.fill((0,0,0)) # Clear the screen and filling the entire space with purple
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
  
    if event.type == KEYDOWN:
      if event.key == K_UP:
          if y_move == speed:
             pass
          else:
            y_move = -speed
            x_move = 0
      if event.key == K_DOWN:
          if y_move == -speed:
             pass
          else:
            y_move = speed 
            x_move = 0
      if event.key == K_LEFT:
          if x_move == speed:
             pass
          else:
            x_move = -speed
            y_move = 0
      if event.key == K_RIGHT:
          if x_move == -speed:
             pass
          else:
            x_move = speed
            y_move = 0

  x_snake = x_snake + x_move
  y_snake = y_snake + y_move


  snake = pygame.draw.rect(screen, ("green"), (x_snake,y_snake,rect_side, rect_side))
  apple = pygame.draw.rect(screen, ("red"), (x_apple,y_apple,rect_side, rect_side))

  if x_snake >= SCREEN_WIDTH:
     x_snake = 0
  if x_snake < 0:
     x_snake = SCREEN_WIDTH
  if y_snake >= SCREEN_HEIGHT:
     y_snake = 0
  if y_snake < 0:
     y_snake = SCREEN_HEIGHT

  if snake.colliderect(apple):
    x_apple = randint(0,23) * 25
    y_apple = randint(0,23) * 25
    points += 1
    snake_length += 1

  snake_head = []
  snake_head.append(x_snake)
  snake_head.append(y_snake)
  snake_positions.append(snake_head)

  text = font_setup.render("Points " + str(points), True, (255,255,255))
  
  if snake_positions.count(snake_head) > 1:
    game_over = font_setup.render("GAME OVER", True, (255,255,255))
    text_position = game_over.get_rect()
    
    hit = True
    while hit:
      screen.fill((0,0,0))

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          exit()
        if event.type == KEYDOWN:
            if event.key == K_r:
              restart()
      text_position.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
      screen.blit(game_over, text_position)
      pygame.display.update()

  if len(snake_positions) > snake_length:
    del snake_positions[0]

  growSnake(snake_positions)
  
  screen.blit(text, (400,0))

  pygame.display.update()

