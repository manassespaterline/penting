import pygame, sys
from pygame.locals import *
from config import *

pygame.init()

canvas.fill(bg_color)

running = True
while running:

    mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True

                if open_sidebar.collidepoint(mouse_pos):
                    if sidebar:
                        sidebar = False
                        canvas.fill(bg_color)
                    else:
                        sidebar = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

    if drawing:
        pygame.draw.circle(canvas, 'white', (mouse_x, mouse_y), 8)
        print('drawing')
    else:
        print("not drawing")

    #Open sidebar
    open_sidebar = pygame.Rect(15, 15, 40, 40)
    pygame.draw.rect(canvas, 'black', open_sidebar)

    #Sidebar
    if sidebar:
        if tools_height < 400:
            tools_height += 10

        tools = pygame.Rect(15, 60, 40, tools_height)
        pygame.draw.rect(canvas, 'black', tools)

        tool_1 = pygame.Rect(20, 70, tool_size, tool_size)
        pygame.draw.rect(canvas, (100, 100, 100), tool_1)

        tool_2 = pygame.Rect(20, 110, tool_size, tool_size)
        pygame.draw.rect(canvas, (100, 100, 100), tool_2)

        tool_3 = pygame.Rect(20, 150, tool_size, tool_size)
        pygame.draw.rect(canvas, (100, 100, 100), tool_3)

        tool_4 = pygame.Rect(20, 190, tool_size, tool_size)
        pygame.draw.rect(canvas, (100, 100, 100), tool_4)
    else:
        tools_height = 0

    pygame.display.update()