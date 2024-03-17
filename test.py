from hokuyolx import HokuyoLX
import pygame
import numpy as np

DMAX = 10000
WIN_SIZE = (800, 600)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def update(laser, screen):
    timestamp, scan = laser.get_filtered_dist(dmax=DMAX)
    cartesian_points = []
    for r, theta in scan:
        x = int(r * np.cos(theta))
        y = int(r * np.sin(theta))
        cartesian_points.append((x, y))
    screen.fill(BLACK)
    pygame.draw.lines(screen, WHITE, True, cartesian_points, 1)
    pygame.display.flip()

def run():
    pygame.init()
    screen = pygame.display.set_mode(WIN_SIZE)
    laser = HokuyoLX()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        update(laser, screen)
        clock.tick(30)
    laser.close()
    pygame.quit()

if __name__ == '__main__':
    run()
