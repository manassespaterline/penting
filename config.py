import pygame
pygame.init()

canvasSize = canvasWidth, canvasHeight = 720, 480
canvas = pygame.display.set_mode(canvasSize)

# Variables
bg_color = (48, 48, 48)
drawing = False

brushSize = 4
brushColor = ((255, 255, 255))
canvasColor = ((48, 48, 48))

sidebar = False
tools_height = 0
tool_size = 30


