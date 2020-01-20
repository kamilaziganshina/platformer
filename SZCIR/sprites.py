import pygame as pg
from random import uniform
from settings import *
from tilemap import collide_hit_rect
vec = pg.math.Vector2


jump = False


def die(sprite):
    if sprite.hit_rect.centery >= 470:
        return True
    else:
        return False


def win(sprite):
    if sprite.hit_rect.centerx >= 5776:
        return True
    else:
        return False


def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.x == sprite.hit_rect.x + sprite.hit_rect.w:
                sprite.pos.x = hits[0].rect.left
                sprite.vel.x = 0
                sprite.hit_rect.centerx = sprite.pos.x
                return True
            if hits[0].rect.x + hits[0].rect.w == sprite.hit_rect.x:
                sprite.pos.x = hits[0].rect.right
                sprite.vel.x = 0
                sprite.hit_rect.centerx = sprite.pos.x
                return True

        else:
            return False
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if not jump:
                sprite.pos.y = hits[0].rect.top
                return True
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y
    return False


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        global onground
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.player_img_list = game.player_img_list
        self.image = self.player_img_list["Walk"][0]
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.xvel = 0
        self.left = False
        self.right = False
        self.rect = pg.Rect(x, y, 46, 51)  # прямоугольный объект
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot = 0
        self.is_jump = False
        self.cof_jump = 10
        self.onground = True
        self.number_anim = 0
        self.counter = 0
        self.type_anim = ["None", "R"]
        collide_with_walls(self, self.game.walls, 'y')

    def get_keys(self):
        global jump

        jump = self.is_jump
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        check_move = None
        collide_with_walls(self, self.game.walls, 'y')
        if not self.onground:
            self.vel = vec(0, 300).rotate(-self.rot)

        if not collide_with_walls(self, self.game.walls, 'x') and (keys[pg.K_RIGHT] or keys[pg.K_d]):
            self.onground = collide_with_walls(self, self.game.walls, 'y')
            if self.onground or self.is_jump:
                self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
                check_move = PLAYER_SPEED
        if not collide_with_walls(self, self.game.walls, 'x') and (keys[pg.K_LEFT] or keys[pg.K_a]):
            self.onground = collide_with_walls(self, self.game.walls, 'y')
            if self.onground or self.is_jump:
                self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)
                check_move = -PLAYER_SPEED
        if keys[pg.K_SPACE] or keys[pg.K_UP] or keys[pg.K_w]:
            self.onground = collide_with_walls(self, self.game.walls, 'y')
            if not self.is_jump and self.onground:
                self.is_jump = True
                self.cof_jump = 16
                self.onground = False

        if self.is_jump:
            if self.cof_jump >= -16:
                if check_move:
                    self.vel = vec(check_move, -(self.cof_jump ** 3) // 2).rotate(-self.rot)
                else:
                    self.vel = vec(0, -(self.cof_jump ** 3) // 2).rotate(-self.rot)
            else:
                self.is_jump = False
                self.type_anim = ["None", self.type_anim[1]]
                self.number_anim = 0
            self.cof_jump -= 1
            self.onground = collide_with_walls(self, self.game.walls, 'y')
        
        if (keys[pg.K_SPACE] or keys[pg.K_w] or keys[pg.K_UP]):
            self.type_anim[0] = "Jump"

        elif (keys[pg.K_RIGHT] or keys[pg.K_d]) and self.type_anim[0] != "Jump":
            self.type_anim[0] = 'Walk'
            self.type_anim[1] = 'R'
        
        elif (keys[pg.K_LEFT] or keys[pg.K_a]) and self.type_anim[0] != "Jump":
            self.type_anim[0] = 'Walk'
            self.type_anim[1] = 'L'
        
        else:
            self.type_anim[0] = 'None'
            self.number_anim = 0
        
    def update(self):
        self.get_keys()

        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        if self.counter > 4:
            self.number_anim = (self.number_anim + 1) % len(self.player_img_list[self.type_anim[0]])
            self.counter = 0
        self.counter += 1
        if self.type_anim[1] == "L":
                self.image = pg.transform.flip(pg.transform.rotate(self.player_img_list[self.type_anim[0]][self.number_anim], self.rot), True, False)
        else:
            self.image = pg.transform.rotate(self.player_img_list[self.type_anim[0]][self.number_anim], self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        if not collide_with_walls(self, self.game.walls, 'x'):
            self.hit_rect.centerx = self.pos.x
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center


def moveRight(self):
    self.x = self.x + self.speed


def moveLeft(self):
    self.x = self.x - self.speed


class Objects(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.rect.w = w
        self.rect.h = h