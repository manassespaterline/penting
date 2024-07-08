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

#Tool 1 - Paint brush color
tool1_h = 30
tool1_x = 20
tool1_y = 70

#Tool 2 - Eraser
tool2_h = 30
tool2_x = 20
tool2_y = 110

#Tool 3 - Paint brush size
tool3_h = 30
tool4_h = 30


#Eraser
eraser = False

choose_brushsize = False

### IMAGE IMPORT

#Icons
icon1 = pygame.image.load('assets/icons/brushcolor.png')
eraser_icon = pygame.image.load('assets/icons/eraser.png')

pointer = pygame.image.load('assets/icons/pointer.png')
pointer_rect = pointer.get_rect()

eraser_cursor = pygame.image.load('assets/icons/eraser_cursor.png')
eraser_cursor_rect = eraser_cursor.get_rect()

tools_icon = pygame.image.load('assets/icons/tools_icon.png')
tools_bg = pygame.image.load('assets/icons/tools_bg.png')
tools_bg_rect = tools_bg.get_rect()


# Buttons Icons

desenhar_btn = pygame.image.load('assets/buttons/desenhar_btn.png')
draw_btn = pygame.image.load('assets/buttons/draw_btn.png')

opcoes_btn = pygame.image.load('assets/buttons/opcoes_btn.png')
options_btn = pygame.image.load('assets/buttons/options_btn.png')

sair_btn = pygame.image.load('assets/buttons/sair_btn.png')
exit_btn = pygame.image.load('assets/buttons/exit_btn.png')