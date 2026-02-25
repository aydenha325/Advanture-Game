import pygame


def pixel_collision(mask1, rect1, mask2, rect2):
    """
    Check if the non-transparent pixels of one mask contacts the non-transparent pixels of another.
    """

    offset_x = rect2[0] - rect1[0]
    offset_y = rect2[1] - rect1[1]

    # See if the two masks at the offset are overlapping.
    overlap = mask1.overlap(mask2, (offset_x, offset_y))
    return overlap != None


def level2():
    pygame.init()

    pygame.display.set_caption('Level 2')

    map = pygame.image.load("background3.jpeg")
    map_size = map.get_size()
    map_rect = map.get_rect()

    screen = pygame.display.set_mode(map_size)
    map = map.convert_alpha()

    map.set_colorkey((255, 255, 255))
    map_mask = pygame.mask.from_surface(map)

    door = pygame.image.load('door2.png')
    door = pygame.transform.smoothscale(door, (80, 120))
    door_rect = door.get_rect()
    door_rect.centerx = 1250
    door_rect.centery = 173

    fly = pygame.image.load('fly.jpg')
    fly = pygame.transform.smoothscale(fly, (75, 50))
    fly_rect = fly.get_rect()
    fly_rect.centerx = 690
    fly_rect.centery = 600

    player = pygame.image.load("pepe1.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (50, 50))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    hungry = pygame.font.SysFont(None, 50)
    should_eat = pygame.font.SysFont(None, 50)

    food = False

    x_pos = 50
    y_pos = 490

    to_x = 0
    to_y = 0

    fps = pygame.time.Clock()
    pygame.mouse.set_visible(False)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= 5
                if event.key == pygame.K_RIGHT:
                    to_x += 5
                if event.key == pygame.K_UP:
                    to_y -= 5
                if event.key == pygame.K_DOWN:
                    to_y += 5

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

        if not food:
            screen.blit(fly, fly_rect)
            label = hungry.render("Pepe is hungry!", True, (255, 150, 150))
            screen.blit(label, (20, 20))

        if player_rect.colliderect(fly_rect):
            food = True

        if player_rect.colliderect(door_rect):
            if not food:
                label = should_eat.render("He should eat something!", True, (255, 150, 150))
                screen.blit(label, (800, 20))
            else:
                run = False

        if pixel_collision(player_mask, player_rect, map_mask, map_rect):
            return False

        pygame.display.update()

        fps.tick(60)
