#Faça um programa em Python que abra e reproduza o áudio de arquivo MP4.

import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
