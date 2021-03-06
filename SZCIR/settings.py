import pygame as pg
vec = pg.math.Vector2


WIDTH = 400
HEIGHT = 400
FPS = 60
TITLE = "Platformer"

TILESIZE = 16
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

PLAYER_SPEED = 280
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'rogue.png'
DIED_IMG = 'died.jpg'
PLAYER_HIT_RECT = pg.Rect(0, 0, 46, 51)
BARREL_OFFSET = vec(30, 10)
