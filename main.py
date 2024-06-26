import pygame as pg
import sys

pg.init()
screen_width, screen_height = 800, 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("isometric game")

WHITE = (255, 255, 255)
GRAY = (127, 127, 127) #🇺🇸🦅
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

mapData = {
    "color1": {(0,0): GRAY, (0,1): GRAY, (0,2): GRAY, (1,0): GRAY, (1,1): GRAY, (1,2): GRAY, (2,0): GRAY, (2,1): GRAY, (2,2): GRAY},
    "color2": {(0,0): RED, (0,1): RED, (0,2): RED, (1,0): RED, (1,1): RED, (1,2): RED, (2,0): RED, (2,1): RED, (2,2): RED},
    "color3": {(0,0): GREEN, (0,1): GREEN, (0,2): GREEN, (1,0): GREEN, (1,1): GREEN, (1,2): GREEN, (2,0): GREEN, (2,1): GREEN, (2,2): GREEN},
    "height": {(0,0): 0, (0,1): 0, (0,2): 0, (1,0): 0, (1,1): 0, (1,2): 0, (2,0): 0, (2,1): 0, (2,2): 0}
}

tile_width, tile_height = 64*3, 32*3

map_width, map_height = 1, 1

offsetX, offsetY = 320, 20

def iso_to_screen(pos):
    return ((pos[0]-pos[1]) * (tile_width/2) + offsetX, (pos[0]+pos[1]) * (tile_height/2) + offsetY)

def draw_tiles():
    for y in range(map_height):
        for x in range(map_width):
            iso_pos = (x, y)
            screen_pos = iso_to_screen(iso_pos)
            bottom,center,top_right,bottom_right,top_left,bottom_left,top = (screen_pos[0]+tile_width/2,screen_pos[1]+tile_height*2),(screen_pos[0]+tile_width/2,screen_pos[1]+tile_height),(screen_pos[0]+tile_width,screen_pos[1]+tile_height/2),(screen_pos[0]+tile_width,screen_pos[1]+tile_height*1.5),(screen_pos[0],screen_pos[1]+tile_height/2),(screen_pos[0],screen_pos[1]+tile_height*1.5),(screen_pos[0]+tile_width/2,screen_pos[1])
            pg.draw.polygon(screen, mapData["color1"][(x,y)], [top_left, top, top_right, center])
            pg.draw.polygon(screen, mapData["color2"][(x,y)], [center, bottom, bottom_left, top_left])
            pg.draw.polygon(screen, mapData["color3"][(x,y)], [center, bottom, bottom_right, top_right])
            pg.draw.line(screen, BLACK, bottom, center, 2)
            pg.draw.line(screen, BLACK, bottom, bottom_left, 2)
            pg.draw.line(screen, BLACK, bottom, bottom_right, 2)
            pg.draw.line(screen, BLACK, center, top_right, 2)
            pg.draw.line(screen, BLACK, top_left, top, 2)
            pg.draw.line(screen, BLACK, top, top_right, 2)
            pg.draw.line(screen, BLACK, top_left, bottom_left, 2)
            pg.draw.line(screen, BLACK, top_left, center, 2)
            pg.draw.line(screen, BLACK, bottom_right, top_right, 2)

def main():
    clock = pg.time.Clock()
    i = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        screen.fill(WHITE)
        draw_tiles()
        pg.display.flip()
        clock.tick()
        if i%500==0:
            pg.display.set_caption("isometric game " + str(int(clock.get_fps())) + " fps")
            i = 0
        i += 1

if __name__ == "__main__": main()
