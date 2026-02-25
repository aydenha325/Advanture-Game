"""
This provides the overall structure of the game

Written by Ayden Ha and Matias Tapia for CS 1400
"""
import level1, level2, level3
import display_win_or_loss as screen
import pygame


def start_screen():
    """
    This is start screen that shows the title of its game and how to move
    """
    pygame.init()

    # Sets the screen's name
    pygame.display.set_caption('Start Screen')

    # Calling the background map image
    start_map = pygame.image.load('background1.webp')
    start_map = pygame.transform.smoothscale(start_map, (1280, 720))
    start_map_rect = start_map.get_rect()

    # Set the screen size as 1280x720
    screen = pygame.display.set_mode((1280, 720))
    start_map = start_map.convert_alpha()

    start_map.set_colorkey((255, 255, 255))

    # Call every image, and set its size and position
    title = pygame.image.load('title.png')
    title = pygame.transform.smoothscale(title, (1560, 660))
    title_rect = title.get_rect()
    title_rect.centerx = 650
    title_rect.centery = 200

    move = pygame.image.load('move.png')
    move = pygame.transform.smoothscale(move, (600, 610))
    move_rect = move.get_rect()
    move_rect.centerx = 230
    move_rect.centery = 530

    start_here = pygame.image.load('start1.png')
    start_here = pygame.transform.smoothscale(start_here, (605, 420))
    start_here_rect = start_here.get_rect()
    start_here_rect.centerx = 970
    start_here_rect.centery = 575

    door = pygame.image.load('door1.png')
    door = pygame.transform.smoothscale(door, (150, 100))
    door_rect = door.get_rect()
    door_rect.centerx = 1100
    door_rect.centery = 682

    # Define the player character
    player = pygame.image.load("pepe1.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (75, 75))
    player_rect = player.get_rect()

    # The first default location of player
    x_pos = start_map.get_size()[0] // 2
    y_pos = start_map.get_size()[1] // 2

    # Player character's movement variables
    to_x = 0
    to_y = 0

    # Sets frame per second and mouse cursor invisible
    fps = pygame.time.Clock()
    pygame.mouse.set_visible(False)

    is_start = False
    while not is_start:
        # If the close button or window closing shortcut is pressed, the game ends and function returns 1
        # Returning 1 is for boolean for use if statement in main function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1

            # Control the player
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

        # Move player
        x_pos += to_x
        y_pos += to_y

        # Declares player's new position
        player_rect.center = x_pos, y_pos

        # Prevents the player to go out of the screen
        if x_pos < 0:
            x_pos = 0
        elif x_pos > 1280 - 30:
            x_pos = 1280 - 30
        if y_pos < 0:
            y_pos = 0
        elif y_pos > 720 - 30:
            y_pos = 720 - 30

        # Call and put the images to the screen
        screen.fill((150, 150, 150))
        screen.blit(start_map, start_map_rect)

        screen.blit(move, move_rect)
        screen.blit(start_here, start_here_rect)
        screen.blit(door, door_rect)
        screen.blit(player, player_rect)
        screen.blit(title, title_rect)

        # Checks the player reaches the door
        if player_rect.colliderect(door_rect):
            is_start = True

        pygame.display.update()

        # Set the fps to 60
        fps.tick(60)


def start_level(name, file):
    """
    Each level have its own start screen theme in this game.
    The 'name' and 'file' are string parameters that for window caption and file name.
    """
    pygame.init()

    # name parameter for window caption
    pygame.display.set_caption(name)

    # file parameter for file name
    start_level1 = pygame.image.load(file)
    start_level1 = pygame.transform.smoothscale(start_level1, (1280, 720))
    start_level1_rect = start_level1.get_rect()

    screen = pygame.display.set_mode((1280, 720))

    fps = pygame.time.Clock()
    pygame.mouse.set_visible(False)

    run = True
    while run:
        # If you quit game instead continue it, function returns 1 to raise ZeroDivisionError in main function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1

            # Space key for move forward in every screen(each stage entering screen and ending screens) except quit screen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False

        screen.fill((150, 150, 150))
        screen.blit(start_level1, start_level1_rect)

        pygame.display.update()

        fps.tick(60)


def main():
    """
    Main function in this game
    """

    # I asked TA that is it okay to use try/except statements, and they allowed it
    # Every function returns 1 if player quit the game, and it raises ZeroDivisionError in try / except statements
    # Or, they return nothing(None) if player successfully passed each screen, or False if player dead
    # They are very effective way to escape the whole code in try statement.
    try:
        # When the ZeroDivisionError occurs in try statement, the program goes to 'except ZeroDivisionError:' directly
        # If statements do not work when player pass the level or press space button (return None)
        if start_screen():
            raise ZeroDivisionError

        # Level 1
        if start_level('Level 1', 'level1start.png'):
            raise ZeroDivisionError
        while 1:
            # First, run the function
            is_quit = level1.level1()
            # Then, check the boolean, and if it's true(int 1), it means player quit the game, then it raise error
            if is_quit:
                raise ZeroDivisionError
            # None means passed the level, since the function returns nothing
            # False means player failed the level
            else:
                if is_quit is None:
                    break
                elif is_quit is False:
                    # If player quit the game in loss screen, the whole game ends as well
                    if screen.display_loss_screen():
                        raise ZeroDivisionError

        # Level 2
        if start_level('Level 2', 'level2start.png'):
            raise ZeroDivisionError
        while 1:
            is_quit = level2.level2()
            if is_quit:
                raise ZeroDivisionError
            else:
                if is_quit is None:
                    break
                elif is_quit is False:
                    if screen.display_loss_screen():
                        raise ZeroDivisionError

        # Level 3
        if start_level('Level 3', 'level3start.png'):
            raise ZeroDivisionError
        while 1:
            is_quit = level3.level3()
            if is_quit:
                raise ZeroDivisionError
            else:
                if is_quit is None:
                    break
                elif is_quit is False:
                    if screen.display_loss_screen():
                        raise ZeroDivisionError

        # Win screen
        screen.display_win_screen('theend1.png')
        screen.display_win_screen('theend2.png')
        pygame.quit()

    # Quit screen
    except ZeroDivisionError:
        screen.display_quit_screen()
        pygame.quit()


if __name__ == "__main__":
    main()
