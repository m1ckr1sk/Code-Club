"""
This module is the concrete implementation
of the abstract level object.
"""
from platform import Platform
from level import Level


# Create platforms for the level
class ConcreteLevel(Level):
    """ Definition for level 1. """

    def __init__(self, player, platforms, level_limit):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = level_limit

        # Array with width, height, x, and y of platform
        level = platforms

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
