import pygame
import sys
import math
import time


pygame.init()


clock_img = pygame.image.load('C:/Users/User/OneDrive/Рабочий стол/LABS/Lab7/images/clock.png')
left_arm_img = pygame.image.load('C:/Users/User/OneDrive/Рабочий стол/LABS/Lab7/images/leftarm.png')
right_arm_img = pygame.image.load('C:/Users/User/OneDrive/Рабочий стол/LABS/Lab7/images/rightarm.png')


screen = pygame.display.set_mode((clock_img.get_width(), clock_img.get_height()))
pygame.display.set_caption("Mickey Clock")


center = (clock_img.get_width() // 2, clock_img.get_height() // 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    
    second_angle = -6 * seconds 
    minute_angle = -6 * minutes   

    
    left_arm_rotated = pygame.transform.rotate(left_arm_img, second_angle)
    right_arm_rotated = pygame.transform.rotate(right_arm_img, minute_angle)

    
    left_arm_rect = left_arm_rotated.get_rect(center=center)
    right_arm_rect = right_arm_rotated.get_rect(center=center)

    
    screen.blit(clock_img, (0, 0))
    screen.blit(left_arm_rotated, left_arm_rect.topleft)
    screen.blit(right_arm_rotated, right_arm_rect.topleft)

    
    pygame.display.flip()
    pygame.time.Clock().tick(60)
