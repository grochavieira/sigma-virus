import pygame
import sys
import random

# Setup padrão
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# Janela principal
screen_width = 960  # largura
screen_height = 720  # altura

screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

display = pygame.Surface((600, 400))

pygame.display.set_caption("Sigma Virus")  # titulo

bg_color = pygame.Color("#e5e5e5")  # cor de fundo
font_color = pygame.Color("#ffffff") # cor da fonte
black_font_color = pygame.Color("#000000") # cor da fonte
basic_font = pygame.font.Font("fonts/8-BIT-WONDER.ttf", 20)  # carrega a fonte

slow_time = 1

# sons de efeito
laser_sound = pygame.mixer.Sound(
    "audio/laser.wav")
destroy_sound = pygame.mixer.Sound("audio/destroy.wav")
hit_sound = pygame.mixer.Sound("audio/hit.wav")
button_sound = pygame.mixer.Sound("audio/button.wav") 
slow_time_sound = pygame.mixer.Sound("audio/slow_time.mp3") 
time_resume_sound = pygame.mixer.Sound("audio/time_resume.mp3") 

# score do jogo
score = 0
moving_bg = 0

# level collisions 
collision_level = 0
collision_wall = 0