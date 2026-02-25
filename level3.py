import pygame


def level3():
    pygame.init()

    pygame.display.set_caption('Level 3')

    map = pygame.image.load('background4.webp')
    map = pygame.transform.smoothscale(map, (1280, 720))
    map_rect = map.get_rect()

    screen = pygame.display.set_mode((1280, 720))
    map = map.convert_alpha()

    door = pygame.image.load('door2.png')
    door = pygame.transform.smoothscale(door, (100, 150))
    door_rect = door.get_rect()
    door_rect.centerx = 1190
    door_rect.centery = 150

    locker_door = pygame.image.load('door3.png')
    locker_door = pygame.transform.smoothscale(locker_door, (70, 150))
    locked_door_rect = locker_door.get_rect()
    locked_door_rect.centerx = 1200
    locked_door_rect.centery = 150

    key1 = pygame.image.load('key1.png')
    key1 = pygame.transform.smoothscale(key1, (75, 75))
    key1_rect = key1.get_rect()
    key1_rect.centerx = 100
    key1_rect.centery = 100

    key2 = pygame.image.load('key2.png')
    key2 = pygame.transform.smoothscale(key2, (60, 60))
    key2_rect = key2.get_rect()
    key2_rect.centerx = 100
    key2_rect.centery = 620

    key3 = pygame.image.load('key3.png')
    key3 = pygame.transform.smoothscale(key3, (70, 30))
    key3_rect = key3.get_rect()
    key3_rect.centerx = 1180
    key3_rect.centery = 630

    player = pygame.image.load("pepe1.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (55, 55))
    player_rect = player.get_rect()

    enemy = pygame.image.load("pepeangry.png").convert_alpha()
    enemy = pygame.transform.smoothscale(enemy, (57, 55))
    enemy_rect = enemy.get_rect()

    not_opened = pygame.font.SysFont(None, 50)

    key1_get = False
    key2_get = False
    key3_get = False

    x_pos = 100
    y_pos = 360
    enemy_x_pos = 800
    enemy_y_pos = 400

    to_x = 0
    to_y = 0
    enemy_to_x = 0
    enemy_to_y = 0

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

        player_pos = player_rect.center
        enemy_pos = enemy_rect.center
        if player_pos[0] > enemy_pos[0]:
            enemy_to_x += 0.25
        else:
            enemy_to_x -= 0.25
        if player_pos[1] > enemy_pos[1]:
            enemy_to_y += 0.25
        else:
            enemy_to_y -= 0.25

        x_pos += to_x
        y_pos += to_y
        enemy_x_pos += enemy_to_x
        enemy_y_pos += enemy_to_y

        player_rect.center = x_pos, y_pos
        enemy_rect.center = enemy_x_pos, enemy_y_pos

        if x_pos < 90:
            x_pos = 90
        elif x_pos > 1280 - 80:
            x_pos = 1280 - 80
        if y_pos < 90:
            y_pos = 90
        elif y_pos > 720 - 90:
            y_pos = 720 - 90

        if enemy_x_pos < 90:
            enemy_x_pos = 90
        elif enemy_x_pos > 1280 - 80:
            enemy_x_pos = 1280 - 80
        if enemy_y_pos < 90:
            enemy_y_pos = 90
        elif enemy_y_pos > 720 - 90:
            enemy_y_pos = 720 - 90

        screen.fill((255, 255, 255))
        screen.blit(map, map_rect)

        if not key1_get:
            screen.blit(key1, key1_rect)
        if player_rect.colliderect(key1_rect):
            key1_get = True

        if not key2_get:
            screen.blit(key2, key2_rect)
        if player_rect.colliderect(key2_rect):
            key2_get = True

        if not key3_get:
            screen.blit(key3, key3_rect)
        if player_rect.colliderect(key3_rect):
            key3_get = True

        if key1_get and key2_get and key3_get:
            screen.blit(door, door_rect)
            if player_rect.colliderect(door_rect):
                run = False
        else:
            screen.blit(locker_door, locked_door_rect)
            if player_rect.colliderect(door_rect):
                label = not_opened.render("You should get 3 keys!", True, (255, 150, 150))
                screen.blit(label, (830, 220))

        if player_rect.colliderect(enemy_rect):
            return False

        screen.blit(player, player_rect)
        screen.blit(enemy, enemy_rect)

        pygame.display.update()

        fps.tick(60)
