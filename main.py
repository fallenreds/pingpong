import pygame

pygame.init()

background_color = (0, 155, 255)
window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Самая лучшая в мире игра")
window.fill(background_color)
clock = pygame.time.Clock()


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img, x, y, width, height, rotation=None):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img), (width, height))

        if rotation:
            self.image = pygame.transform.rotate(self.image, rotation)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def rotate(self, degree):
        self.image = pygame.transform.rotate(self.image, degree)
        self.rect = self.image.get_rect()




class Controller:
    def __init__(self, obj, k_up, k_down):
        self.obj = obj
        self.k_up = k_up
        self.k_down = k_down

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.k_up]:
            self.obj.rect.y -= 5
        if keys[self.k_down]:
            self.obj.rect.y += 5



game = True


class Player(GameSprite):
    def __init__(self, img, x, y, width, height, k_up, k_down, rotation=None):
        super().__init__(img, x, y, width, height, rotation)
        self.controller = Controller(self, k_up, k_down)

    def reset(self):
        super().reset()
        self.controller.update()


player1 = Player("imgs/platform.png", 0, 0, 100, 25, pygame.K_UP, pygame.K_DOWN,  90)
player2 = Player("imgs/platform.png", 300, 0, 100, 25, pygame.K_w, pygame.K_s)




while game:

    window.fill(background_color)
    player1.reset()
    player2.reset()



    # window.blit(ball, (0,0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()

    pygame.display.update()
    clock.tick(60)
