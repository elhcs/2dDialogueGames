# gamedialogue.py
import pygame
import sys
from interface import ImageLoaderApp
from PyQt5.QtWidgets import QApplication

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dialogue Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Characters
app = QApplication([])
image_loader = ImageLoaderApp()
image_loader.show()

# Wait for the user to load images
app.exec_()

# Get the selected image paths
image_paths = image_loader.get_selected_image_paths()

# Continue with the rest of the code
character_scale_factor = 4.5

# Load characters and background
characters = [pygame.image.load(path) for path in image_paths[:2]]
background = pygame.image.load(image_paths[2])

# Scale characters if needed
characters = [pygame.transform.scale(char, (int(100 * character_scale_factor), int(100 * character_scale_factor))) for char in characters]

# Scale background
background = pygame.transform.scale(background, (width, height))

# Dialogue
dialogue = [
    (characters[0], "Hello! How are you?"),
    (characters[1], "I'm good, thanks for asking."),
    (characters[0], "What brings you here?"),
    (characters[1], "Just exploring."),
    # Add more dialogue lines as needed
]

# Main game loop
current_line = 0
running = True
skip_dialogue = False

character1_position = (50, 185)  # Adjust the position for character 1
character2_position = (500, 50)  # Adjust the position for character 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # Skip dialogue when Enter key is pressed
            skip_dialogue = True

    # Display background
    screen.blit(background, (0, 0))

    # Display character images
    screen.blit(dialogue[current_line][0], character1_position)

    # Display dialogue
    text_surface = font.render(dialogue[current_line][1], True, black)
    screen.blit(text_surface, (200, 50))

    # Update display
    pygame.display.flip()

    # Wait for a key press to move to the next line
    pygame.time.delay(100)  # Add a delay for better readability

    if skip_dialogue:
        # Move to the next line when Enter key is pressed
        current_line += 1
        skip_dialogue = False

    # Check if all dialogue lines have been displayed
    if current_line >= len(dialogue):
        running = False

# Quit Pygame
pygame.quit()
sys.exit()
