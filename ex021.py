#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('C:\Users\joao.mfrodrigues\Downloads\SENAC---DESENVOLVIMENTO-DE-SISTEMAS\ex021.mp3')
pygame.event.wait()
