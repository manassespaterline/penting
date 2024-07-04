import pygame, sys
from pygame.locals import *
from config import *
import pygame_gui

from pygame_gui.elements import UIButton
from pygame_gui.windows import UIColourPickerDialog

pygame.init()

drawn_positions = []


def colorPicker():
    global brushColor
    global drawing
    ui_manager = pygame_gui.UIManager((800, 600))
    #background = pygame.Surface((800, 600))
    #background.fill("#3a3b3c")

    colour_picker_button = UIButton(relative_rect=pygame.Rect(-700, -500, 150, 30),
                                text='Pick Colour',
                                manager=ui_manager,
                                anchors={'left': 'right',
                                        'right': 'right',
                                        'top': 'bottom',
                                        'bottom': 'bottom'})
    colour_picker = None                                    
    current_colour = pygame.Color(0, 0, 0)
    #picked_colour_surface = pygame.Surface((400, 400))
    #picked_colour_surface.fill(current_colour)

    clock = pygame.time.Clock()

    running_colorpicker = True
    while running_colorpicker:
        time_delta = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == colour_picker_button:
                colour_picker = UIColourPickerDialog(pygame.Rect(160, 50, 420, 400),
                                                    ui_manager,
                                                    window_title="Change Colour...",
                                                    initial_colour=current_colour)
                colour_picker_button.disable()
            if event.type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED:
                current_colour = event.colour
                #picked_colour_surface.fill(current_colour)
                brushColor = current_colour
                drawing = False
                running_colorpicker = False
            if event.type == pygame_gui.UI_WINDOW_CLOSE:
                colour_picker_button.enable()
                colour_picker = None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    running_colorpicker = False
            
            ui_manager.process_events(event)
            
        ui_manager.update(time_delta)

        #canvas.blit(background, (0, 0))
        #canvas.blit(picked_colour_surface, (200, 100))

        ui_manager.draw_ui(canvas)

        pygame.display.update()


running = True
while running:

    canvas.fill(bg_color)
    mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()

    tools = pygame.Rect(15, 60, 40, tools_height)
    tool_1 = pygame.Rect(20, tool1_y, tool_size, tool1_h)
    tool_2 = pygame.Rect(20, 110, tool_size, tool2_h)
    tool_3 = pygame.Rect(20, 150, tool_size, tool3_h)
    tool_4 = pygame.Rect(20, 190, tool_size, tool4_h)

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
                    else:
                        sidebar = True

                 #Open color picker
                if tool_1.collidepoint(mouse_pos):
                    colorPicker()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

    if drawing:
        drawn_positions.append(((mouse_x, mouse_y), brushColor))

    # Desenhe todas as posições armazenadas
    for pos, color in drawn_positions:
        pygame.draw.circle(canvas, color, pos, 8)

    #Open sidebar
    open_sidebar = pygame.Rect(15, 15, 40, 40)
    pygame.draw.rect(canvas, 'black', open_sidebar)

    #Sidebar
    if sidebar:
        if tools_height < 400:
            tools_height += 10

        pygame.draw.rect(canvas, 'black', tools)
        pygame.draw.rect(canvas, (100, 100, 100), tool_1)
        pygame.draw.rect(canvas, (100, 100, 100), tool_2)
        pygame.draw.rect(canvas, (100, 100, 100), tool_3)
        pygame.draw.rect(canvas, (100, 100, 100), tool_4)

    elif not sidebar:
        if tools_height > 0:
            tools_height -= 10

            pygame.draw.rect(canvas, 'black', tools)
            pygame.draw.rect(canvas, (100, 100, 100), tool_1)
            pygame.draw.rect(canvas, (100, 100, 100), tool_2)
            pygame.draw.rect(canvas, (100, 100, 100), tool_3)
            pygame.draw.rect(canvas, (100, 100, 100), tool_4)

        

    print(tools_height)

    pygame.display.update()