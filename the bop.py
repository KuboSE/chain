import pygame
import sys
# import playsound
# Your system will throw an error if you don't have PyGame installed. 
# Run 
# python3 -m pip install pygame==2.0.0 
# if this throws an error at all for you.

# Declan Fletcher,
# part of Kubo Engineering, 
# 2022.
# Some assembly required.

# Eat your heart out, Square Enix 
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("peep the horror")
     
    # This will define the actual surface of the window.
    screen_width = 600
    screen_height = 480
    screen = pygame.display.set_mode((screen_width,screen_height))

    running = True
    image = pygame.image.load("de_shogun.png").convert() # In this, our image and its hitbox.
    xpos = 18
    ypos = 18
    
    platformx = 0
    platformy = 448
    platformthicc = 100
    # Our platform rect. Should make this a function for repeating. 
    platformRect = pygame.Rect(platformx, platformy, screen_width, platformthicc)
    # This gravity chain accumulates gravity.
    gravity = .00001
    kokomo = 0
    speed = 0

    ching = .1 # PyGame doesn't use any specific variable for speed, 
    cheng = .2 # but this specifies horizontal and vertical movement.
    
    movingLeft = False  # These create more smooth movement. 
    movingRight = False # I should debounce the vertical as well... 
    pygame.mixer.music.load("nokia.wav")
    pygame.mixer.music.play(-1)
    
    while running:
        # Keystrikes, those held down too, borrow from "keys."
        # I learned the hard way that booleans use uppercase True and False.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            xpos -= ching 
            movingLeft = True
        if keys[pygame.K_d]: 
            xpos += ching
            movingRight = True
        if keys[pygame.K_SPACE]:
            ypos -= cheng
        if keys[pygame.K_s]:
            ypos += cheng
        if keys[pygame.K_ESCAPE]:
            running = False
                # change the value to False, to exit the main loop
        
        # Smoothes jumping. 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ypos += cheng
        pygame.display.update() # no fucking clue what this does tbh
        
        # The smoothing.
        if gravity > 0 and movingLeft:
            xpos -= ching
        if gravity > 0 and movingRight:
            xpos += ching
        
        # Defines collision and color variables.
        # Collision can be made into a function, which it is. 
        # [icon.get_rect(topleft = (whereever, whenever)).inflate(8, 8))] 
        # tends to be the preferred.
        collision = platformRect.colliderect(image.get_rect(topleft=(xpos, ypos)).inflate(8, 8))
        color = (255, 255, 255)
        if collision: # Kokomo 
            gravity = 0
            kokomo = 0
            speed = 0
            ypos -= cheng
            movingLeft = False
            movingRight = False
        if ypos <= (screen_height - platformthicc/2 - .08): # Aruba
            gravity = .00012 # Jamaica
        if xpos > screen_width-16: # Ooh, I wanna take ya'
            xpos -= 32 + ching # Bermuda
        if xpos < 0: # Bahama, 
            xpos += ching+16 # C'mon, pretty mama 
        if ypos > screen_height-16: # Key Largo,
            ypos -= cheng # Montego, 
        if ypos < 0: # Baby, why don't we go 
            ypos += cheng # ... off the florida keys ... 
            
        # This is a place called Kokomo 
        kokomo += gravity
        ypos += speed + kokomo
        
        screen.fill((0,0,150)) # bodies in the saaand 
        pygame.draw.rect(screen, color, platformRect) # tropical drink melting in your hand 
        screen.blit(image, (xpos,ypos))  # we'll be falling in love to the sound of a steel drum band
        for event in pygame.event.get(): # oh by the way this is the quit event. 
            # The stuff you see above starting at the screen.fill requires being in order.
            if event.type == pygame.QUIT: # Otherwise it won't draw correctly, 
                running = False # there's literally nothing to just clean the screen and 
                # per efficiency terms, I prefer it messy.
        
        
# by the way if you take this out nothing works 
if __name__=="__main__":
    # importing it as as module makes it just not work. Make this program your main module.
    main()