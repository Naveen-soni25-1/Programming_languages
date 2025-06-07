import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("game_character")
screen_rect = screen.get_rect()

# Load and scale image
image = pygame.image.load("images_2/red1.png").convert_alpha()
image = pygame.transform.smoothscale(image, (50, 70))
image_rect = image.get_rect()
image_rect.center = screen_rect.center

# Track float positions separately
pos_x = float(image_rect.x)
pos_y = float(image_rect.y)
rocket_speed = 4

# Movement flags
moving_right = False
moving_left = False 
moving_up = False 
moving_down = False 

def rocket_update():
    global pos_x, pos_y
    if moving_right and image_rect.right < screen_rect.right:
        pos_x += rocket_speed
    if moving_left and image_rect.left > screen_rect.left:
        pos_x -= rocket_speed
    if moving_up and image_rect.top >= screen_rect.top:
        pos_y -= rocket_speed
    if moving_down and image_rect.bottom <= screen_rect.bottom:
        pos_y += rocket_speed

    # Update the rect position using int cast
    image_rect.x = int(pos_x)
    image_rect.y = int(pos_y)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RIGHT:
                moving_right = True
            elif event.key == pygame.K_LEFT:
                moving_left = True 
            elif event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True 

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            elif event.key == pygame.K_LEFT:
                moving_left = False
            elif event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False

    screen.fill((0, 0, 0))
    rocket_update()
    screen.blit(image, image_rect)
    pygame.display.flip()
    clock.tick(60)  # Use clock to maintain smooth 60 FPS
