import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("game_character")
screen.fill((118, 156, 156))
screen_rect = screen.get_rect()
image = pygame.image.load("images_2/game_character.jpg").convert()
image = pygame.transform.smoothscale(image, (495, 700))
image_rect = image.get_rect()

image_rect.center = screen_rect.center

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.blit(image, image_rect)    
    pygame.display.flip()
    pygame.time.delay(100) # delay to limit the frame rate.
