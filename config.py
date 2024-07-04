import pygame
pygame.init()

canvasSize = canvasWidth, canvasHeight = 800, 600
canvas = pygame.display.set_mode(canvasSize)
pygame.display.set_caption("Penting")

# Variables
bg_color = (48, 48, 48)
drawing = False

brushSize = 8
brushColor = (255, 255, 255)
lastBrushColor = (255, 255, 255)
canvasColor = ((48, 48, 48))

sidebar = False
tools_height = 0
tool_size = 30

tool1_h = 30
tool1_y = 70


tool2_h = 30
tool3_h = 30
tool4_h = 30


#Eraser
eraser = False



choose_brushsize = False

