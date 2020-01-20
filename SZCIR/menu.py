import pygame
from pygame.locals import *
import os

class Menu:
    def __init__(self, obj):
        self.main_object = obj
        # Здесь будут хранится загруженные спрайты (ключем будет название файла спрайта см Graphics)
        self.content = {}
        # Здесь координаты по которым нужно будет отрисовывать картинку
        self.coords_content = {}
        # Здесь будут прямоугольники (объекты Rect из pygame) нужны для проверки столкновений и тд
        self.coords_content_rect = {}
        self.load_content()
        self.is_click = None
        self.counter_frames = 0

    def load_content(self):
        files = os.listdir("Graphics/Menu/buttons")
        t = self.main_object.size_screen
        # Какая-то страшная дичь, вообщем тут подбирается "оптимальный" под размер окна, размер спрайта
        width = t[0] // 100 * 8
        height = t[1] // 100 * 8
        # Вообщем тут идет загрузка картинок, изменяется их размер, определяются координаты по которым
        # нужно будет расположить их ну и здесь же опрделяются прямоугольники
        for file in files:
            name = file[:-4]
            self.content[name] = []
            image = pygame.image.load("Graphics/Menu/buttons/" + file).convert_alpha()
            x, y = size = image.get_width(), image.get_height()
            image = pygame.transform.scale(image, (int(x / 100 * width), int(y / 100 * height)))
            self.content[name].append(image)
            file_1 = name + "_aiming.png"
            if os.path.exists("Graphics/Menu/buttons_aiming/" + file_1):
                image = pygame.image.load("Graphics/Menu/buttons_aiming/" + file_1).convert_alpha()
                image = pygame.transform.scale(image, (int(x / 100 * width), int(y / 100 * height)))
                self.content[name].append(image)
                file_2 = name + "_pressed.png"
                image = pygame.image.load("Graphics/Menu/buttons_pressed/" + file_2).convert_alpha()
                image = pygame.transform.scale(image, (int(x / 100 * width), int(y / 100 * height)))
                self.content[name].append(image)
            else:
                self.content[name].append(None)
                self.content[name].append(None)
        image = pygame.image.load("Graphics/Menu/background.png").convert_alpha()
        image = pygame.transform.scale(image, self.main_object.size_screen)
        self.content["background"] = image
        self.coords_content["start_game"] = (self.main_object.size_screen[0] // 2 - self.content["start_game"][0].get_width() // 2,
                                             self.main_object.size_screen[1] // 2 - self.content["start_game"][0].get_height() // 2 - self.main_object.size_screen[1] // 4)
        self.coords_content["settings"] = (self.main_object.size_screen[0] // 2 - self.content["settings"][0].get_width() // 2,
                                           self.main_object.size_screen[1] // 2 - self.content["settings"][0].get_height() // 2)
        self.coords_content["quit_game"] = (self.main_object.size_screen[0] // 2 - self.content["quit_game"][0].get_width() // 2,
                                            self.main_object.size_screen[1] // 2 - self.content["quit_game"][0].get_height() // 2 + self.main_object.size_screen[1] // 4)
        self.coords_content["singleplayer"] = (self.main_object.size_screen[0] // 2 - self.content["singleplayer"][0].get_width() // 2,
                                            self.main_object.size_screen[1] // 2 - self.content["singleplayer"][0].get_height() // 2 - self.main_object.size_screen[1] // 4)
        self.coords_content["multiplayer"] = (self.main_object.size_screen[0] // 2 - self.content["multiplayer"][0].get_width() // 2,
                                            self.main_object.size_screen[1] // 2 - self.content["multiplayer"][0].get_height() // 2)
        self.coords_content["back"] = (self.main_object.size_screen[0] // 2 - self.content["back"][0].get_width() // 2,
                                            self.main_object.size_screen[1] // 2 - self.content["back"][0].get_height() // 2 + self.main_object.size_screen[1] // 4)
        self.coords_content["create_server"] = (self.main_object.size_screen[0] // 2 - self.content["create_server"][0].get_width() // 2,
                                            self.main_object.size_screen[1] // 2 - self.content["create_server"][0].get_height() // 2 - self.main_object.size_screen[1] // 4)
        self.coords_content["connect"] = (self.main_object.size_screen[0] // 2 - self.content["connect"][0].get_width() // 2,
                                            self.main_object.size_screen[1] // 2 - self.content["connect"][0].get_height() // 2)
        self.coords_content["creating_server"] = (self.main_object.size_screen[0] // 2 - self.content["creating_server"][0].get_width() // 2,
                                            self.main_object.size_screen[1] // 2 - self.content["creating_server"][0].get_height() // 2 - self.main_object.size_screen[1] // 3)
        self.coords_content["enter_port"] = (self.main_object.size_screen[0] // 2 - self.content["enter_port"][0].get_width() // 2  - self.main_object.size_screen[0] // 4,
                                            self.main_object.size_screen[1] // 2 - self.content["enter_port"][0].get_height() // 2 - self.main_object.size_screen[0] // 9)
        self.coords_content["create_server_1"] = (self.main_object.size_screen[0] // 2 - self.content["create_server"][0].get_width() // 2,
                                            self.main_object.size_screen[1] // 2 - self.content["create_server"][0].get_height() // 2 + self.main_object.size_screen[1] // 4)
        self.coords_content["back_1"] = (self.main_object.size_screen[0] // 2 - self.content["back"][0].get_width() // 2 + self.main_object.size_screen[0] // 3,
                                            self.main_object.size_screen[1] // 2 - self.content["back"][0].get_height() // 2 + self.main_object.size_screen[1] // 3)
        self.coords_content["connecting"] = (self.main_object.size_screen[0] // 2 - self.content["connecting"][0].get_width() // 2,
                                            self.main_object.size_screen[1] // 2 - self.content["connecting"][0].get_height() // 2 - self.main_object.size_screen[1] // 3)
        self.coords_content["enter_ip"] = (self.main_object.size_screen[0] // 2 - self.content["enter_ip"][0].get_width() // 2 - self.main_object.size_screen[0] // 4,
                                            self.main_object.size_screen[1] // 2 - self.content["enter_ip"][0].get_height() // 2)
        self.coords_content["connect_1"] = (self.main_object.size_screen[0] // 2 - self.content["connect"][0].get_width() // 2,
                                            self.main_object.size_screen[1] // 2 - self.content["connect"][0].get_height() // 2 + self.main_object.size_screen[1] // 4)


        for key in self.coords_content.keys():
            try:
                self.coords_content_rect[key] = pygame.Rect([*self.coords_content[key]] + [self.content[key][0].get_width(), 
                                                                                         self.content[key][0].get_height()])
            except:
                pass

        self.coords_content_rect["create_server_1"] = pygame.Rect([*self.coords_content["create_server_1"]] + [self.content["create_server"][0].get_width(), 
                                                                                         self.content["create_server"][0].get_height()])
        self.coords_content_rect["back_1"] = pygame.Rect([*self.coords_content["back_1"]] + [self.content["back"][0].get_width(), 
                                                                                         self.content["back"][0].get_height()])
        self.coords_content_rect["connect_1"] = pygame.Rect([*self.coords_content["connect_1"]] + [self.content["connect"][0].get_width(), 
                                                                                         self.content["connect"][0].get_height()])

    def render(self, screen, size_screen):
        # Самое веселое
        # Здесь проверяется навелись ли мышкой на кнопку, если да, у кнопки меняется картинка
        # Также здесь проверяется нажатие на кнопку, если да, то в игровой стек добавляется нужный объект
        buttons = [0, 0, 0]
        if not self.is_click:
            if self.coords_content_rect["start_game"].collidepoint(self.main_object.pos_mouse):
                buttons[0] = 1
            elif self.coords_content_rect["settings"].collidepoint(self.main_object.pos_mouse):
                buttons[1] = 1
            elif self.coords_content_rect["quit_game"].collidepoint(self.main_object.pos_mouse):
                buttons[2] = 1
        else:
            buttons[self.is_click - 1] = 2
            self.counter_frames += 1

        if self.counter_frames == 10:
            if self.is_click == 1:
                self.main_object.game_stack.append(MenuSelectGameType(self))
                self.counter_frames = 0
                self.is_click = 0
            elif self.is_click == 3:
                self.main_object.running = False
            
        for event in pygame.event.get():
            if event.type == QUIT:
                self.main_object.running = False
            elif event.type == MOUSEMOTION:
                self.main_object.pos_mouse = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                if self.coords_content_rect["start_game"].collidepoint(event.pos):
                    buttons[0] = 2
                    self.is_click = 1
                elif self.coords_content_rect["settings"].collidepoint(event.pos):
                    buttons[1] = 2
                    self.is_click = 2
                elif self.coords_content_rect["quit_game"].collidepoint(event.pos):
                    buttons[2] = 2
                    self.is_click = 3

        screen.blit(self.content["background"], (0, 0))
        screen.blit(self.content["start_game"][buttons[0]], self.coords_content["start_game"])
        #screen.blit(self.content["settings"][buttons[1]], self.coords_content["settings"])
        screen.blit(self.content["quit_game"][buttons[2]], self.coords_content["quit_game"])

# Дальше все аналогично

class MenuSelectGameType:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.is_click = False
        self.counter_frames = 0

    def render(self, screen, size_screen):
        buttons = [0, 0, 0]
        if not self.is_click:
            if self.main_menu.coords_content_rect["singleplayer"].collidepoint(self.main_menu.main_object.pos_mouse):
                buttons[0] = 1
            elif self.main_menu.coords_content_rect["multiplayer"].collidepoint(self.main_menu.main_object.pos_mouse):
                buttons[1] = 1
            elif self.main_menu.coords_content_rect["back"].collidepoint(self.main_menu.main_object.pos_mouse):
                buttons[2] = 1
        else:
            buttons[self.is_click - 1] = 2
            self.counter_frames += 1

        if self.counter_frames == 10:
            if self.is_click == 3:
                del self.main_menu.main_object.game_stack[-1]
            elif self.is_click == 2:
                self.main_menu.main_object.game_stack.append(MenuSelectMultiplayerType(self.main_menu))
                self.counter_frames = 0
                self.is_click = 0
            elif self.is_click == 1:
                self.main_menu.main_object.game_stack.clear()
                self.counter_frames = 0
                self.is_click = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                self.main_menu.main_object.running = False
            elif event.type == MOUSEMOTION:
                self.main_menu.main_object.pos_mouse = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                if self.main_menu.coords_content_rect["singleplayer"].collidepoint(event.pos):
                    buttons[0] = 2
                    self.is_click = 1
                elif self.main_menu.coords_content_rect["multiplayer"].collidepoint(event.pos):
                    buttons[1] = 2
                    self.is_click = 2
                elif self.main_menu.coords_content_rect["back"].collidepoint(event.pos):
                    buttons[2] = 2
                    self.is_click = 3

        screen.blit(self.main_menu.content["background"], (0, 0))
        screen.blit(self.main_menu.content["singleplayer"][buttons[0]], self.main_menu.coords_content["singleplayer"])
        #screen.blit(self.main_menu.content["multiplayer"][buttons[1]], self.main_menu.coords_content["multiplayer"])
        screen.blit(self.main_menu.content["back"][buttons[2]], self.main_menu.coords_content["back"])
        

class MenuSelectMultiplayerType:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.is_click = False
        self.counter_frames = 0

    def render(self, screen, size_screen):
        buttons = [0, 0, 0]
        if not self.is_click:
            if self.main_menu.coords_content_rect["create_server"].collidepoint(self.main_menu.main_object.pos_mouse):
                buttons[0] = 1
            elif self.main_menu.coords_content_rect["connect"].collidepoint(self.main_menu.main_object.pos_mouse):
                buttons[1] = 1
            elif self.main_menu.coords_content_rect["back"].collidepoint(self.main_menu.main_object.pos_mouse):
                buttons[2] = 1
        else:
            buttons[self.is_click - 1] = 2
            self.counter_frames += 1

        if self.counter_frames == 10:
            if self.is_click == 3:
                del self.main_menu.main_object.game_stack[-1]
                self.counter_frames = 0
                self.is_click = 0
            elif self.is_click == 1:
                self.main_menu.main_object.game_stack.append(MenuCreateServer(self.main_menu))
                self.counter_frames = 0
                self.is_click = 0
            elif self.is_click == 2:
                self.main_menu.main_object.game_stack.append(MenuConnectServer(self.main_menu))
                self.counter_frames = 0
                self.is_click = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                self.main_menu.main_object.running = False
            elif event.type == MOUSEMOTION:
                self.main_menu.main_object.pos_mouse = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                if self.main_menu.coords_content_rect["create_server"].collidepoint(event.pos):
                    buttons[0] = 2
                    self.is_click = 1
                elif self.main_menu.coords_content_rect["connect"].collidepoint(event.pos):
                    buttons[1] = 2
                    self.is_click = 2
                elif self.main_menu.coords_content_rect["back"].collidepoint(event.pos):
                    buttons[2] = 2
                    self.is_click = 3

        screen.blit(self.main_menu.content["background"], (0, 0))
        screen.blit(self.main_menu.content["create_server"][buttons[0]], self.main_menu.coords_content["create_server"])
        screen.blit(self.main_menu.content["connect"][buttons[1]], self.main_menu.coords_content["connect"])
        screen.blit(self.main_menu.content["back"][buttons[2]], self.main_menu.coords_content["back"])


class MenuCreateServer:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.is_click = False
        self.counter_frames = 0
        self.color_inactive = pygame.Color(70, 70, 70)
        self.color_active = pygame.Color('black')
        self.color = self.color_inactive
        self.active = False
        self.port = ""
        self.font = pygame.font.Font("Fonts/gothic_font.ttf", 32)
        self.coords_port = (self.main_menu.main_object.size_screen[0] // 2,
                            self.main_menu.main_object.size_screen[1] // 2 - self.main_menu.main_object.size_screen[1] // 13)
        self.input_box = pygame.Rect(self.coords_port[0], 
                                     self.coords_port[1] - self.main_menu.main_object.size_screen[1] // 8, 
                                     self.main_menu.main_object.size_screen[0] // 7, 
                                     self.main_menu.main_object.size_screen[1] // 15)


    def render(self, screen, size_screen):
        buttons = [0, 0]
        if not self.is_click:
            if self.main_menu.coords_content_rect["create_server_1"].collidepoint(self.main_menu.main_object.pos_mouse):
                buttons[0] = 1
            elif self.main_menu.coords_content_rect["back_1"].collidepoint(self.main_menu.main_object.pos_mouse):
                buttons[1] = 1
                self.counter_frames = 0
                self.is_click = 0
        else:
            buttons[self.is_click - 1] = 2
            self.counter_frames += 1

        if self.counter_frames == 10:
            if self.is_click == 2:
                del self.main_menu.main_object.game_stack[-1]
            elif self.is_click == 1:
                #self.main_menu.main_object.game_stack.append(MenuCreateServer(self.main_menu))
                pass

        for event in pygame.event.get():
            if event.type == QUIT:
                self.main_menu.main_object.running = False
            elif event.type == MOUSEMOTION:
                self.main_menu.main_object.pos_mouse = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                if self.main_menu.coords_content_rect["create_server_1"].collidepoint(event.pos):
                    buttons[0] = 2
                    self.is_click = 1
                elif self.main_menu.coords_content_rect["back_1"].collidepoint(event.pos):
                    buttons[1] = 2
                    self.is_click = 2

                if self.input_box.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
                self.color = self.color_active if self.active else self.color_inactive
            elif event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == K_RETURN:
                        print(self.port)
                        self.port = ''
                    elif event.key == K_BACKSPACE:
                        self.port = self.port[:-1]
                    else:
                        if event.unicode in "0123456789" and len(self.port) <= 4:
                            self.port += event.unicode

        screen.blit(self.main_menu.content["background"], (0, 0))

        txt_surface = self.font.render(self.port, True, self.color)
        screen.blit(txt_surface, (self.input_box.x, self.input_box.y))
        #pygame.draw.rect(screen, self.color, self.input_box, 2)
        pygame.draw.line(screen, self.color, (self.coords_port[0], self.input_box.y + self.main_menu.main_object.size_screen[1] // 20), 
                                             (self.coords_port[0] + self.main_menu.main_object.size_screen[0] // 6, self.input_box.y + self.main_menu.main_object.size_screen[1] // 20), 4)

        
        screen.blit(self.main_menu.content["creating_server"][0], self.main_menu.coords_content["creating_server"])
        screen.blit(self.main_menu.content["enter_port"][0], self.main_menu.coords_content["enter_port"])
        screen.blit(self.main_menu.content["back"][buttons[1]], self.main_menu.coords_content["back_1"])
        screen.blit(self.main_menu.content["create_server"][buttons[0]], self.main_menu.coords_content["create_server_1"])


class MenuConnectServer:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.is_click = False
        self.counter_frames = 0
        self.color_inactive = pygame.Color(70, 70, 70)
        self.color_active = pygame.Color('black')
        self.color = self.color_inactive
        self.color_ip = self.color_inactive
        self.active = False
        self.active_1 = False
        self.port = ""
        self.ip_adres = ""
        self.font = pygame.font.Font("Fonts/gothic_font.ttf", 32)
        self.coords_port = (self.main_menu.main_object.size_screen[0] // 2,
                            self.main_menu.main_object.size_screen[1] // 2 - self.main_menu.main_object.size_screen[1] // 13)
        self.coords_ip = (self.main_menu.main_object.size_screen[0] // 2,
                            self.main_menu.main_object.size_screen[1] // 2 + self.main_menu.main_object.size_screen[1] // 12)
        self.input_box = pygame.Rect(self.coords_port[0], 
                                     self.coords_port[1] - self.main_menu.main_object.size_screen[1] // 8, 
                                     self.main_menu.main_object.size_screen[0] // 7, 
                                     self.main_menu.main_object.size_screen[1] // 15)
        self.input_box_1 = pygame.Rect(self.coords_ip[0], 
                                     self.coords_ip[1] - self.main_menu.main_object.size_screen[1] // 8, 
                                     self.main_menu.main_object.size_screen[0] // 3, 
                                     self.main_menu.main_object.size_screen[1] // 15)

    def render(self, screen, size_screen):
        buttons = [0, 0]
        if not self.is_click:
            if self.main_menu.coords_content_rect["create_server_1"].collidepoint(self.main_menu.main_object.pos_mouse):
                buttons[0] = 1
            elif self.main_menu.coords_content_rect["back_1"].collidepoint(self.main_menu.main_object.pos_mouse):
                buttons[1] = 1
                self.counter_frames = 0
                self.is_click = 0
        else:
            buttons[self.is_click - 1] = 2
            self.counter_frames += 1

        if self.counter_frames == 10:
            if self.is_click == 2:
                del self.main_menu.main_object.game_stack[-1]
            elif self.is_click == 1:
                #self.main_menu.main_object.game_stack.append(MenuCreateServer(self.main_menu))
                pass

        for event in pygame.event.get():
            if event.type == QUIT:
                self.main_menu.main_object.running = False
            elif event.type == MOUSEMOTION:
                self.main_menu.main_object.pos_mouse = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                if self.main_menu.coords_content_rect["create_server_1"].collidepoint(event.pos):
                    buttons[0] = 2
                    self.is_click = 1
                elif self.main_menu.coords_content_rect["back_1"].collidepoint(event.pos):
                    buttons[1] = 2
                    self.is_click = 2

                if self.input_box.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
                self.color = self.color_active if self.active else self.color_inactive

                if self.input_box_1.collidepoint(event.pos):
                    self.active_1 = not self.active_1
                else:
                    self.active_1 = False
                self.color_ip = self.color_active if self.active_1 else self.color_inactive

            elif event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == K_BACKSPACE:
                        self.port = self.port[:-1]
                    else:
                        if event.unicode in "0123456789" and len(self.port) <= 4:
                            self.port += event.unicode
                if self.active_1:
                    if event.key == K_BACKSPACE:
                        self.ip_adres = self.ip_adres[:-1]
                    else:
                        if event.unicode in "0123456789.":
                            self.ip_adres += event.unicode

        screen.blit(self.main_menu.content["background"], (0, 0))

        txt_surface = self.font.render(self.port, True, self.color)
        screen.blit(txt_surface, (self.input_box.x, self.input_box.y))

        txt_surface = self.font.render(self.ip_adres, True, self.color_ip)
        screen.blit(txt_surface, (self.input_box_1.x, self.input_box_1.y))
        #pygame.draw.rect(screen, self.color, self.input_box_1, 2)
        pygame.draw.line(screen, self.color, (self.coords_port[0], self.input_box.y + self.main_menu.main_object.size_screen[1] // 20), 
                                             (self.coords_port[0] + self.main_menu.main_object.size_screen[0] // 6, self.input_box.y + self.main_menu.main_object.size_screen[1] // 20), 4)
        pygame.draw.line(screen, self.color_ip, (self.coords_ip[0], self.input_box_1.y + self.main_menu.main_object.size_screen[1] // 20), 
                                             (self.coords_ip[0] + self.main_menu.main_object.size_screen[0] // 3, self.input_box_1.y + self.main_menu.main_object.size_screen[1] // 20), 4)
        
        screen.blit(self.main_menu.content["connecting"][0], self.main_menu.coords_content["connecting"])
        screen.blit(self.main_menu.content["enter_port"][0], self.main_menu.coords_content["enter_port"])
        screen.blit(self.main_menu.content["enter_ip"][0], self.main_menu.coords_content["enter_ip"])
        screen.blit(self.main_menu.content["back"][buttons[1]], self.main_menu.coords_content["back_1"])
        screen.blit(self.main_menu.content["connect"][buttons[0]], self.main_menu.coords_content["connect_1"])


class MenuSettings:
    def __init__(self, main_menu):
        self.main_menu = main_menu