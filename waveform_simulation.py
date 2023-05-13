import pygame
import numpy as np
import random

h = 1        # spatial step width
k = 1        # time step width
dimx = 500   # width of the simulation domain
dimy = 500   # height of the simulation domain
cellsize = 2 # display size of a cell in pixel


def init_simulation():
    u = np.zeros((3, dimx, dimy))         # The three dimensional simulation grid 
    c = 0.5                               # The "original" wave propagation speed
    alpha = np.zeros((dimx, dimy))        # wave propagation velocities of the entire simulation domain
    alpha[0:dimx,0:dimy] = ((c*k) / h)**4 # will be set to a constant value of tau
    return u, alpha


def update(u, alpha):
    u[2] = u[1]
    u[1] = u[0]

    complex_form = False

    if complex_form:
        for c in range(1, dimx-1):
            for r in range(1, dimy-1):
                u[0, c, r]  = alpha[c,r] * (u[1, c-1, r] + u[1, c+1, r] + u[1, c, r-1] + u[1, c, r+1] - 4*u[1, c, r])
                u[0, c, r] += 2 * u[1, c, r] - u[2, c, r]
    else:
        u[0, 1:dimx-1, 1:dimy-1]  = alpha[1:dimx-1, 1:dimy-1] * (u[1, 0:dimx-2, 1:dimy-1] + 
                                            u[1, 2:dimx,   1:dimy-1] + 
                                            u[1, 1:dimx-1, 0:dimy-2] + 
                                            u[1, 1:dimx-1, 2:dimy] - 4*u[1, 1:dimx-1, 1:dimy-1]) \
                                        + 2 * u[1, 1:dimx-1, 1:dimy-1] - u[2, 1:dimx-1, 1:dimy-1]

    # Not part of the wave equation but need to remove energy from the system
    u[0, 1:dimx-1, 1:dimy-1] *= 0.995


def place_sound(u):
    if (random.random() < 0.02):
        x = 450
        y = 50
        u[0, x-2:x+2, y-2:y+2] = 120


def main():
    pygame.init()
    display = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("2d Wave Equation")

    u, alpha = init_simulation()
    pixeldata = np.zeros((dimx, dimy, 3), dtype=np.uint8 )
    i = 0

    while True:
        i += 1
        # Uncomment the following lines to save screenshots
        #fullpath = ".\\pygame\\ss%08d.png"%i
        #pygame.image.save(display, fullpath)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        place_sound(u)
        update(u, alpha)

        pixeldata[1:dimx, 1:dimy, 0] = np.clip(u[0, 1:dimx, 1:dimy] + 128, 0, 255)
        pixeldata[1:dimx, 1:dimy, 1] = np.clip(u[1, 1:dimx, 1:dimy] + 128, 0, 255)
        pixeldata[1:dimx, 1:dimy, 2] = np.clip(u[2, 1:dimx, 1:dimy] + 128, 0, 255)

        surf = pygame.surfarray.make_surface(pixeldata)
        display.blit(pygame.transform.scale(surf, (dimx * cellsize, dimy * cellsize)), (0, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()