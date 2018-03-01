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

# get sound
crash_sound = pygame.mixer.Sound("crash.wav")  
pygame.mixer.music.load("bird.wav")

display_width = 500
display_height = 400

# set colors
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,230,0)
bright_green = (0,255,0)

# set birds
bird_width = 40
bird_height = 32

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Flappy bird')
clock = pygame.time.Clock()

# get the images for background and bird
birdImg = pygame.image.load('forwardbird3.png')
background = pygame.image.load('background.png')
background2 = pygame.image.load('background2.png')

pause = False # define and set pause to false

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
    TextRect.center = ((display_width/2), (160))
    gameDisplay.blit(TextSurf, TextRect)
    
# Game is over
def die():
    # set the music
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    message_display('Game Over')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              quitgame()
        # Call button method
        button("Play Again!", 100, 300, 150, 50, green, bright_green, game_loop)
        button("Quit", 300, 300, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)

#define the start button method
#the method pass a message, x and y coordinates, width, height, a inactive collor, a active collor and a action/method
def button(msg,x,y,w,h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos() # Grab mouse position
    click = pygame.mouse.get_pressed() # Get the click
    # Create the start and quit buttons
    if x+w > mouse[0] > x and y+h > mouse[1] > y: # If the mouse cursor is over the button
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h)) # Color the mouse lighter to look interactive
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(msg, smallText)   #set the tesx and the font and type of text inside the rectangle where will be the text 
    TextRect.center = ((x+(w/2)), (y+(h/2))) #set this mesage in the center of screen
    gameDisplay.blit(TextSurf, TextRect)

# Define the quit game method
def quitgame():
    pygame.quit()
    quit()


# The game intro method
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()


        # display the background
        gameDisplay.blit(background2, (0,0))
 #       gameDisplay.fill(white)
        # display the message on the screen
        message_display('Flappy Bird')
        # Call button method
        button("PLAY!", 100, 300, 100, 50, green, bright_green, game_loop)
        button("Quit", 300, 300, 100, 50, red, bright_red, quitgame)
       
        pygame.display.update()
        clock.tick(15)

# The unpause method
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    

# Define the game pause method
def paused():
    pygame.mixer.music.pause() # stop the music
    
    message_display('Paused')
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
 
        # Call button method
        button("Continue", 100, 300, 100, 50, green, bright_green, unpause)
        button("Quit", 300, 300, 100, 50, red, bright_red, quitgame)
       
        pygame.display.update()
        clock.tick(15)       

# The main game loop
def game_loop():

     # set the music
    pygame.mixer.Sound.stop(crash_sound)
    pygame.mixer.music.play(-1) # -1 will play the music in a loop
    global pause
    
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
                quitgame()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_bird_change = -6
                if event.key == pygame.K_p: # if 'p' is pressed then pause the game
                    pause = True
                    paused()  # call the paused method
            elif event.type == pygame.MOUSEBUTTONDOWN:
                y_bird_change = -6
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    y_bird_change = 0
            elif event.type == pygame.MOUSEBUTTONUP:
                y_bird_change = 0


        y_bird = y_bird + y_bird_change + 3

        if (y_bird < -10) :
            y_bird = -10

        # display the background
        gameDisplay.blit(background, (0,0))

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

#call the intro
game_intro()
#call the game loop
game_loop()
quitgame()
