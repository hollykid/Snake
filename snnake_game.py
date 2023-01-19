### Snake Game Tutorial

import random
import sys
import pygame



# Initialized pygame
pygame.init()

# Time
clock = pygame.time.Clock()

# Create screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Color
red = (255, 0,0)
white = (255, 255, 255)
black = (0,0,0)

# Caption
pygame.display.set_caption("Snake")

FPS = 50

direction = "right"

apple_img = pygame.image.load("apple.png")

img = pygame.image.load("snak_head.png")
def snakes(snake_list, snake_width, snake_height):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    screen.blit(head, (snake_list[-1][0], snake_list[-1][1]))
    for snake in snake_list[:-1]:
        pygame.draw.rect(screen, black, (snake[0],snake[1], snake_width, snake_height))
#global lead_x, lead_y, lead_x_change, lead_y_change


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    game_loop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        screen.fill((255, 255, 255))

        intro_font = pygame.font.SysFont("comicsansms", 70)
        intro_font2 = pygame.font.SysFont("comicsansms", 30)
        intro_render = intro_font.render("Snake Game", True, (0, 200, 0))
        intro_render2 = intro_font2.render("Press C to play and Q to quit", True, (0, 0, 0))
        screen.blit(intro_render, (180, 100))
        screen.blit(intro_render2, (180, 300))

        pygame.display.update()
        clock.tick(15)

def paused():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pause = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        screen.fill((255, 255, 255))

        pause_font = pygame.font.SysFont(None, 50)
        pause_font2 = pygame.font.SysFont(None, 30)
        pause_render = pause_font.render("PAUSED", True, (0,0,0))
        pause_render2 = pause_font2.render("Press C to continue or Q to quit", True, (0, 0, 0))
        screen.blit(pause_render, (350, 200))
        screen.blit(pause_render2, (280, 300))
        pygame.display.update()
        clock.tick(5)



# Game Loop
def game_loop():
    global direction


    lead_x = width/2
    lead_y = height/2
    snake_width = 20
    snake_height = 20
    lead_x_change = 0
    lead_y_change = 0
    apple_width = 20
    apple_height = 20
    snake_list = []
    snake_length = 1
    score = 0




    apple_x = round(random.randint(0, width-apple_width))  #/10.0)*10.0
    apple_y =  round(random.randint(0, height-apple_height)) #/10.0)*10.0

    running = True
    while running:


        screen.fill((white))

        # pygame.draw.rect(screen, (255, 100, 0), (apple_x,apple_y, apple_width, apple_height))
        screen.blit(apple_img, (apple_x, apple_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Keyboarding Binding
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and lead_x_change != -10:
                    direction = "right"
                    lead_x_change += 10
                    lead_y_change = 0

                if event.key == pygame.K_LEFT and lead_x_change != 10:
                    direction = "left"
                    lead_x_change -= 10
                    lead_y_change = 0

                if event.key == pygame.K_UP and lead_y_change != 10:
                    direction = "up"
                    lead_y_change -= 10
                    lead_x_change = 0

                if event.key == pygame.K_DOWN and lead_y_change != -10:
                    direction = "down"
                    lead_y_change += 10
                    lead_x_change = 0
                if event.key == pygame.K_p:
                    paused()









        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)


        if len(snake_list) > snake_length:
            del snake_list[0]

        snakes(snake_list, snake_width, snake_height)
        for each_segment in snake_list[:-1]:
            if each_segment == snake_head:
                gv_font = pygame.font.SysFont("comicsansms", 50)
                gv2_font = pygame.font.SysFont("comicsansms", 30)
                gv_render = gv_font.render("Game Over", True, red)
                gv_render2 = gv2_font.render("Press C to play again or Q to quit", True, black)
                screen.blit(gv_render, (280, 200))
                screen.blit(gv_render2, (200, 300))


                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            game_loop()
                            quit()
                        elif event.key == pygame.K_q:

                            pygame.quit()
                            quit()


        # Collision with border

        if lead_x >= width - snake_width or lead_x <= 0 or lead_y >= height - snake_height or lead_y <= 0:
            gv_font = pygame.font.SysFont("comicsansms", 50)
            gv2_font = pygame.font.SysFont("comicsansms", 30)
            gv_render = gv_font.render("Game Over", True, red)
            gv_render2 = gv2_font.render("Press C to play again or Q to quit", True, black)
            screen.blit(gv_render, (280, 200))
            screen.blit(gv_render2, (200, 300))

            lead_x_change = 0
            lead_y_change = 0

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        game_loop()
                        quit()
                    elif event.key == pygame.K_q:

                        pygame.quit()
                        quit()



        # Collision with apple
        lead_x += lead_x_change
        lead_y += lead_y_change
        if lead_x >= apple_x and lead_x <= apple_x + apple_width or lead_x + snake_width >= apple_x and lead_x + snake_width <= apple_x + apple_width:
            if lead_y > apple_y and lead_y < apple_y+ apple_height or lead_y + snake_height > apple_y and lead_y + snake_height < apple_y + apple_height:

                apple_x = round(random.randint(0, width - apple_width))  # /10.0)*10.0
                apple_y = round(random.randint(0, height - apple_height))  # /10.0)*10.0
                snake_length += 1
                score += 1

        score_font = pygame.font.SysFont(None, 30)
        score_render = score_font.render("score : " + str(score), True, (0, 0, 0))
        screen.blit(score_render, (0, 0))
        pygame.display.update()
        clock.tick(FPS)




game_intro()
game_loop()
pygame.quit()
quit()

