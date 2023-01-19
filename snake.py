#### Snake Game Tutorial

# import random
# import sys
# import pygame
#
#
#
# # Initialized pygame
# pygame.init()
#
# # Time
# clock = pygame.time.Clock()
#
# # Create screen
# width = 800
# height = 600
# screen = pygame.display.set_mode((width, height))
#
# # Color
# red = (255, 0,0)
# white = (255, 255, 255)
# black = (0,0,0)
#
# # Caption
# pygame.display.set_caption("Snake")
#
# FPS = 50
#
# direction = "right"
#
# apple_img = pygame.image.load("apple.png")
#
# img = pygame.image.load("snak_head.png")
# def snakes(snake_list, snake_width, snake_height):
#     if direction == "right":
#         head = pygame.transform.rotate(img, 270)
#     if direction == "left":
#         head = pygame.transform.rotate(img, 90)
#     if direction == "up":
#         head = img
#     if direction == "down":
#         head = pygame.transform.rotate(img, 180)
#     screen.blit(head, (snake_list[-1][0], snake_list[-1][1]))
#     for snake in snake_list[:-1]:
#         pygame.draw.rect(screen, black, (snake[0],snake[1], snake_width, snake_height))
# #global lead_x, lead_y, lead_x_change, lead_y_change
#
#
# def game_intro():
#     intro = True
#     while intro:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_c:
#                     game_loop()
#                 if event.key == pygame.K_q:
#                     pygame.quit()
#                     quit()
#         screen.fill((255, 255, 255))
#
#         intro_font = pygame.font.SysFont("comicsansms", 70)
#         intro_font2 = pygame.font.SysFont("comicsansms", 30)
#         intro_render = intro_font.render("Snake Game", True, (0, 200, 0))
#         intro_render2 = intro_font2.render("Press C to play and Q to quit", True, (0, 0, 0))
#         screen.blit(intro_render, (180, 100))
#         screen.blit(intro_render2, (180, 300))
#
#         pygame.display.update()
#         clock.tick(15)
#
# def paused():
#     pause = True
#     while pause:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_c:
#                     pause = False
#                 elif event.key == pygame.K_q:
#                     pygame.quit()
#                     quit()
#
#         screen.fill((255, 255, 255))
#
#         pause_font = pygame.font.SysFont(None, 50)
#         pause_font2 = pygame.font.SysFont(None, 30)
#         pause_render = pause_font.render("PAUSED", True, (0,0,0))
#         pause_render2 = pause_font2.render("Press C to continue or Q to quit", True, (0, 0, 0))
#         screen.blit(pause_render, (350, 200))
#         screen.blit(pause_render2, (280, 300))
#         pygame.display.update()
#         clock.tick(5)
#
#
#
# # Game Loop
# def game_loop():
#     global direction
#
#
#     lead_x = width/2
#     lead_y = height/2
#     snake_width = 20
#     snake_height = 20
#     lead_x_change = 0
#     lead_y_change = 0
#     apple_width = 20
#     apple_height = 20
#     snake_list = []
#     snake_length = 1
#     score = 0
#
#
#
#
#     apple_x = round(random.randint(0, width-apple_width))  #/10.0)*10.0
#     apple_y =  round(random.randint(0, height-apple_height)) #/10.0)*10.0
#
#     running = True
#     while running:
#
#
#         screen.fill((white))
#
#         # pygame.draw.rect(screen, (255, 100, 0), (apple_x,apple_y, apple_width, apple_height))
#         screen.blit(apple_img, (apple_x, apple_y))
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#             # Keyboarding Binding
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RIGHT and lead_x_change != -10:
#                     direction = "right"
#                     lead_x_change += 10
#                     lead_y_change = 0
#
#                 if event.key == pygame.K_LEFT and lead_x_change != 10:
#                     direction = "left"
#                     lead_x_change -= 10
#                     lead_y_change = 0
#
#                 if event.key == pygame.K_UP and lead_y_change != 10:
#                     direction = "up"
#                     lead_y_change -= 10
#                     lead_x_change = 0
#
#                 if event.key == pygame.K_DOWN and lead_y_change != -10:
#                     direction = "down"
#                     lead_y_change += 10
#                     lead_x_change = 0
#                 if event.key == pygame.K_p:
#                     paused()
#
#
#
#
#
#
#
#
#
#         snake_head = []
#         snake_head.append(lead_x)
#         snake_head.append(lead_y)
#         snake_list.append(snake_head)
#
#
#         if len(snake_list) > snake_length:
#             del snake_list[0]
#
#         snakes(snake_list, snake_width, snake_height)
#         for each_segment in snake_list[:-1]:
#             if each_segment == snake_head:
#                 gv_font = pygame.font.SysFont("comicsansms", 50)
#                 gv2_font = pygame.font.SysFont("comicsansms", 30)
#                 gv_render = gv_font.render("Game Over", True, red)
#                 gv_render2 = gv2_font.render("Press C to play again or Q to quit", True, black)
#                 screen.blit(gv_render, (280, 200))
#                 screen.blit(gv_render2, (200, 300))
#
#
#                 for event in pygame.event.get():
#                     if event.type == pygame.KEYDOWN:
#                         if event.key == pygame.K_c:
#                             game_loop()
#                             quit()
#                         elif event.key == pygame.K_q:
#
#                             pygame.quit()
#                             quit()
#
#
#         # Collision with border
#
#         if lead_x >= width - snake_width or lead_x <= 0 or lead_y >= height - snake_height or lead_y <= 0:
#             gv_font = pygame.font.SysFont("comicsansms", 50)
#             gv2_font = pygame.font.SysFont("comicsansms", 30)
#             gv_render = gv_font.render("Game Over", True, red)
#             gv_render2 = gv2_font.render("Press C to play again or Q to quit", True, black)
#             screen.blit(gv_render, (280, 200))
#             screen.blit(gv_render2, (200, 300))
#
#             lead_x_change = 0
#             lead_y_change = 0
#
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_c:
#                         game_loop()
#                         quit()
#                     elif event.key == pygame.K_q:
#
#                         pygame.quit()
#                         quit()
#
#
#         # Collision with food
#         # if lead_x == apple_x and lead_y == apple_y:
#         #     apple_x = round(random.randrange(0, width - apple_width) / 10.0) * 10.0
#         #     apple_y = round(random.randrange(0, height - apple_height) / 10.0) * 10.0
#         #     snake_length += 1
#         # if lead_x >= apple_x and lead_x <= apple_x + apple_width:
#         #     if lead_y >= apple_y and lead_y <= apple_y + apple_height:
#         #         apple_x = round(random.randrange(0, width - apple_width))  # /10.0)*10.0
#         #         apple_y = round(random.randrange(0, height - apple_height))  # /10.0)*10.0
#         #         snake_length += 1
#
#         # Collision with apple
#         lead_x += lead_x_change
#         lead_y += lead_y_change
#         if lead_x >= apple_x and lead_x <= apple_x + apple_width or lead_x + snake_width >= apple_x and lead_x + snake_width <= apple_x + apple_width:
#             if lead_y > apple_y and lead_y < apple_y+ apple_height or lead_y + snake_height > apple_y and lead_y + snake_height < apple_y + apple_height:
#
#                 apple_x = round(random.randint(0, width - apple_width))  # /10.0)*10.0
#                 apple_y = round(random.randint(0, height - apple_height))  # /10.0)*10.0
#                 snake_length += 1
#                 score += 1
#
#         score_font = pygame.font.SysFont(None, 30)
#         score_render = score_font.render("score : " + str(score), True, (0, 0, 0))
#         screen.blit(score_render, (0, 0))
#         pygame.display.update()
#         clock.tick(FPS)
#
#
#
#
# game_intro()
# game_loop()
# pygame.quit()
# quit()





























###################
###################
##### My snake Game
import random
import sys

import pygame

# initialize pygame
pygame.init()


# time
clock = pygame.time.Clock()
FPS = 50

#screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))


# color
red = (255, 0,0)
black = (0,0,0)
white = (255, 255, 255)



# caption
pygame.display.set_caption("Snake")






# Game over
def game_over():
    gv_font = pygame.font.SysFont("comicsansms", 50)
    gv_font2 = pygame.font.SysFont("comicsansms", 30)

    gv_render = gv_font.render("Game Over", True, (155, 0,0))
    gv_render2 = gv_font2.render("Press c to continue and q to quit", True, (0, 0, 0))
    screen.blit(gv_render, (300, 200))
    screen.blit(gv_render2, (200, 300))




# Snake Function
snake_img = pygame.image.load("snakkkke_head.png")
apple_img = pygame.image.load("apple.png")

direction = "right"

def snakes(snake_list, snake_width, snake_height):
    if direction == "right":
        head = pygame.transform.rotate(snake_img, 270)
    if direction == "left":
        head = pygame.transform.rotate(snake_img,90)
    if direction == "up":
        head = snake_img
    if direction == "down":
        head = pygame.transform.rotate(snake_img,180)

    screen.blit(head, (snake_list[-1][0], snake_list[-1][1]))
    for snake in snake_list[:-1]:
        pygame.draw.rect(screen, (255, 255, 100), (snake[0], snake[1], snake_width, snake_height))


# Game Intro
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game_loop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        screen.fill((255, 255, 255))
        intro_font = pygame.font.SysFont("comicsansms", 50)
        intro_font2 = pygame.font.SysFont("comicsansms", 30)
        intro_render = intro_font.render("Snake Game", True, (0,255,0))
        intro_render2 = intro_font2.render("Press s to start and q to quit", True, (0, 0, 0))
        screen.blit(intro_render, (250, 200))
        screen.blit(intro_render2, (200, 300))




        pygame.display.update()
        clock.tick(15)


# Paused
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
                    game_loop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        screen.fill((255, 255, 255))
        intro_font = pygame.font.SysFont("comicsansms", 50)
        intro_font2 = pygame.font.SysFont("comicsansms", 30)
        intro_render = intro_font.render("PAUSED!", True, (0,255,0))
        intro_render2 = intro_font2.render("Press c to continue and q to quit", True, (0, 255, 0))
        screen.blit(intro_render, (280, 200))
        screen.blit(intro_render2, (200, 300))


        pygame.display.update()





# Game Loop
def game_loop():
    global direction


    direction = "right"
    lead_x = width/2
    lead_y = height/2
    snake_width = 20
    snake_height = 20
    lead_x_change = 10
    lead_y_change = 0


    apple_width = 20
    apple_height = 20
    snake_list = []
    snake_length = 1
    score = 0

    apple_x = round(random.randint(0, width-apple_width))
    apple_y = round(random.randint(0, height- apple_height))



    running = True
    while running:
        screen.fill((white))


        # pygame.draw.line(surface=screen, color=(0, 255, 0), start_pos=(0, 0), end_pos=(800, 0), width=40)
        # pygame.draw.line(surface=screen, color=(0, 255, 0), start_pos=(0, 600), end_pos=(800, 600), width=40)
        # pygame.draw.line(surface=screen, color=(0, 255, 0), start_pos=(0, 0), end_pos=(0, 600), width=40)
        # pygame.draw.line(surface=screen, color=(0, 255, 0), start_pos=(800, 0), end_pos=(800, 600), width=40)



        pygame.draw.line(screen, (255,0, 0), (0,0), (0,25), 10)
        pygame.draw.line(screen, (255, 0, 0), (0, 50), (0, 75), 10)
        pygame.draw.line(screen, (255, 0, 0), (0, 100), (0, 125), 10)
        pygame.draw.line(screen, (255, 0, 0), (0, 150), (0, 175), 10)
        pygame.draw.line(screen, (255, 0, 0), (0, 200), (0, 225), 10)
        pygame.draw.line(screen, (255, 0, 0), (0, 250), (0, 275), 10)
        pygame.draw.line(screen, (255, 0, 0), (0, 300), (0, 325), 10)
        pygame.draw.line(screen, (255, 0, 0), (0, 350), (0, 375), 10)
        pygame.draw.line(screen, (255, 0, 0), (0, 400), (0, 425), 10)
        pygame.draw.line(screen, (255, 0, 0), (0, 450), (0, 475), 10)
        pygame.draw.line(screen, (255, 0, 0), (0, 500), (0, 525), 10)
        pygame.draw.line(screen, (255, 0, 0), (0, 550), (0, 575), 10)
        pygame.draw.line(screen, (255, 0, 0), (0, 600), (0, 625), 10)











        pygame.draw.line(screen, (255,0, 0), (0, 0), (25, 0), 10)
        pygame.draw.line(screen, (255,0,0), (50, 0), (75, 0), 10)
        pygame.draw.line(screen, (255, 0,0), (100, 0), (125, 0), 10)
        pygame.draw.line(screen, (255, 0,0), (150, 0), (175, 0), 10)
        pygame.draw.line(screen, (255, 0, 0), (200, 0), (225, 0), 10)
        pygame.draw.line(screen, (255, 0, 0), (250, 0), (275, 0), 10)
        pygame.draw.line(screen, (255, 0, 0), (300, 0), (325, 0), 10)
        pygame.draw.line(screen, (255, 0, 0), (350, 0), (375, 0), 10)
        pygame.draw.line(screen, (255, 0, 0), (400, 0), (425, 0), 10)
        pygame.draw.line(screen, (255, 0, 0), (450, 0), (475, 0), 10)
        pygame.draw.line(screen, (255, 0, 0), (500, 0), (525, 0), 10)
        pygame.draw.line(screen, (255, 0, 0), (550, 0), (575, 0), 10)
        pygame.draw.line(screen, (255, 0, 0), (600, 0), (625, 0), 10)
        pygame.draw.line(screen, (255, 0, 0), (650, 0), (675, 0), 10)
        pygame.draw.line(screen, (255, 0, 0), (700, 0), (725, 0), 10)
        pygame.draw.line(screen, (255, 0, 0), (750, 0), (775, 0), 10)
        pygame.draw.line(screen, (255, 0, 0), (790, 0), (800, 0), 10)



        pygame.draw.line(screen, (0, 0, 0), (800, 0), (800, 25), 13)
        pygame.draw.line(screen, (0,0,0), (800, 50), (800, 75), 13)
        pygame.draw.line(screen, (0, 0, 0), (800, 100), (800, 125), 13)
        pygame.draw.line(screen, (0, 0, 0), (800, 150), (800, 175), 13)
        pygame.draw.line(screen, (0, 0, 0), (800, 200), (800, 225), 13)
        pygame.draw.line(screen, (0, 0, 0), (800, 250), (800, 275), 13)
        pygame.draw.line(screen, (0, 0, 0), (800, 300), (800, 325), 13)
        pygame.draw.line(screen, (0, 0, 0), (800, 350), (800, 375), 13)
        pygame.draw.line(screen, (0, 0, 0), (800, 400), (800, 425), 13)
        pygame.draw.line(screen, (0, 0, 0), (800, 450), (800, 475), 13)
        pygame.draw.line(screen, (0, 0, 0), (800, 500), (800, 525), 13)
        pygame.draw.line(screen, (0, 0, 0), (800, 550), (800, 575), 13)
        pygame.draw.line(screen, (0, 0, 0), (800, 600), (800, 625), 13)




        pygame.draw.line(screen, (0, 0, 0), (0, 600), (25, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (50, 600), (75, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (100, 600), (125, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (150, 600), (175, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (200, 600), (225, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (250, 600), (275, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (300, 600), (325, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (350, 600), (375, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (400, 600), (425, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (450, 600), (475, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (500, 600), (525, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (550, 600), (575, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (600, 600), (625, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (650, 600), (675, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (700, 600), (725, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (750, 600), (775, 600), 13)
        pygame.draw.line(screen, (0, 0, 0), (790, 600), (800, 600), 13)






        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            # Keyboard Binding
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and lead_x_change != -10:
                    direction ="right"
                    lead_x_change += 10
                    lead_y_change = 0
                    if lead_x_change ==20:
                        lead_x_change = 10
                if event.key == pygame.K_LEFT and lead_x_change != 10:
                    direction = "left"
                    lead_x_change -= 10
                    lead_y_change = 0
                    if lead_x_change == -20:
                        lead_x_change = -10
                if event.key == pygame.K_UP and lead_y_change != 10:
                    direction = "up"
                    lead_y_change -= 10
                    lead_x_change = 0
                    if lead_y_change == -20:
                        lead_y_change = -10
                if event.key == pygame.K_DOWN and lead_y_change != -10:
                    direction = "down"
                    lead_y_change += 10
                    lead_x_change = 0
                    if lead_y_change == 20:
                        lead_y_change = 10
                if event.key == pygame.K_p:
                    paused()


        screen.blit(apple_img, (apple_x, apple_y))

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)


        if len(snake_list) > snake_length:
            del snake_list[0]


        snakes(snake_list, snake_width, snake_height)


        # bite itself
        for each_segment in snake_list[:-1]:
            if each_segment == snake_head:
                lead_x_change = 0
                lead_y_change = 0
                game_over()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            game_loop()
                            quit()
                        if event.key == pygame.K_q:
                            pygame.quit()
                            quit()

        lead_x += lead_x_change
        lead_y += lead_y_change

        # Collision with apple
        if lead_x > apple_x and lead_x < apple_x + apple_width or lead_x + snake_width > apple_x and lead_x + snake_width < apple_x + apple_width:
            if lead_y > apple_y and lead_y < apple_y + apple_height or lead_y + snake_height > apple_y and lead_y + snake_height < apple_y + apple_height:
                apple_x = round(random.randint(0, width - apple_width))
                apple_y = round(random.randint(0, height - apple_height))
                snake_length += 1
                score += 1
        score_font = pygame.font.SysFont(None, 40)
        score_render = score_font.render("score : " + str(score), True, (255, 200, 100))
        screen.blit(score_render, (10, 10))


        # Border Collision
        if lead_x > width-snake_width or lead_x < 0 or lead_y > height-snake_height or lead_y < 0:
            lead_y_change = 0
            lead_x_change = 0
            game_over()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        game_loop()
                        quit()
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                        sys.exit()

        pygame.display.update()
        clock.tick(FPS)


game_intro()
game_loop()
pygame.quit()
quit()


















