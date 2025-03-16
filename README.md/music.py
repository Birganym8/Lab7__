import pygame
import os
import time

pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Music Player")


music_folder = "music" 
music_files = ['Rick-Roll-Sound-Effect.mp3', 'kto-takie-fiksiki.mp3']
current_track = 0


if music_files:
    pygame.mixer.music.load(os.path.join(music_folder, music_files[current_track]))


def play_music():
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_folder, music_files[current_track]))
    play_music()


def previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_folder, music_files[current_track]))
    play_music()


running = True
playing = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  
                if not playing:
                    play_music()
                    playing = True
            elif event.key == pygame.K_s:  
                stop_music()
                playing = False
            elif event.key == pygame.K_n:  
                next_track()
                playing = True
            elif event.key == pygame.K_b:
                previous_track()
                playing = True

   
    screen.fill((255, 255, 255))  
    pygame.display.flip()
    
    
    time.sleep(0.1)


pygame.quit()
