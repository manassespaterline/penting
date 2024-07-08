import pygame, sys
from pygame.locals import *
from config import *
import pygame_gui

from pygame_gui.elements import UIButton
from pygame_gui.windows import UIColourPickerDialog

pygame.init()

drawn_positions = []

font = pygame.font.SysFont('none', 24)
brushSize_txt = font.render("1        2        4       8      16      32      64", True, 'black')

pygame.mouse.set_visible(False)

draw_btn_y = 200
options_btn_y = 270
exit_btn_y = 340

up_anim_draw = False
down_anim_draw = False

up_anim_options = False
down_anim_options = False

up_anim_exit = False
down_anim_exit = False

def menu():

    global draw_btn_y
    global up_anim_draw
    global down_anim_draw

    global options_btn_y
    global up_anim_options
    global down_anim_options

    global exit_btn_y
    global up_anim_exit
    global down_anim_exit

    running_menu = True
    while running_menu:

        mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
        pointer_rect.center = (mouse_x + 10, mouse_y + 10)

        eraser_cursor_rect.center = (mouse_x + 10, mouse_y + 10)

        canvas.fill(bg_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if draw_rect.collidepoint(mouse_pos):
                        running_menu = False

                    if config_rect.collidepoint(mouse_pos):
                        pass

                    if exit_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

        draw_rect = pygame.Rect(300, draw_btn_y, 200, 50)
        pygame.draw.rect(canvas, 'white', draw_rect)
        canvas.blit(desenhar_btn, (300, draw_btn_y))

        config_rect = pygame.Rect(300, options_btn_y, 200, 50)
        pygame.draw.rect(canvas, 'white', config_rect)
        canvas.blit(opcoes_btn, (300, options_btn_y))

        exit_rect = pygame.Rect(300, exit_btn_y, 200, 50)
        pygame.draw.rect(canvas, 'white', exit_rect)
        canvas.blit(sair_btn, (300, exit_btn_y))


        if draw_rect.collidepoint(mouse_pos):
            if draw_btn_y == 200:
                up_anim_draw = True
                down_anim_draw= False
            if draw_btn_y == 210:
                up_anim_draw = False
                down_anim_draw = True
        else:
            draw_btn_y = 200
            up_anim_draw = False
            down_anim_draw = False

        if up_anim_draw:
            draw_btn_y += 0.5
        if down_anim_draw:
            draw_btn_y -= 0.5

        #---------------------------

        if config_rect.collidepoint(mouse_pos):
            if options_btn_y == 270:
                up_anim_options = True
                down_anim_options= False
            if options_btn_y == 280:
                up_anim_options = False
                down_anim_options = True
        else:
            options_btn_y = 270
            up_anim_options = False
            down_anim_options = False

        if up_anim_options:
            options_btn_y += 0.5
        if down_anim_options:
            options_btn_y -= 0.5

        #---------------------------

        if exit_rect.collidepoint(mouse_pos):
            if exit_btn_y == 340:
                up_anim_exit = True
                down_anim_exit= False
            if exit_btn_y == 350:
                up_anim_exit = False
                down_anim_exit = True
        else:
            exit_btn_y = 340
            up_anim_exit = False
            down_anim_exit = False

        if up_anim_exit:
            exit_btn_y += 0.5
        if down_anim_exit:
            exit_btn_y -= 0.5


        #Last thing that shoul be drawn.
        canvas.blit(pointer, pointer_rect)

        pygame.display.update()


def colorPicker():
    global brushColor
    global drawing
    global current_colour
    ui_manager = pygame_gui.UIManager((800, 600))
    #background = pygame.Surface((800, 600))
    #background.fill("#3a3b3c")

    colour_picker_button = UIButton(relative_rect=pygame.Rect(-700, -500, 30, 30),
                                #text='Pick Colour',
                                text='',
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

        mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
        pointer_rect.center = (mouse_x + 10, mouse_y + 10)

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

        canvas.blit(pointer, pointer_rect)

        pygame.display.update()


menu()

running = True
while running:

    canvas.fill(bg_color)
    mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
    pointer_rect.center = (mouse_x + 10, mouse_y + 10)

    eraser_cursor_rect.center = (mouse_x + 10, mouse_y + 10)

    tools = pygame.Rect(15, 60, 40, tools_height)
    tool_1 = pygame.Rect(tool1_x, tool1_y, tool_size, tool1_h)
    tool_2 = pygame.Rect(tool2_x, tool2_y, tool_size, tool2_h)
    tool_3 = pygame.Rect(20, 150, tool_size, tool3_h)
    tool_4 = pygame.Rect(20, 190, tool_size, tool4_h)


    square1 = pygame.Rect(60, 150, 30, 30)
    square2 = pygame.Rect(100, 150, 30, 30)
    square3 = pygame.Rect(140, 150, 30, 30)
    square4 = pygame.Rect(180, 150, 30, 30)
    square5 = pygame.Rect(220, 150, 30, 30)
    square6 = pygame.Rect(260, 150, 30, 30)
    square7 = pygame.Rect(300, 150, 30, 30)
    

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
                    eraser = False
                    colorPicker()
                if not eraser:
                    lastBrushColor = brushColor
                    if tool_2.collidepoint(mouse_pos):
                        eraser = True
                else:
                    if tool_2.collidepoint(mouse_pos):
                        eraser = False

                if not choose_brushsize:
                    if tool_3.collidepoint(mouse_pos):
                        choose_brushsize = True
                else:
                    if tool_3.collidepoint(mouse_pos):
                        choose_brushsize = False

                if choose_brushsize:
                    if square1.collidepoint(mouse_pos):
                        brushSize = 1
                    elif square2.collidepoint(mouse_pos):
                        brushSize = 2
                    elif square3.collidepoint(mouse_pos):
                        brushSize = 4
                    elif square4.collidepoint(mouse_pos):
                        brushSize = 8
                    elif square5.collidepoint(mouse_pos):
                        brushSize = 16
                    elif square6.collidepoint(mouse_pos):
                        brushSize = 32
                    elif square7.collidepoint(mouse_pos):
                        brushSize = 64


        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

    if drawing:
        drawn_positions.append(((mouse_x, mouse_y), brushColor, brushSize))

    # Desenhe todas as posições armazenadas
    for pos, color, size in drawn_positions:
        pygame.draw.circle(canvas, color, pos, size)

    #Open sidebar
    open_sidebar = pygame.Rect(15, 15, 40, 40)
    pygame.draw.rect(canvas, 'black', open_sidebar)
    canvas.blit(tools_icon, (15, 15))

    #Sidebar
    if sidebar:
        if tools_height < 400:
            tools_height += 10

        pygame.draw.rect(canvas, 'black', tools)
        canvas.blit(tools_bg, (15, 60))
        pygame.draw.rect(canvas, brushColor, tool_1)
        canvas.blit(icon1, (tool1_x, tool1_y))
        pygame.draw.rect(canvas, (100, 100, 100), tool_2)
        canvas.blit(eraser_icon, (tool2_x, tool2_y))
        pygame.draw.rect(canvas, (100, 100, 100), tool_3)
        pygame.draw.rect(canvas, (100, 100, 100), tool_4)

    elif not sidebar:
        if tools_height > 0:
            tools_height -= 10

            pygame.draw.rect(canvas, 'black', tools)
            pygame.draw.rect(canvas, (100, 100, 100), tool_1)
            canvas.blit(icon1, (tool1_x, tool1_y))
            pygame.draw.rect(canvas, (100, 100, 100), tool_2)
            canvas.blit(eraser_icon, (tool2_x, tool2_y))
            pygame.draw.rect(canvas, (100, 100, 100), tool_3)
            pygame.draw.rect(canvas, (100, 100, 100), tool_4)

            choose_brushsize = False

    if choose_brushsize:
        pygame.draw.rect(canvas, 'white', square1)
        pygame.draw.rect(canvas, 'white', square2)
        pygame.draw.rect(canvas, 'white', square3)
        pygame.draw.rect(canvas, 'white', square4)
        pygame.draw.rect(canvas, 'white', square5)
        pygame.draw.rect(canvas, 'white', square6)
        pygame.draw.rect(canvas, 'white', square7)
        canvas.blit(brushSize_txt, (70, 155))

    if eraser:
        brushColor = bg_color
    else:
        brushColor = lastBrushColor


    if not eraser:
        canvas.blit(pointer, pointer_rect)
    else:
        canvas.blit(eraser_cursor, eraser_cursor_rect)

    

    print(tools_bg_rect)

    pygame.display.update()