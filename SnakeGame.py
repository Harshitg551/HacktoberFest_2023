import pygame
import time
import random

pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Snake properties
snake_block = 20
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)

clock = pygame.time.Clock()

# Snake
snake_list = []

# Initialize snake position
snake_head = [screen_width // 2, screen_height // 2]
snake_list.append(snake_head)

# Initial movement direction
direction = "RIGHT"

# Food properties
food_block = 20
food_x = round(random.randrange(0, screen_width - food_block) / 10.0) * 10.0
food_y = round(random.randrange(0, screen_height - food_block) / 10.0) * 10.0

# Score
score = 0

# Display score
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

# Main game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
            elif event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

    # Move the snake
    if direction == "LEFT":
        snake_head[0] -= snake_block
    elif direction == "RIGHT":
        snake_head[0] += snake_block
    elif direction == "UP":
        snake_head[1] -= snake_block
    elif direction == "DOWN":
        snake_head[1] += snake_block

    snake_head_copy = list(snake_head)
    snake_list.append(snake_head_copy)

    # Check if snake has eaten the food
    if snake_head[0] == food_x and snake_head[1] == food_y:
        score += 1
        food_x = round(random.randrange(0, screen_width - food_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - food_block) / 10.0) * 10.0
    else:
        snake_list.pop(0)

    # Check if snake has collided with the wall or itself
    if snake_head[0] >= screen_width or snake_head[0] < 0 or snake_head[1] >= screen_height or snake_head[1] < 0:
        game_over = True
    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    screen.fill(black)

    # Draw the snake and food
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

    pygame.draw.rect(screen, red, [food_x, food_y, food_block, food_block])
    
    Your_score(score)

    pygame.display.update()

    clock.tick(snake_speed)

# Display "Game Over" message
font_style = pygame.font.SysFont(None, 75)
game_over_msg = font_style.render("Game Over", True, white)
screen.blit(game_over_msg, [screen_width / 2 - 200, screen_height / 2 - 50])
Your_score(score)
pygame.display.update()

time.sleep(2)

pygame.quit()
