import pygame
pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
background_img = pygame.image.load('images/background.png')
background_img = pygame.transform.scale(background_img, (400, 600))
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)
    screen.blit(background_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()  
