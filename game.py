import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('My First Game')

# Player settings
player_color = (255, 0, 0)  # Red color
player_size = 50
player_x = width // 2
player_y = height // 2
player_speed = 0.5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movement controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    
    # Fill the screen with black
    screen.fill((0, 0, 0))
    
    # Draw the player character
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))
    
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
