import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *
from menu import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        self.size_screen = [400, 400]
        self.game_stack = [Menu(self)]
        self.pos_mouse = [0, 0]
        while self.game_stack:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
            self.dt = self.clock.tick(FPS) / 1000.0
            pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
            self.game_stack[-1].render(self.screen, self.size_screen)
            pg.display.flip()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.img_folder = path.join(game_folder, 'img')
        map_folder = path.join(game_folder, 'maps')
        self.mus_folder = path.join(game_folder, 'music')
        self.map = TiledMap(path.join(map_folder, 'level_1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.win_img = pg.image.load(path.join(self.img_folder, 'win.jpg'))
        self.died_img = pg.image.load(path.join(self.img_folder, DIED_IMG))
        self.died_img = pg.transform.scale(self.died_img, (400, 400))
        self.player_img_list = {}
        files = ["Walk", "Jump"]
        for file in files:
            files_1 = os.listdir(f"Graphics/Sprait/Rogue/{file}")
            self.player_img_list[file] = []
            for file_1 in files_1:
                image = pygame.image.load(f"Graphics/Sprait/Rogue/{file}/{file_1}").convert_alpha()
                self.player_img_list[file].append(image)
        self.player_img_list["None"] = [self.player_img_list["Walk"][0]]


    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Objects(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True
        pg.mixer_music.load(path.join(self.mus_folder, 'play.mp3'))
        pg.mixer.music.play()
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        if not die(self.player) and not win(self.player):
            self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
            for sprite in self.all_sprites:
                self.screen.blit(sprite.image, self.camera.apply(sprite))
        if win(self.player) and self.win_img != 'done':
            for opacity in range(255, 0, -15):
                pg.draw.rect(self.screen, (0, 0, 0, opacity), (0, 0, 400, 400))
                pg.time.delay(30)
                pg.display.flip()
            self.screen.blit(self.win_img, (0, 0))
            pg.mixer_music.load(path.join(self.mus_folder, 'win.mp3'))
            self.win_img = 'done'
            pg.mixer.music.play()
        if self.win_img == 'done':
            keys = pg.key.get_pressed()

            if keys[pg.K_RETURN]:
                self.win_img = pg.image.load(path.join(self.img_folder, 'win.jpg'))
                self.died_img = pg.image.load(path.join(self.img_folder, DIED_IMG))
                self.died_img = pg.transform.scale(self.died_img, (400, 400))
                g.new()
                g.run()

        if die(self.player) and self.died_img != 'done':
            for opacity in range(255, 0, -15):
                pg.draw.rect(self.screen, (0, 0, 0, opacity), (0, 0, 400, 400))
                pg.time.delay(30)
                pg.display.flip()
            self.screen.blit(self.died_img, (0, 0))
            pg.mixer_music.load(path.join(self.mus_folder, 'died.mp3'))
            self.died_img = 'done'
            pg.mixer.music.play()
        if self.died_img == 'done':
            keys = pg.key.get_pressed()

            if keys[pg.K_RETURN]:
                self.win_img = pg.image.load(path.join(self.img_folder, 'win.jpg'))
                self.died_img = pg.image.load(path.join(self.img_folder, DIED_IMG))
                self.died_img = pg.transform.scale(self.died_img, (400, 400))
                g.new()
                g.run()

        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()