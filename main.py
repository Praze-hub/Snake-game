import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (110,110,5)

class Apple:
    def __init__(self,parent_screen):
        self.block = pygame.image.load("accessories/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.parent_screen.blit(self.block,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0,15)*SIZE
        self.y = random.randint(0,10)*SIZE





class Snake:
    def __init__(self,parent_screen,lenght):
        self.lenght = lenght
        self.parent_screen = parent_screen
        self.block = pygame.image.load("accessories/block.jpg").convert()
        self.x = [SIZE]*lenght
        self.y = [SIZE]*lenght
        self.direction = "down"

   

    def draw(self):
        for i in range(self.lenght):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()

    def increase_lenght(self):
        self.lenght +=1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = "left"
    def move_right(self):
        self.direction = "right"
        
    def move_up(self):
        self.direction = "up"
        
    def move_down(self):
        self.direction = "down"
        

    
    def walk(self):

        for i in range(self.lenght-1,0,-1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "up":
            self.y[0] -= SIZE
        if self.direction == "down":
            self.y[0] += SIZE
        if self.direction == "left":
            self.x[0] -= SIZE
        if self.direction == "right":
            self.x[0] += SIZE
        
        self.draw()

   






class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.play_background_music()
        self.surface = pygame.display.set_mode((600,600))
        self.surface.fill((110,110,5))
        self.snake = Snake(self.surface,1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 <= x2 + SIZE:
            if y1 >= y2 and y1 <= y2 + SIZE:
                return True

        return False

    def play_background_music(self):
        pygame.mixer.music.load("accessories/bg_music_1.mp3")
        pygame.mixer.music.play()

    def render_background(self):
        bg = pygame.image.load("accessories/background.jpg")
        self.surface.blit(bg,(0,0))


    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            sound = pygame.mixer.Sound("accessories/1_snake_game_resources_ding.mp3")
            pygame.mixer.Sound.play(sound)
            self.snake.increase_lenght()
            self.apple.move()

        for i in range(3,self.snake.lenght):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                sound = pygame.mixer.Sound("accessories/1_snake_game_resources_crash.mp3")
                pygame.mixer.Sound.play(sound)
            
                raise "Collision Occured"

        if not (0 <= self.snake.x[0] <=600 and 0 <=self.snake.y[0] <=600):
            self.play_sound("accessories/1_snake_game_resources_crash.mp3")
            raise "Hit the boundary error"
    
    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial',30)
        line1 = font.render(f"Game Over! Your score is {self.snake.lenght}",True,(255,255,255))
        self.surface.blit(line1,(200,300))
        line2 = font.render("To play again press Enter,To exit game press Escape!",True,(255,255,255))
        self.surface.blit(line2,(10,350))
        pygame.display.flip()
        pygame.mixer.music.pause()
    
    def reset(self):
        self.snake = Snake(self.surface,1)
        self.apple = Apple(self.surface)





    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.lenght}",True,(255,255,255))
        self.surface.blit(score,(500,10))



    def run(self):
        running =True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause= False
                    if not pause:
                        if event.key  == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()

                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()


                    
                


                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()
            except Exception  as e:
                self.show_game_over()
                pause = True
                self.reset()
            time.sleep(.3)

            




def draw_block():
    surface.fill((110,110,5))
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()




    
    