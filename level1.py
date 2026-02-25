import random
import pygame


def level1():
    pygame.init()

    pygame.display.set_caption('Level 1')

    map = pygame.image.load('background2.webp')
    map = pygame.transform.smoothscale(map, (1280, 720))
    map_rect = map.get_rect()

    screen = pygame.display.set_mode((1280, 720))
    map = map.convert_alpha()

    flame = pygame.image.load('flame.png')
    flame = pygame.transform.smoothscale(flame, (30, 45))
    flame_rect = pygame.Rect(flame.get_rect())
    flametimer = 10
    flames = [[20, 0, 0]]

    door = pygame.image.load('door2.png')
    door = pygame.transform.smoothscale(door, (100, 150))
    door_rect = door.get_rect()
    door_rect.centerx = 1242
    door_rect.centery = 150

    player = pygame.image.load("pepe1.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (50, 50))
    player_rect = player.get_rect()

    x_pos = 50
    y_pos = 650

    to_x = 0
    to_y = 0

    fps = pygame.time.Clock()
    pygame.mouse.set_visible(False)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= 6
                if event.key == pygame.K_RIGHT:
                    to_x += 6
                if event.key == pygame.K_UP:
                    to_y -= 6
                if event.key == pygame.K_DOWN:
                    to_y += 6

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    to_y = 0

        x_pos += to_x
        y_pos += to_y

        player_rect.center = x_pos, y_pos

        if x_pos < 0:
            x_pos = 0
        elif x_pos > 1280 - 30:
            x_pos = 1280 - 30
        if y_pos < 0:
            y_pos = 0
        elif y_pos > 720 - 30:
            y_pos = 720 - 30

        screen.fill((255, 255, 255))
        screen.blit(map, map_rect)
        screen.blit(door, door_rect)

        screen.blit(player, player_rect)

        flametimer -= 15
        if flametimer <= 0:
            flames.append([random.randint(5, 1275), 0, random.randint(0, 2)])
            flametimer = random.randint(50, 200)

        index = 0
        for flame_ in flames:
            flame_[1] += 10
            if flame_[1] > 720:
                flames.pop(index)

            flame_rect.left = flame_[0]
            flame_rect.top = flame_[1]
            if flame_rect.colliderect(player_rect):
                flames.pop(index)
                return False
            screen.blit(flame, (flame_[0], flame_[1]))
            index += 1

        if player_rect.colliderect(door_rect):
            run = False

        pygame.display.update()

        fps.tick(60)
