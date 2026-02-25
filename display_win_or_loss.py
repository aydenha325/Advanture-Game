import time
import pygame


def display_win_screen(file):
    """
    Since there are two 'The End' screens, this function get file name parameter as string
    """
    pygame.init()

    pygame.display.set_caption('The End')

    # this is the point where parameter is used for calling the files
    endscreen = pygame.image.load(file)
    endscreen = pygame.transform.smoothscale(endscreen, (1280, 720))
    endscreen_rect = endscreen.get_rect()

    screen = pygame.display.set_mode((1280, 720))
    endscreen = endscreen.convert_alpha()

    endscreen.set_colorkey((255, 255, 255))

    fps = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False

        screen.fill((150, 150, 150))
        screen.blit(endscreen, endscreen_rect)

        pygame.display.update()

        fps.tick(60)


def display_loss_screen():
    """
    The loss screen is called when each level functions return False
    """
    pygame.init()

    pygame.display.set_caption('Game Over')

    quitscreen = pygame.image.load('gameover.png')
    quitscreen = pygame.transform.smoothscale(quitscreen, (1280, 720))
    quitscreen_rect = quitscreen.get_rect()

    screen = pygame.display.set_mode((1280, 720))
    quitscreen = quitscreen.convert_alpha()

    quitscreen.set_colorkey((255, 255, 255))

    fps = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False

        screen.fill((150, 150, 150))
        screen.blit(quitscreen, quitscreen_rect)

        pygame.display.update()

        fps.tick(60)


def display_quit_screen():
    """
    This is quit screen that showing the Pepe gave up to escape the dungeon with 'You gave up' subtitle
    """
    pygame.init()

    pygame.display.set_caption('Quit Screen')

    quitscreen = pygame.image.load('quitscreen.png')
    quitscreen = pygame.transform.smoothscale(quitscreen, (1280, 720))
    quitscreen_rect = quitscreen.get_rect()

    screen = pygame.display.set_mode((1280, 720))
    quitscreen = quitscreen.convert_alpha()

    quitscreen.set_colorkey((255, 255, 255))

    fps = pygame.time.Clock()

    run = True
    while run:
        screen.fill((150, 150, 150))
        screen.blit(quitscreen, quitscreen_rect)

        pygame.display.update()

        fps.tick(60)

        # The quit screen is automatically closed after 1.5 seconds instead of clicking close button
        time.sleep(1.5)
        run = False
