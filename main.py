import pygame

# Initialize Pygame
pygame.init()

# Set up window size
window_width = 640
window_height = 480
screen = pygame.display.set_mode((window_width, window_height))

# Set window caption
pygame.display.set_caption("My First Game Screen")

# Define colors
WHITE = (255, 255, 255)
RECT_COLOR = (0, 128, 255)  # You can change this to any color

# Define font for text
font = pygame.font.SysFont(None, 48)
text = font.render("Hello, Pygame!", True, (0, 0, 0))  # Text with black color

# Get text rectangle to center the text
text_rect = text.get_rect(center=(window_width // 2, window_height // 2 - 100))

# Define the rectangle (width, height)
rect_width = 150
rect_height = 100
rect_x = (window_width // 2) - (rect_width // 2)  # Centering the rectangle
rect_y = (window_height // 2) - (rect_height // 2)
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with white background
    screen.fill(WHITE)

    # Draw the rectangle in the center of the screen
    pygame.draw.rect(screen, RECT_COLOR, rect)

    # Display the text
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()