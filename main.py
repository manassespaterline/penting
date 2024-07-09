import pygame, sys
from pygame.locals import *
from config import *
import pygame_gui

from pygame_gui.elements import UIButton
from pygame_gui.windows import UIColourPickerDialog

pygame.init()

drawn_positions = []

titleFont = pygame.font.Font('assets/fonts/This Cafe.otf', 38)
normalFont = pygame.font.Font('assets/fonts/Happy Memories.otf', 24)
creditFont = pygame.font.SysFont('none', 20)

brushSize_txt = titleFont.render("1        2        4       8      16      32      64", True, 'black')

pygame.mouse.set_visible(False)

# Languages
portugues = True
english = False

def menu():

    draw_btn_y = 250
    options_btn_y = 320
    exit_btn_y = 390

    up_anim_draw = False
    down_anim_draw = False

    up_anim_options = False
    down_anim_options = False

    up_anim_exit = False
    down_anim_exit = False

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
                        options()

                    if exit_rect.collidepoint(mouse_pos):
                        confirm_exit()

        # Logo
        #pygame.draw.rect(canvas, 'white', (250, 50, 300, 200))
        canvas.blit(logo, (250, 50))

        draw_rect = pygame.Rect(300, draw_btn_y, 200, 50)
        pygame.draw.rect(canvas, 'white', draw_rect)
        if portugues:
            canvas.blit(desenhar_btn, (300, draw_btn_y))
        if english:
            canvas.blit(draw_btn, (300, draw_btn_y))

        config_rect = pygame.Rect(300, options_btn_y, 200, 50)
        pygame.draw.rect(canvas, 'white', config_rect)
        if portugues:
            canvas.blit(opcoes_btn, (300, options_btn_y))
        if english:
            canvas.blit(options_btn, (300, options_btn_y))

        exit_rect = pygame.Rect(300, exit_btn_y, 200, 50)
        pygame.draw.rect(canvas, 'white', exit_rect)
        if portugues:
            canvas.blit(sair_btn, (300, exit_btn_y))
        if english:
            canvas.blit(exit_btn, (300, exit_btn_y))


        if draw_rect.collidepoint(mouse_pos):
            if draw_btn_y == 250:
                up_anim_draw = True
                down_anim_draw= False
            if draw_btn_y == 260:
                up_anim_draw = False
                down_anim_draw = True
        else:
            draw_btn_y = 250
            up_anim_draw = False
            down_anim_draw = False

        if up_anim_draw:
            draw_btn_y += 0.5
        if down_anim_draw:
            draw_btn_y -= 0.5

        #---------------------------

        if config_rect.collidepoint(mouse_pos):
            if options_btn_y == 320:
                up_anim_options = True
                down_anim_options= False
            if options_btn_y == 330:
                up_anim_options = False
                down_anim_options = True
        else:
            options_btn_y = 320
            up_anim_options = False
            down_anim_options = False

        if up_anim_options:
            options_btn_y += 0.5
        if down_anim_options:
            options_btn_y -= 0.5

        #---------------------------

        if exit_rect.collidepoint(mouse_pos):
            if exit_btn_y == 390:
                up_anim_exit = True
                down_anim_exit= False
            if exit_btn_y == 400:
                up_anim_exit = False
                down_anim_exit = True
        else:
            exit_btn_y = 390
            up_anim_exit = False
            down_anim_exit = False

        if up_anim_exit:
            exit_btn_y += 0.5
        if down_anim_exit:
            exit_btn_y -= 0.5

        print(draw_btn_y, options_btn_y, exit_btn_y)


        credits = creditFont.render("Made by Manassés, 2024", True, 'black')
        canvas.blit(credits, (321, 570))

        #Last thing that shoul be drawn.
        canvas.blit(pointer, pointer_rect)

        pygame.display.update()


def options():

    global portugues
    global english

    #Pt-br
    opcoes_title = titleFont.render("Opcoes", True, 'white')
    linguagem_txt = normalFont.render("Idioma", True, 'white')

    #En
    options_title = titleFont.render("Options", True, 'white')
    language_txt = normalFont.render("Language", True, 'white')

    running_options = True
    while running_options:

        mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
        pointer_rect.center = (mouse_x + 10, mouse_y + 10)

        eraser_cursor_rect.center = (mouse_x + 10, mouse_y + 10)

        canvas.fill(bg_color)
        if portugues:
            canvas.blit(opcoes_title, (340, 60))
            canvas.blit(linguagem_txt, (80, 140))
        if english:
            canvas.blit(options_title, (340, 60))
            canvas.blit(language_txt, (80, 140))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running_options = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if brasil_rect.collidepoint(mouse_pos):
                        portugues = True
                        english = False
                    if usa_rect.collidepoint(mouse_pos):
                        portugues = False
                        english = True

        brasil_rect = pygame.Rect(80, 200, 100, 50)
        usa_rect = pygame.Rect(200, 200, 100, 50)
        pygame.draw.rect(canvas, 'green', brasil_rect)
        if portugues:
            pygame.draw.rect(canvas, 'black', (78, 198, 104, 54), 2)
        canvas.blit(brasil_flag, (80, 200))
        

        pygame.draw.rect(canvas, 'blue', usa_rect)
        if english:
            pygame.draw.rect(canvas, 'black', (198, 198, 104, 54), 2)
        canvas.blit(usa_flag, (200, 200))


        #Last thing that shoul be drawn.
        canvas.blit(pointer, pointer_rect)

        pygame.display.update()

def confirm_exit():
    running_confirm_exit = True
    while running_confirm_exit:

        canvas.fill(bg_color)

        mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
        pointer_rect.center = (mouse_x + 10, mouse_y + 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running_confirm_exit = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if yes_btn_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
                    if no_btn_rect.collidepoint(mouse_pos):
                        running_confirm_exit = False

        confirm_exit_rect = pygame.Rect(270, 60, 300, 450)
        pygame.draw.rect(canvas, 'white', confirm_exit_rect)
        canvas.blit(confirmation_img, (270, 60))

        confirmar_saida_txt = normalFont.render("Deseja sair?", True, 'yellow')
        confirm_exit_txt = normalFont.render("Wanna leave?", True, 'yellow')
        if portugues:
            canvas.blit(confirmar_saida_txt, (370, 340))
        if english:
            canvas.blit(confirm_exit_txt, (360, 340))

        yes_btn_rect = pygame.Rect(310, 400, 100, 50)
        pygame.draw.rect(canvas, (29, 21, 59), yes_btn_rect)
        no_btn_rect = pygame.Rect(430, 400, 100, 50)
        pygame.draw.rect(canvas, (29, 21, 59), no_btn_rect)

        sim_txt = normalFont.render("Sim", True, 'yellow')
        nao_txt = normalFont.render("Não", True, 'yellow')

        yes_txt = normalFont.render("Yes", True, 'yellow')
        no_txt = normalFont.render("No", True, 'yellow')

        if portugues:
            canvas.blit(sim_txt, (343, 412))
            canvas.blit(nao_txt, (463, 412))
        if english:
            canvas.blit(yes_txt, (343, 412))
            canvas.blit(no_txt, (470, 412))



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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu()

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