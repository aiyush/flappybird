import pygame, sys

# 14.) Until now the moving floor isnt continuously repeating in loop
#      so we need to merge two floors together that will give an illusion
#      of continuous repetition

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,900))
    screen.blit(floor_surface,(floor_x_pos + 576,900))# adding a new movable floor image after 576px,ie at the end of 1st floor

# 23.) Creating pipes
def create_pipes():
    new_pipes = pipes.get_rect(midtop = (188,312))
    return new_pipes

# 24.) Making the pipes move by creating a new list
def move_pipes(pipess):
    for pipe in pipess:
        pipe.centerx -= 5
    return pipess

# 26.) drawing the pipes from list(in step 25) to screen
def draw_pipes(pipe_list):
    screen.blit(pipes,(pipes_list))
    
# 1.) Initializing our game
pygame.init()

# 2.) Creating a screen - width of 576 and height of 1024
screen = pygame.display.set_mode((576,1024))

# 3.) Setting FPS for the game
fps = pygame.time.Clock()

# 17.) Now creating game variables
gravity = 0.25
bird_movement = 0

# 5.) Importing and displaying images on the screen now. 
bg_surface = pygame.image.load("flappy-bird/assets/background-day.png").convert()
# 7.) After loading the background image,we have to scale it now 
#     to fit the screen
bg_surface = pygame.transform.scale2x(bg_surface)

# 8.) Now putting another image on top of the background image that will
#     move.
floor_surface = pygame.image.load("flappy-bird/assets/base.png").convert()
# 10.) Scaling the moveable image - floor
floor_surface = pygame.transform.scale2x(floor_surface)
# 11.) declaring variable for making the floor move in x direction
floor_x_pos = 0

# 20.) Displaying pipes now
pipes = pygame.image.load("flappy-bird/assets/pipe-green.png").convert()
# pipes = pygame.transform.scale2x(pipes)
pipes_list = []
SPAWNPIPES = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPES,1200)

# 17.) Now placing the bird on the screen
bird = pygame.image.load("flappy-bird/assets/bluebird-midflap.png").convert()
bird = pygame.transform.scale2x(bird)
# rect creates a rectangle over an object.Used for detecting collisions
bird_rect = bird.get_rect(center = (100,512))

# 4.) Until now we were getting the screen for just a second
#  changing that to forever until we quit

while True:
    for event in pygame.event.get():
        #for closing the pygame,otherwie the loop will run forever
        if event.type == pygame.QUIT:
            pygame.quit()
            #without sys.exit the code will show error coz the program
            #terminates while in a loop
            sys.exit()

        # 19.) making the bird move by pressing a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 12

        # 22.) Making the pipes spawn continuously
        if event.type == SPAWNPIPES:
            pipes_list.append(create_pipes()) # this hasnt been created yet...creating it in step 23
            print(pipes_list)

    # 6.) displaying the background image on screen
    screen.blit(bg_surface,(0,0))
    # displaying moveable bird
    screen.blit(bird,bird_rect)
    # 21.) Displaying pipes
    screen.blit(pipes,(10,2))
    # 25. ) Taking the pipes list from step 22 and making it pass through move_pipes function 
    # to create a new list with new co ordinates....giving it an illusion of movement
    pipes_list = move_pipes(pipes_list)

    # 27.) making the pipes visible on the screen
    # draw_pipes(pipes_list)

    # 18.) Applying game variables
    bird_movement += gravity
    bird_rect.centery += bird_movement

    # 12.) Now making the moveable image move - floor
    floor_x_pos -= 1
    # 9.) displaying moveable image on the screen - floor
    # 13.) changing the x coordinate of the screen so that the
    #      screen seems moving(changing 0 with floor_x_pos)
    #screen.blit(floor_surface,(floor_x_pos,900)) 
    # 15.) after step 14,we do not need the above method,instead we use
    draw_floor()

    # 16.) To tackle the problem of running out of floor image in step 14,we use
    if floor_x_pos <= -576:
        floor_x_pos = 0

    pygame.display.update()
    fps.tick(120)

