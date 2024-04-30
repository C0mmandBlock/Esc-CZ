import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("isometric game")

WHITE = (255, 255, 255)
GRAY = (127, 127, 127) #🇺🇸🦅

tile_width = 64
tile_height = 32

map_width = 10
map_height = 10

offsetX = 370
offsetY = 20

def iso_to_screen(pos):
    x = (pos[0]-pos[1]) * (tile_width/2)
    y = (pos[0]+pos[1]) * (tile_height/2)
    return (x+offsetX, y+offsetY)

def draw_tiles():
    for y in range(map_height):
        for x in range(map_width):
            iso_pos = (x, y)
            screen_pos = iso_to_screen(iso_pos)
            pygame.draw.polygon(screen, GRAY, [
                (screen_pos[0], screen_pos[1] + tile_height / 2),
                (screen_pos[0] + tile_width / 2, screen_pos[1]),
                (screen_pos[0] + tile_width, screen_pos[1] + tile_height / 2),
                (screen_pos[0] + tile_width / 2,screen_pos[1] + tile_height)
            ],2)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(WHITE)
        draw_tiles()
        pygame.display.flip()

if __name__ == "__main__":
    main()
