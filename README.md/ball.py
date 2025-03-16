import pygame
import sys


pygame.init()


screen_width, screen_height = 400, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move the Ball")


ball_radius = 25
ball_color = (255, 0, 0) 
ball_x, ball_y = screen_width // 2, screen_height // 2  


clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_UP]:
        if ball_y - ball_radius > 0:  
            ball_y -= 20
    if keys[pygame.K_DOWN]:
        if ball_y + ball_radius < screen_height:  
            ball_y += 20
    if keys[pygame.K_LEFT]:
        if ball_x - ball_radius > 0:  
            ball_x -= 20
    if keys[pygame.K_RIGHT]:
        if ball_x + ball_radius < screen_width:  
            ball_x += 20


    screen.fill((255, 255, 255))


    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)


    pygame.display.flip()


    clock.tick(60)


pygame.quit()
sys.exit()
