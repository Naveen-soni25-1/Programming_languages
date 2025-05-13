import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blue Sky")
screen.fill((135, 206, 235))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    pygame.time.delay(100) # delay to limit the frame rate.
