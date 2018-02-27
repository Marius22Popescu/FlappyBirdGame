# Norman Lew & Marius Popescu
# CS 320
# Winter 2018

# Assignment 3

# This code fulfills the requirements for Assignment 3.  Assignment 3 calls for implementing a Flappy Bird type game.

# The template for this code was taken from: 
# https://pythonprogramming.net/game-development-tutorials/
# A step by step tutorial is provided by this website to get started with a Python game using pygame

import pygame
import time
import random

pygame.init()

display_width = 500
display_height = 400

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

bird_width = 40
bird_height = 32

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Flappy bird')
clock = pygame.time.Clock()

birdImg = pygame.image.load('forwardbird3.png')

# This method will count the number of pipes passed and keep the score
def pipe_score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("SCORE: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

# Function that draws the pipe to the screen
def pipe(pipeX, pipeY, pipeW, pipeH, color):
    pygame.draw.rect(gameDisplay, color, [pipeX, pipeY, pipeW, pipeH])

# Function that draws the bird to the screen
def bird(x,y):
    gameDisplay.blit(birdImg,(x,y))

# Function to return a text object
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Function to display a message to the center of the screen
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    game_loop() # erase when is redy
    
# Game is over
def die():
    message_display('Game Over')

# The main game loop
def game_loop():
    x_bird = (display_width * 0.05)
    y_bird = (display_height * 0.4)

    x_bird_change = 0
    y_bird_change = 0  

    # This is the first set of pipes.  A set of pipes consists of a pipe protruding from the top of the screen and another one protruding from the bottom of the screen
    pipe_x = display_width
    pipe_y = random.randrange(195, display_height)
    pipe_speed = 2
    pipe_width = 60
    pipe_height = display_height - pipe_y

    pipe_x2 = display_width
    pipe_y2 = 0
    pipe_height2 = pipe_y - 200 

    # This is the second set of pipes.
    pipe_x3 = display_width + 275
    pipe_y3 = random.randrange(195, display_height)
    pipe_height3 = display_height - pipe_y3

    pipe_x4 = display_width + 275
    pipe_y4 = 0
    pipe_height4 = pipe_y3 - 200

    score = 0 

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_bird_change = -5
            if event.type == pygame.MOUSEBUTTONDOWN:
                y_bird_change = -5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    y_bird_change = 0
            if event.type == pygame.MOUSEBUTTONUP:
                y_bird_change = 0


        y_bird = y_bird + y_bird_change + 3

        if (y_bird < -10) :
            y_bird = -10

        gameDisplay.fill(white)

        # When a pipe has disappeared from the screen, create a new pipe for the player to go between
        if (pipe_x < (0 - pipe_width)) :
            pipe_x = display_width
            pipe_y = random.randrange(200, display_height)
            pipe_height = display_height - pipe_y

            pipe_x2 = display_width
            pipe_y2 = 0
            pipe_height2 = pipe_y - (200 - 3*score) #narrow the hole in the pipe
            score += 1 # increase the score
            pipe_speed += score*0.03 # increase the speed 

        if (pipe_x3 < (0 - pipe_width)) :
            pipe_x3 = display_width
            pipe_y3 = random.randrange(200, display_height)
            pipe_height3 = display_height - pipe_y3

            pipe_x4 = display_width
            pipe_y4 = 0
            pipe_height4 = pipe_y3 - (200 - 3*score) #narrow the hole in the pipe
            score += 1 # increase the score
            pipe_speed += score*0.03 # increase the speed
        
        # Update the location of the pipes and the bird
        pipe_x -= pipe_speed
        pipe(pipe_x, pipe_y, pipe_width, pipe_height, green)
        pipe_x2 -= pipe_speed
        pipe(pipe_x2, pipe_y2, pipe_width, pipe_height2, green)
        

        pipe_x3 -=   pipe_speed
        pipe(pipe_x3, pipe_y3, pipe_width, pipe_height3, green)
        pipe_x4 -= pipe_speed
        pipe(pipe_x4, pipe_y4, pipe_width, pipe_height4, green)

        # show the bird
        bird(x_bird,y_bird)
        pipe_score(score)

        pygame.display.update()

        # If a bird has fallen below the playing screen or has run into a pipe, the game is over
        if (y_bird > display_height or ((x_bird + bird_width > pipe_x and x_bird < pipe_x + pipe_width) and (y_bird + bird_height > pipe_y or y_bird < (pipe_y2 + pipe_height2 -5))) or ((x_bird + bird_width > pipe_x3 and x_bird < pipe_x3 + pipe_width) and (y_bird + bird_height > pipe_y3 or y_bird < (pipe_y4 + pipe_height4 -5)))):
            die()
            gameExit = True

        
        clock.tick(60)

game_loop()
pygame.quit()
quit()
