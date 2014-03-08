# Alien Destroy


import math, random
from livewires import games, color

games.init(screen_width = 800, screen_height = 600, fps = 50)

class Alien(games.Sprite):
    """
    An alien which moves.
    """
    image = games.load_image("alien.jpg")

    def __init__(self, y, speed = 2, odds_change = 200):
        """ Initialize alien. """
        super(Alien, self).__init__(image = alien.image,
                                   x = games.screen.width / 2,
                                   y = y,
                                   dx = speed)
        
        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        """ Determine if direction needs to be reversed. """
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
           self.dx = -self.dx
                
        self.check_drop()
        

    def die(self):
        """ Destroy block. """
        Block.total -= 1

        self.game.score.value += int(Block.POINTS)
        self.game.score.right = games.screen.width - 10   
    

        # if block is gone, next level    
        if Block.total == 0:
            self.game.advance()

        super(Block, self).die()
        

class Ball(games.Sprite):
    """ A bouncing ball. """
    ballImage = games.load_image("ball.jpg", transparent = True)

    def __init__(self, game, x, y):
        """ Initialize platform sprite. """
        super(Ball, self).__init__(image = Ball.ballImage, x = x, y = y)
        self.game = game
        
    def update(self):
        """ Reverse a velocity component if platform reached. """
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
            
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy


class Platform(games.Sprite):
    """ The player. """
    pImage = games.load_image("platform.jpg", transparent = True)


    def __init__(self, game, x, y):
        """ Initialize platform sprite. """
        super(Platform, self).__init__(image = Platform.pImage, x = x, y = y)
        self.game = game
        

    def update(self):
        """ move based on keys pressed. """
        super(Platform, self).update()
    
        # move based on left and right arrow keys
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x -= 1
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x += 1
            

    def die(self):
        """ Destroy platform and end the game. """
        self.game.end()
        super(Platform, self).die()
##
class Game(object):
    """ The game itself. """
    def __init__(self):
        """ Initialize Game object. """
        # set level
        self.level = 0

        # load sound for level advance
        self.sound = games.load_sound("level.wav")

        # create score
        self.score = games.Text(value = 0,
                                size = 30,
                                color = color.white,
                                top = 5,
                                right = games.screen.width - 10,
                                is_collideable = False)
        games.screen.add(self.score)
##
        # create player's ship
        self.platform = Platform(game = self, 
                         x = games.screen.width/2,
                         y = games.screen.height)
        games.screen.add(self.platform)
        # Create the ball
        self.ball = Ball(game = self,
                     x = games.screen. width/2,
                     y = games.screen.height,
                     dx = 2,
                     dy = 2)
        games.screen.add(self.ball)
##        
    def play(self):
        """ Play the game. """
        # begin theme music
        games.music.load("Gthang.mp3")
        games.music.play(-1)

        # load and set background
        meadow_image = games.load_image("meadow.jpg", transparent = False)
        games.screen.background = meadow_image
##
##        # advance to level 1
        self.advance()
##
##        # start play
        games.screen.mainloop()
##
##    def advance(self):
##        """ Advance to the next game level. """
        self.level += 1
##     
##       
            # create the alien
        self.alien = Alien(game = self, 
                         x = games.screen.width/2,
                         y = games.screen.height/5)
        games.screen.add(self.alien)
##
##        # display level number
##        level_message = games.Message(value = "Level " + str(self.level),
##                                      size = 40,
##                                      color = color.yellow,
##                                      x = games.screen.width/2,
##                                      y = games.screen.width/10,
##                                      lifetime = 3 * games.screen.fps,
##                                      is_collideable = False)
##        games.screen.add(level_message)
##
##        # play new level sound (except at first level)
##        if self.level > 1:
##            self.sound.play()
##            
##    def end(self):
##        """ End the game. """
##        # show 'Game Over' for 5 seconds
##        end_message = games.Message(value = "Game Over",
##                                    size = 90,
##                                    color = color.red,
##                                    x = games.screen.width/2,
##                                    y = games.screen.height/2,
##                                    lifetime = 5 * games.screen.fps,
##                                    after_death = games.screen.quit,
##                                    is_collideable = False)
        games.screen.add(end_message)


def main():
    astrocrash = Game()
    astrocrash.play()

# kick it off!
main()
