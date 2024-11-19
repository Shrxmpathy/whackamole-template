import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_coord = (0,0)

        def create_grid():
            for i in range(1, 16):
                ##rows grid drawing
                pygame.draw.line(screen,
                                 (0, 0, 0),
                                 (0, i * 32),
                                 (640, i * 32),
                                 1

                                 )
            for i in range(1, 20):
                # col grid drawing
                pygame.draw.line(screen,
                                 (0, 0, 0),
                                 (i * 32, 0),
                                 (i * 32, 640),
                                 1
                                 )

        screen.fill("light green")
        create_grid()
        screen.blit(mole_image, mole_image.get_rect(topleft=((0), (0))))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    print(x//32, y//32)
                    mouse_pos = (x//32, y//32)
                    if mouse_pos == mole_coord:
                        screen.fill("light green")
                        create_grid()
                        pygame.display.flip()
                        rand_num1 = random.randrange(0, 640)
                        rand_num2 = random.randrange(0,480)
                        # screen.blit(mole_image, mole_image.get_rect(space =((rand_num1), (rand_num2))))



            mole_coord = (0,0)
            pygame.display.flip()

            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
