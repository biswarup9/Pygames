from pygame.locals import *
import random
from random import randint
import pygame
import time
import sys
dis_width = 800
dis_height = 600
  #size of screen given    #title given
pygame.init()   #initializes all modules of pygame
 
white = (255, 255, 255) #colour codes initialised using html values
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
violet= (238, 130, 238)


clock = pygame.time.Clock()    #creates object to help track time
 
snake_block = 10
 
font_style = pygame.font.SysFont("baskerville old face", 35)    #game over font
score_font = pygame.font.SysFont("arial", 25)   #score font

def isCollision(x1,y1,x2,y2,bsize):
    if x1 >= x2 and x1 <= x2 + bsize:
        if y1 >= y2 and y1 <= y2 + bsize:
            return True
    return False

class Apple:
    x = 0
    y = 0
    step = 44

    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step

    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y))



class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)

       # initial positions, no collision.
       self.x[0] = 1*44
       self.x[0] = 2*44

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0


    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3 

    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 



class Computer:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)

       # initial positions, no collision.
       self.x[0] = 1*44
       self.y[0] = 4*44

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0


    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3 

    
    def target(self,dx,dy):
        if self.x[0] > dx:
            self.moveLeft()

        if self.x[0] < dx:
            self.moveRight()

        if self.x[0] == dx:
            if self.y[0] < dy:
                self.moveDown()

            if self.y[0] > dy:
                self.moveUp()

    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 

 
def Your_score(score):  #function to display score
    value = score_font.render("Your Score: " + str(score), True, yellow)    #draws text on a new surface
    dis.blit(value, [0, 0]) #draws an image on screen 
 
def message(msg, color):    #function to display game over message
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
    
def message1(msg, color,height):    #function to display game over message
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, height])
    

class App:

    player = 0
    apple = 0
    
    
    
    def __init__(self):
        self.Length_of_snake = 1
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.player = Player(5) 
        self.apple = Apple(8,5)
        self.computer = Computer(5)

    def on_init(self):  
        self._display_surf= pygame.display.set_mode((dis_width, dis_height))  #size of screen given
        pygame.display.set_caption('Snake Game by Biswarup Ray')
        self._running = True
        self._image_surf = pygame.image.load("pygame.png").convert_alpha()
        self._apple_surf = pygame.image.load("apple.png").convert_alpha()
        
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.player.update()
        self.computer.update()
        self.computer.target(self.apple.x, self.apple.y)
        # does snake eat apple?
        for i in range(0,self.player.length):
            if isCollision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],44):
                self.apple.x = randint(2,9) * 44
                self.apple.y = randint(2,9) * 44
                self.player.length = self.player.length + 1
                self.Length_of_snake+=1

        for i in range(0,self.player.length):
            if isCollision(self.apple.x,self.apple.y,self.computer.x[i], self.computer.y[i],44):
                self.apple.x = randint(2,9) * 44
                self.apple.y = randint(2,9) * 44
                #self.computer.length = self.computer.length + 1

        # does snake collide with itself?
        for i in range(2,self.player.length):
            if isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],40):
                dis.fill(violet)    #giving colour to the background
                message("GAME OVER!!", red)
                message1("Press C To Play Again and Escape to quit", red,dis_height / 1.92)#displaying game over using message()
                Your_score(self.Length_of_snake -1)  #displaying score using Your_score()
                pygame.display.flip()
        pass

    def on_render(self):
        self._display_surf.fill(violet)
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        self.computer.draw(self._display_surf, self._image_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                    
            if (keys[K_RIGHT]):
                self.player.moveRight()

            if (keys[K_LEFT]):
                self.player.moveLeft()

            if (keys[K_UP]):
                self.player.moveUp()

            if (keys[K_DOWN]):
                self.player.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()

            time.sleep (50.0 / 1000.0);
        self.on_cleanup()


dis = pygame.display.set_mode((dis_width, dis_height))

 
def system():
     dis.fill(violet)
     message1('SNAKE GAME', red,dis_height / 5)
     message1('Press a for AI to play', black,dis_height / 2.92)
     message1('Press b for playing yourself', black,dis_height / 2.42)
     pygame.display.flip() 
     while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                theApp = App()
                theApp.on_execute()
            if event.key == pygame.K_b:
                system1()
 

def system1():
     dis.fill(violet)
     message1('Choose Difficulty', red,dis_height / 3.6)
     message1('Press 1 for Easy', black,dis_height / 2.92)
     message1('Press 2 for Medium', black,dis_height / 2.42)
     message1('Press 3 for Hard', black,dis_height / 2.02)
     pygame.display.flip() 
     while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                gameloop(15)
            if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                gameloop(25)
            if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                hard_gameloop(35)
            


_image_surf = pygame.image.load("pygame.png").convert_alpha()
_apple_surf = pygame.image.load("apple.png").convert_alpha()
def our_snake(snake_block, snake_list): #function to draw/display the snake
    for x in snake_list:
        dis.blit(_image_surf,[x[0], x[1], snake_block, snake_block])
clock = pygame.time.Clock()    #creates object to help track time
 
snake_block = 10
def gameloop(snake_speed): #function to continue the game
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #rounding the coordinates
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:    #game_over is bool variable to exit the program
        while game_close == True:   #game_close is bool variable to losing the game
            dis.fill(violet)    #giving colour to the background
            message("GAME OVER!!", red)
            message1("Press C To Play Again and Escape to quit", red,dis_height / 1.92)#displaying game over using message()
            Your_score(Length_of_snake -1)  #displaying score using Your_score()
            pygame.display.flip() #updating the background 
 
            for event in pygame.event.get():    #event in all the events in the queue 
                if event.type == pygame.KEYDOWN:#if a key is hold or not
                    if event.key == pygame.K_c: #if game is over but c key is pressed
                        system()
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:    #if a key is hold or not
                if event.key == pygame.K_LEFT:  #if a left arrow key is hold 
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:#if a right arrow key is hold 
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:  #if an up arrow key is hold 
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:#if a down arrow key is hold 
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width:
            x1=0
        elif x1 < 0:
            x1=dis_width
        if y1 >= dis_height:
            y1=0
        elif y1 < 0:
            y1=dis_height
        x1 += x1_change
        y1 += y1_change
        dis.fill(violet)
        dis.blit(_apple_surf,(foodx, foody))
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()
 
        if isCollision(foodx,foody,x1, y1,snake_block):
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()



def hard_gameloop(snake_speed): #function to continue the game
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #rounding the coordinates
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:    #game_over is bool variable to exit the program
        while game_close == True:   #game_close is bool variable to exit the program
            dis.fill(violet)    #giving colour to the background
            message("GAME OVER!!", red)
            message1("Press C To Play Again and Escape to quit", red,dis_height / 1.92)#displaying game over using message()
            Your_score(Length_of_snake -1)  #displaying score using Your_score()
            pygame.display.flip() #updating the background 
 
            for event in pygame.event.get():    #event in all the events in the queue
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:#if a key is hold or not
                    if event.key == pygame.K_c: #if game is over but c key is pressed
                        system()
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:    #if a key is hold or not
                if event.key == pygame.K_LEFT:  #if a left arrow key is hold 
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:#if a right arrow key is hold 
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:  #if an up arrow key is hold 
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:#if a down arrow key is hold 
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
           game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(violet)
        dis.blit(_apple_surf,(foodx, foody))
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()

     
system()    

