import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("isometric game")

WHITE = (255, 255, 255)
GRAY = (127, 127, 127) #🇺🇸🦅
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

mapData = {
    "color": {(0,0): GRAY, (0,1): RED, (0,2): GRAY, (1,0): GRAY, (1,1): RED, (1,2): GRAY, (2,0): GRAY, (2,1): GRAY, (2,2): RED},
    "height": {(0,0): 0, (0,1): 0, (0,2): 0, (1,0): 0, (1,1): 0, (1,2): 0, (2,0): 0, (2,1): 0, (2,2): 0}
}

tile_width = 64*3
tile_height = 32*3

map_width = 1
map_height = 1

offsetX = 320
offsetY = 20

def iso_to_screen(pos):
    return ((pos[0]-pos[1]) * (tile_width/2) + offsetX, (pos[0]+pos[1]) * (tile_height/2) + offsetY)

def draw_tiles():
    for y in range(map_height):
        for x in range(map_width):
            iso_pos = (x, y)
            screen_pos = iso_to_screen(iso_pos)
            pygame.draw.polygon(screen, mapData["color"][(x,y)], [
                (screen_pos[0], screen_pos[1] + tile_height / 2),
                (screen_pos[0] + tile_width / 2, screen_pos[1]),
                (screen_pos[0] + tile_width, screen_pos[1] + tile_height / 2),
                (screen_pos[0] + tile_width / 2,screen_pos[1] + tile_height)
            ],2)

def main():
    clock = pygame.time.Clock()
    i = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(WHITE)
        draw_tiles()
        pygame.display.flip()
        clock.tick()
        if i%500==0:
            pygame.display.set_caption("isometric game " + str(int(clock.get_fps())) + " fps")
            i = 0
        i += 1

if __name__ == "__main__":
    main()
