"""
This module contains the core application logic and
game loop
"""
from concrete_level import ConcreteLevel
from player import Player
import yaml
import pygame
import constants


def main():
    """Main entry oint of the application"""
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Side-scrolling Platformer")

    # Create the player
    player = Player()

    level_list = load_game_levels(player)

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                handle_key_down(event, player)

            if event.type == pygame.KEYUP:
                handle_key_up(event, player)

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        detect_player_screen_shift(player, current_level)

        current_level = detect_level_change(player, current_level, current_level_no, level_list)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

def detect_player_screen_shift(player, current_level):
    """If the player gets near the right side, shift the world left (-x)
    If the player gets near the left side, shift the world right (+x)"""
    if player.rect.right >= 500:
        diff = player.rect.right - 500
        player.rect.right = 500
        current_level.shift_world(-diff)


    if player.rect.left <= 120:
        diff = 120 - player.rect.left
        player.rect.left = 120
        current_level.shift_world(diff)

def detect_level_change(player, current_level, current_level_no, level_list):
    """If the player gets to the end of the level, go to the next level"""
    current_position = player.rect.x + current_level.world_shift
    if current_position < current_level.level_limit:
        player.rect.x = 120
        if current_level_no < len(level_list) - 1:
            current_level_no += 1
            current_level = level_list[current_level_no]
            player.level = current_level
    return current_level

def handle_key_up(event, player):
    """All logic to handle the key up command"""
    if event.key == pygame.K_LEFT and player.change_x < 0:
        player.stop()
    if event.key == pygame.K_RIGHT and player.change_x > 0:
        player.stop()

def handle_key_down(event, player):
    """All logic to handle the key down command"""
    if event.key == pygame.K_LEFT:
        player.go_left()
    if event.key == pygame.K_RIGHT:
        player.go_right()
    if event.key == pygame.K_UP:
        player.jump()

def load_game_levels(player):
    """Load the game configuration from the games
    configuration file"""
    level_limit = -1000
    level_list = []
    with open("game_config/data.yaml", 'r') as stream:
        try:
            game_configuration = yaml.load(stream)
            for level in game_configuration['Game Configuration']:
                level_list.append(ConcreteLevel(player, level['Level']['Platforms'], level_limit))
        except yaml.YAMLError as exc:
            print(exc)
    return level_list


if __name__ == "__main__":
    main()
