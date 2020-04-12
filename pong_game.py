import pygame, time
from pygame.locals import *
from random import randint
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
pygame.init()

def human_player1(event):
        global NO_MOVEMENT1,UP1,DOWN1
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_w:
                UP1 = True
                DOWN1 = False
                NO_MOVEMENT1 = False
            elif event.key == K_s:
                UP1 = False
                DOWN1 = True
                NO_MOVEMENT1 = False
                          
        elif event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                NO_MOVEMENT1 = True
                DOWN1 = False
                UP1 = False

def human_player2(event):
        global NO_MOVEMENT2,UP2,DOWN2
          
        if event.type == KEYDOWN:
            if event.key == K_UP:
                UP2 = True
                DOWN2 = False
                NO_MOVEMENT2 = False
                
            elif event.key == K_DOWN:
                UP2 = False
                DOWN2 = True
                NO_MOVEMENT2 = False

        elif event.type == KEYUP:
            if event.key == K_DOWN or event.key == K_UP:
                NO_MOVEMENT2 = True
                DOWN2 = False
                UP2 = False
                
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 600

clock = pygame.time.Clock()



UP1 = False
DOWN1 = False
NO_MOVEMENT1 = True

UP2 = False
DOWN2 = False
NO_MOVEMENT2 = True


UPLEFT = 0
DOWNLEFT = 1
UPRIGHT = 2
DOWNRIGHT = 3



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



### Creating the main surface ###

main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption("Pong by Biswarup Ray")
surface_rect = main_surface.get_rect()


class Paddle(pygame.sprite.Sprite):
    def __init__(self, player_number):

        ### Creating the paddle ###
        
        pygame.sprite.Sprite.__init__(self)

        self.player_number = player_number
        self.image = pygame.Surface([10, 100])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.speed = 10


        ### Establishing the location of each paddle ##
        
        if self.player_number == 1:
            self.rect.centerx = main_surface.get_rect().left
            self.rect.centerx += 50
        elif self.player_number == 2:
            self.rect.centerx = main_surface.get_rect().right
            self.rect.centerx -= 50
        self.rect.centery = main_surface.get_rect().centery



    def move(self):

        if self.player_number == 1:
            if (UP1 == True) and (self.rect.y > 5):
                self.rect.y -= self.speed
            elif (DOWN1 == True) and (self.rect.bottom < WINDOW_HEIGHT-5):
                self.rect.y += self.speed
            elif (NO_MOVEMENT1 == True):
                pass

        if self.player_number == 2:
            if (UP2 == True) and (self.rect.y > 5):
                self.rect.y -= self.speed
            elif (DOWN2 == True) and (self.rect.bottom < WINDOW_HEIGHT-5):
                self.rect.y += self.speed
            elif (NO_MOVEMENT2 == True):
                pass

class AIPaddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 100])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        #ai paddle speed
        self.speed = 10
        self.rect.centerx += 50

    def move(self, ball):
        if ball.rect.top < self.rect.top:
            self.rect.centery -= self.speed
        elif ball.rect.bottom > self.rect.bottom:
            self.rect.centery += self.speed




class Ball(pygame.sprite.Sprite):
    def __init__(self,speed):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = surface_rect.centerx
        self.rect.centery = surface_rect.centery
        self.direction = randint(0,3)
        self.speed = speed

    def move(self):
        if self.direction == UPLEFT:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
        elif self.direction == UPRIGHT:
            self.rect.x += self.speed
            self.rect.y -= self.speed
        elif self.direction == DOWNLEFT:
            self.rect.x -= self.speed
            self.rect.y += self.speed
        elif self.direction == DOWNRIGHT:
            self.rect.x += self.speed
            self.rect.y += self.speed

    def change_direction(self):
        if self.rect.y < 0 and self.direction == UPLEFT:
            self.direction = DOWNLEFT
        if self.rect.y < 0 and self.direction == UPRIGHT:
            self.direction = DOWNRIGHT
        if self.rect.y > surface_rect.bottom and self.direction == DOWNLEFT:
            self.direction = UPLEFT
        if self.rect.y > surface_rect.bottom and self.direction == DOWNRIGHT:
            self.direction = UPRIGHT

       
        
basic_font = pygame.font.SysFont("Arial", 80)
game_over_font_big = pygame.font.SysFont("Baskerville old face", 72)
game_over_font_small = pygame.font.SysFont("Baskerville old face", 50)
game_over_font=pygame.font.SysFont("Baskerville old face", 40)
font=pygame.font.SysFont("Arial", 20)
font_style = pygame.font.SysFont("baskerville old face", 35)





def paddle_hit(ball,paddle1,paddle2):

    if pygame.sprite.collide_rect(ball, paddle2):
        if (ball.direction == UPRIGHT):
            ball.direction = UPLEFT
        elif (ball.direction == DOWNRIGHT):
            ball.direction = DOWNLEFT
        ball.speed += 1
    elif pygame.sprite.collide_rect(ball, paddle1):
        if (ball.direction == UPLEFT):
            ball.direction = UPRIGHT
        elif (ball.direction == DOWNLEFT):
            ball.direction = DOWNRIGHT
        ball.speed +=1

def paddle_hit_impossible(ball,paddle1,paddle2):

    if pygame.sprite.collide_rect(ball, paddle2):
        if (ball.direction == UPRIGHT):
            ball.direction = UPLEFT
        elif (ball.direction == DOWNRIGHT):
            ball.direction = DOWNLEFT
    elif pygame.sprite.collide_rect(ball, paddle1):
        if (ball.direction == UPLEFT):
            ball.direction = UPRIGHT
        elif (ball.direction == DOWNLEFT):
            ball.direction = DOWNRIGHT
                   
def singlegame():
 ball = Ball(4)
 global player1_win,player2_win
 player1_win = False
 player2_win = False 
 paddle1 = AIPaddle()
 paddle2 = Paddle(2)
 all_sprites = pygame.sprite.RenderPlain(paddle1, paddle2, ball) 
 all_sprites_list = pygame.sprite.Group()
 counter = 0  
 player1_score = 0
 player2_score = 0
 while True:

    clock.tick(60)

    if (ball.rect.x > WINDOW_WIDTH):
        ball.rect.centerx = surface_rect.centerx
        ball.rect.centery = surface_rect.centery
        ball.direction = randint(0, 1)
        ball.speed = 6
    elif (ball.rect.x < 0):
        ball.rect.centerx = surface_rect.centerx
        ball.rect.centery = surface_rect.centery
        ball.direction = randint(2, 3)
        ball.speed = 6


    #add the movement here
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        human_player2(event)
        
    instr=font.render("*5 points to Win*",True,WHITE,BLACK)
    instr_rect=instr.get_rect()
    instr_rect.centerx=200
    instr_rect.centery = 30
    score_board = basic_font.render(str(player1_score) + "           " + str(player2_score), True, WHITE, BLACK) 
    score_board_rect = score_board.get_rect()
    score_board_rect.centerx = surface_rect.centerx 
    score_board_rect.y = 10

    
    main_surface.fill(BLACK)
    main_surface.blit(instr,instr_rect)
    main_surface.blit(score_board, score_board_rect)

    ##draw the net##
    pygame.draw.line(main_surface, WHITE, [512, 0], [512, 600], 6)
    
    all_sprites_list.draw(main_surface)


    all_sprites.draw(main_surface)

    paddle1.move(ball)
    paddle2.move()
    ball.move()
    ball.change_direction()

    paddle_hit(ball,paddle1,paddle2)

    if ball.rect.x > WINDOW_WIDTH:
        player1_score += 1
    elif ball.rect.x < 0:
        player2_score += 1

    

    pygame.display.update()

    if counter == 0:
        time.sleep(1.5)

    if player1_score == 5:
        player1_win = True
        break
    elif player2_score == 5:
        player2_win = True
        break

    counter += 1
    
def singlegame1():
 ball = Ball(8)
 global player1_win,player2_win
 player1_win = False
 player2_win = False 
 paddle1 = AIPaddle()
 paddle2 = Paddle(2)
 all_sprites = pygame.sprite.RenderPlain(paddle1, paddle2, ball) 
 all_sprites_list = pygame.sprite.Group()
 counter = 0  
 player1_score = 0
 player2_score = 0
 while True:

    clock.tick(60)

    if (ball.rect.x > WINDOW_WIDTH):
        ball.rect.centerx = surface_rect.centerx
        ball.rect.centery = surface_rect.centery
        ball.direction = randint(0, 1)
        ball.speed = 8
    elif (ball.rect.x < 0):
        ball.rect.centerx = surface_rect.centerx
        ball.rect.centery = surface_rect.centery
        ball.direction = randint(2, 3)
        ball.speed = 8


    #add the movement here
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        human_player2(event)
        
    instr=font.render("*5 points to Win*",True,WHITE,BLACK)
    instr_rect=instr.get_rect()
    instr_rect.centerx=200
    instr_rect.centery = 30
    score_board = basic_font.render(str(player1_score) + "           " + str(player2_score), True, WHITE, BLACK) 
    score_board_rect = score_board.get_rect()
    score_board_rect.centerx = surface_rect.centerx 
    score_board_rect.y = 10

    
    main_surface.fill(BLACK)
    main_surface.blit(instr,instr_rect)
    main_surface.blit(score_board, score_board_rect)

    ##draw the net##
    pygame.draw.line(main_surface, WHITE, [512, 0], [512, 600], 6)
    
    all_sprites_list.draw(main_surface)


    all_sprites.draw(main_surface)

    paddle1.move(ball)
    paddle2.move()
    ball.move()
    ball.change_direction()

    paddle_hit_impossible(ball,paddle1,paddle2)

    if ball.rect.x > WINDOW_WIDTH:
        player1_score += 1
    elif ball.rect.x < 0:
        player2_score += 1

    

    pygame.display.update()

    if counter == 0:
        time.sleep(1.5)

    if player1_score == 5:
        player1_win = True
        break
    elif player2_score == 5:
        player2_win = True
        break

    counter += 1

def doublegame():
 ball = Ball(4)
 global player1_win,player2_win
 player1_win = False
 player2_win = False 
 paddle1 = Paddle(1)
 paddle2 = Paddle(2)
 counter = 0  
 player1_score = 0
 player2_score = 0

 all_sprites = pygame.sprite.RenderPlain(paddle1, paddle2, ball) 
 all_sprites_list = pygame.sprite.Group()
 while True:

    clock.tick(60)

    if (ball.rect.x > WINDOW_WIDTH):
        ball.rect.centerx = surface_rect.centerx
        ball.rect.centery = surface_rect.centery
        ball.direction = randint(0, 1)
        ball.speed = 6
    elif (ball.rect.x < 0):
        ball.rect.centerx = surface_rect.centerx
        ball.rect.centery = surface_rect.centery
        ball.direction = randint(2, 3)
        ball.speed = 6


    #add the movement here
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        human_player1(event)
        human_player2(event)
        
    instr=font.render("*5 points to Win*",True,WHITE,BLACK)
    instr_rect=instr.get_rect()
    instr_rect.centerx=200
    instr_rect.centery = 30
    score_board = basic_font.render(str(player1_score) + "           " + str(player2_score), True, WHITE, BLACK) 
    score_board_rect = score_board.get_rect()
    score_board_rect.centerx = surface_rect.centerx 
    score_board_rect.y = 10

    
    main_surface.fill(BLACK)
    main_surface.blit(instr,instr_rect)
    main_surface.blit(score_board, score_board_rect)

    ##draw the net##
    pygame.draw.line(main_surface, WHITE, [512, 0], [512, 600], 6)
    
    all_sprites_list.draw(main_surface)


    all_sprites.draw(main_surface)

    paddle1.move()
    paddle2.move()
    ball.move()
    ball.change_direction()

    paddle_hit(ball,paddle1,paddle2)

    if ball.rect.x > WINDOW_WIDTH:
        player1_score += 1
    elif ball.rect.x < 0:
        player2_score += 1

    

    pygame.display.update()

    if counter == 0:
        time.sleep(1.5)

    if player1_score == 5:
        player1_win = True
        break
    elif player2_score == 5:
        player2_win = True
        break

    counter += 1
    
#main program
def message1(msg, color,height):    #function to display game over message
    mesg = font_style.render(msg, True, color)
    main_surface.blit(mesg, [WINDOW_WIDTH / 6, height])
                
def main():
 main_surface.fill(BLACK)
 message1('PONG GAME', WHITE,WINDOW_HEIGHT / 5)
 message1('Press a for SINGLE PLAYER', WHITE,WINDOW_HEIGHT / 2.92)
 message1('Press b for PLAYER VS PLAYER', WHITE,WINDOW_HEIGHT / 2.42)
 pygame.display.flip() 
 while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
        if event.key == pygame.K_a: 
                main_ai()                

        if event.key == pygame.K_b:
            doublegame()
            while True:

                for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()

                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pygame.quit()
                                sys.exit()

                        if event.type == KEYDOWN:
                            if event.key == K_c:
                                main()

                main_surface.fill(BLACK)

                if player1_win == True:
                        game_over = game_over_font_big.render("GAME OVER", True, WHITE, BLACK)
                        game_over1 = game_over_font_small.render("Player 1 Wins", True, WHITE, BLACK)
                        game_over2 = game_over_font.render("Press c to play again and Escape to exit", True, WHITE, BLACK)
                elif player2_win == True:
                        game_over = game_over_font_big.render("GAME OVER", True, WHITE, BLACK)
                        game_over1 = game_over_font_small.render("Player 2 Wins", True, WHITE, BLACK)
                        game_over2 = game_over_font.render("Press c to play again and Escape to exit", True, WHITE, BLACK)

                game_over_rect = game_over.get_rect()
                game_over_rect.centerx = surface_rect.centerx
                game_over_rect.centery = surface_rect.centery -80
                game_over1_rect = game_over1.get_rect()
                game_over1_rect.centerx = game_over_rect.centerx
                game_over1_rect.centery = game_over_rect.centery + 45
                game_over2_rect = game_over2.get_rect()
                game_over2_rect.centerx = game_over_rect.centerx
                game_over2_rect.centery = game_over_rect.centery + 100

                main_surface.blit(game_over, game_over_rect)
                main_surface.blit(game_over1, game_over1_rect)
                main_surface.blit(game_over2, game_over2_rect)

                pygame.display.flip()

def main_ai():
 main_surface.fill(BLACK)
 message1('Press 1 to play against ai', WHITE,WINDOW_HEIGHT / 2.92)
 message1('Press 2 to play against UNBEATABLE ai', WHITE,WINDOW_HEIGHT / 2.42)
 pygame.display.flip() 
 while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
        if event.key == pygame.K_1 or event.key == pygame.K_KP1: 
            singlegame()
            while True:

                for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()

                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pygame.quit()
                                sys.exit()

                        if event.type == KEYDOWN:
                            if event.key == K_c:
                                main()

                main_surface.fill(BLACK)

                if player1_win == True:
                        game_over = game_over_font_big.render("GAME OVER", True, WHITE, BLACK)
                        game_over1 = game_over_font_small.render("Player 1 Wins", True, WHITE, BLACK)
                        game_over2 = game_over_font.render("Press c to play again and Escape to exit", True, WHITE, BLACK)
                elif player2_win == True:
                        game_over = game_over_font_big.render("GAME OVER", True, WHITE, BLACK)
                        game_over1 = game_over_font_small.render("Player 2 Wins", True, WHITE, BLACK)
                        game_over2 = game_over_font.render("Press c to play again and Escape to exit", True, WHITE, BLACK)

                game_over_rect = game_over.get_rect()
                game_over_rect.centerx = surface_rect.centerx
                game_over_rect.centery = surface_rect.centery -80
                game_over1_rect = game_over1.get_rect()
                game_over1_rect.centerx = game_over_rect.centerx
                game_over1_rect.centery = game_over_rect.centery + 45
                game_over2_rect = game_over2.get_rect()
                game_over2_rect.centerx = game_over_rect.centerx
                game_over2_rect.centery = game_over_rect.centery + 100

                main_surface.blit(game_over, game_over_rect)
                main_surface.blit(game_over1, game_over1_rect)
                main_surface.blit(game_over2, game_over2_rect)

                pygame.display.flip()
        if event.key == pygame.K_2 or event.key == pygame.K_KP2: 
            singlegame1()
            while True:

                for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()

                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pygame.quit()
                                sys.exit()

                        if event.type == KEYDOWN:
                            if event.key == K_c:
                                main()

                main_surface.fill(BLACK)

                if player1_win == True:
                        game_over = game_over_font_big.render("GAME OVER", True, WHITE, BLACK)
                        game_over1 = game_over_font_small.render("Player 1 Wins", True, WHITE, BLACK)
                        game_over2 = game_over_font.render("Press c to play again and Escape to exit", True, WHITE, BLACK)
                elif player2_win == True:
                        game_over = game_over_font_big.render("GAME OVER", True, WHITE, BLACK)
                        game_over1 = game_over_font_small.render("Player 2 Wins", True, WHITE, BLACK)
                        game_over2 = game_over_font.render("Press c to play again and Escape to exit", True, WHITE, BLACK)

                game_over_rect = game_over.get_rect()
                game_over_rect.centerx = surface_rect.centerx
                game_over_rect.centery = surface_rect.centery -80
                game_over1_rect = game_over1.get_rect()
                game_over1_rect.centerx = game_over_rect.centerx
                game_over1_rect.centery = game_over_rect.centery + 45
                game_over2_rect = game_over2.get_rect()
                game_over2_rect.centerx = game_over_rect.centerx
                game_over2_rect.centery = game_over_rect.centery + 100

                main_surface.blit(game_over, game_over_rect)
                main_surface.blit(game_over1, game_over1_rect)
                main_surface.blit(game_over2, game_over2_rect)

                pygame.display.flip()               
main()
input('press enter to exit')
