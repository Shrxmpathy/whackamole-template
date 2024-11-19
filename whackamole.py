import pygame



def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            for i in range(1, 16):
                ##rows grid drawing
                pygame.draw.line(screen,
                                 (0, 0, 0),
                                 (0, i * 32),
                                 (640, i * 32),
                                 1

                                 )
            for i in range(1,20):
                #col grid drawing
                pygame.draw.line(screen,
                                 (0,0,0),
                                 (i*32, 0),
                                 (i*32, 640),
                                 1
                                 )
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
