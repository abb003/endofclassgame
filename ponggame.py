from livewires import games, color
import random

games.init(screen_width=680, screen_height=650, fps=50)

## Menu options
def main():
    choice = None
    while choice != "0":

        print(
        """
        PyPong options

        0 - Quit
        1 - Display creator's name + credits
        2 - Full game title
        3 - game instructions
        4 - start game
        """
        )

        choice = input("Choice: ")
        print()

        ##exit
        if choice == "0":
            print("Goodbye")
        ##creator name
        elif choice == "1":
            print("Alan Brincks, special thanks to Dr. Craven, Michael Dawson, and Carolyn Brodie")
        elif choice == "2":
            print("Pong game pyStyle")
        elif choice == "3":
            print("Move the mouse up and down to move the platform, and bounce the ball to gain points and advance to the next level, it gets faster as you gain points!")
        elif choice == "4":
            maingame()
        else:
            print("\nSorry, but", choice, "is not valid.")
            
class Alien(games.Sprite):
    """
    An alien which moves.
    """
    image = games.load_image("crab.jpg")

    def __init__(self, y, speed = 2, odds_change = 250):
        """ Initialize alien. """
        super(Alien, self).__init__(image = Alien.image,
                                   x = games.screen.width/2,
                                   y = y,
                                   dx = speed)
        
        self.odds_change = odds_change
        self.collided = False

    def update(self):
        """ Determine if direction needs to be reversed. """
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
           self.dx = -self.dx
        self.collided = False   
        self.check_collide()
        
   ##if ball hits alien add points
    def check_collide(self):
        for ball in self.overlapping_sprites:
            if self.collided == False:
                Paddle.score.value+=10
                self.collided = True
                ball.handle_collide()
            
            
class Paddle(games.Sprite):
##load up paddle sprite
    image=games.load_image("platform.jpg")
    score=games.Text(value=20, size=75, color = color.white, top=5,
                              right=games.screen.width - 20, is_collideable = False)
    def __init__(self, theY=games.screen.height - 25):
        super(Paddle, self).__init__(image=Paddle.image, angle = 0,
                                    y = theY,
                                    x=games.mouse.x,
                                    left=20)
        
        games.screen.add(Paddle.score)

    def update(self):
        self.x=games.mouse.x
        if self.left<0:
            self.x=0
        if self.right>games.screen.width:
            self.x=games.screen.width
        self.check_collide()

    def check_collide(self):
        for ball in self.overlapping_sprites:
            ball.handle_collide2()

class Ball(games.Sprite):

    image=games.load_image("ball.jpg")
    speed=2

    def __init__(self, x=100, y=70):
        super(Ball, self).__init__(image=Ball.image,
                                   x=x, y=y,
                                   dx=Ball.speed, dy=Ball.speed)

##make the ball bounce off walls
    def update(self):
        if self.right>games.screen.width:
            self.dx=-self.dx
        if self.left<0:
            self.dx=-self.dx
        if self.top<0:
            self.dy=-self.dy
        if self.bottom>games.screen.height:
            self.end_game()
            self.destroy()
##ball gets faster as score rises
    def handle_collide(self):
        if Paddle.score.value == 30:
            self.dx *= 2
            self.dy *= 2
        if Paddle.score.value == 60:
            self.dx *= 2
            self.dy *= 2
        self.dy=-self.dy
    def handle_collide2(self):
        self.dy=-self.dy

    def end_game(self):
        end_message=games.Message(value="Game Over",
                                  size=100,
                                  color = color.red,
                                  x=games.screen.width/2,
                                  y=games.screen.height/2,
                                  lifetime=200,
                                  after_death=games.screen.quit)
        games.screen.add(end_message)



def maingame():

    background_image = games.load_image("space.jpg", transparent=False)
    games.screen.background = background_image

    # begin theme music
    games.music.load("80hits.mp3")
    games.music.play(-1)
    
##add sprites to game
    the_alien = Alien(25)
    games.screen.add(the_alien)
    
    the_paddle = Paddle()
    games.screen.add(the_paddle)

    the_ball = Ball()
    games.screen.add(the_ball)

    games.mouse.is_visible=False

    games.screen.event_grab=True

    games.screen.mainloop()

main()
