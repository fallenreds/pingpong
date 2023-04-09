import pygame
pygame.init()

background_color = (0, 155, 255)
window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Самая лучшая в мире игра")
window.fill(background_color)
clock = pygame.time.Clock()



while True:
    window.fill(background_color)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    pygame.display.update()
    clock.tick(60)