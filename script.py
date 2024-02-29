
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)  # Color for the ant

# Grid dimensions
cols, rows = 80, 60
cell_size = width // cols

# Initialize grid
grid = np.zeros((rows, cols), dtype=int)

# Ant properties
ant_pos = [rows // 2, cols // 2]  # Start in the middle of the grid
ant_dir = 0  # 0: up, 1: right, 2: down, 3: left

# Directions vectors
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# Main loop flag
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rules of Langton's Ant
    current = grid[ant_pos[1]][ant_pos[0]]
    if current == 0:  # If the cell is white
        ant_dir = (ant_dir - 1) % 4  # Turn left
        grid[ant_pos[1]][ant_pos[0]] = 1  # Flip the color
    else:  # If the cell is black
        ant_dir = (ant_dir + 1) % 4  # Turn right
        grid[ant_pos[1]][ant_pos[0]] = 0  # Flip the color

    # Move the ant
    ant_pos[0] = (ant_pos[0] + directions[ant_dir][0]) % cols
    ant_pos[1] = (ant_pos[1] + directions[ant_dir][1]) % rows

    # Update the display
    screen.fill(white)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                pygame.draw.rect(screen, black, (col * cell_size, row * cell_size, cell_size, cell_size))
    
    # Draw the ant
    pygame.draw.rect(screen, red, (ant_pos[0] * cell_size, ant_pos[1] * cell_size, cell_size, cell_size))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
