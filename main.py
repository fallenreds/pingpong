import pygame

pygame.init()

background_color = (0, 155, 255)
window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Самая лучшая в мире игра")
window.fill(background_color)
clock = pygame.time.Clock()


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img, x,y, width, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

a = GameSprite("imgs/ball.png", 0,0, 100, 100)


game = True
while game:

    window.fill(background_color)
    a.reset()
    # window.blit(ball, (0,0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()


    pygame.display.update()
    clock.tick(60)
