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
    def __init__(self,  k_up, k_down, obj):
        self.obj = obj
        self.k_up = k_up
        self.k_down = k_down

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.k_up] and self.obj.rect.y>0:
            self.obj.rect.y -= 5
        if keys[self.k_down] and self.obj.rect.y<500-self.obj.rect.height:
            self.obj.rect.y += 5



game = True


class Player(GameSprite):
    def __init__(self, img, x, y, width, height, k_up, k_down, rotation=None):
        super().__init__(img, x, y, width, height, rotation)
        self.controller = Controller(k_up, k_down, self)
        self.score = 0

    def reset(self):
        super().reset()
        self.controller.update()


player1 = Player("imgs/platform.png", 30, 0, 100, 25, pygame.K_UP, pygame.K_DOWN,  90)
player2 = Player("imgs/platform.png", 730, 0, 100, 25, pygame.K_w, pygame.K_s, 90)


#відобразити картинку і прямокутник
#Постійний рух

ball = GameSprite("imgs/tenis_ball.png", 400, 250, 50,50)
dx = 3
dy = -3

win_variant = 2


score_font = pygame.font.Font(None, 35)


is_menu = True
while game:

    score = f"{player1.score}:{player2.score}"
    score_text = score_font.render(score, True, (0,0,0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_F1]:
        win_variant=1
    if keys[pygame.K_F2]:
        win_variant=2




    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False


    if is_menu:
        text = score_font.render("Prey any key to continue", True, (0,0,0))
        text2 = score_font.render("F1 to v1, F2 to v2", True, (0, 0, 0))
        window.blit(text, (300, 250))
        window.blit(text2, (300, 290))
        keys = pygame.key.get_pressed()
        if True in keys and not keys[pygame.K_ESCAPE]:
            is_menu=False


    else:
        window.fill(background_color)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            is_menu = True

        player1.reset()
        player2.reset()
        ball.reset()
        window.blit(score_text, (380, 30))

        if ball.rect.y >500-ball.rect.width or ball.rect.y <0:
            dy *= -1

        if ball.rect.x >800-ball.rect.width:
            player1.score+=1
            print(player1.score)


            if win_variant==1:
                dx*=-1


            if win_variant==2:
                ball.rect.x = 400
                ball.rect.y = 250

        if ball.rect.x <0:
            player2.score+=1
            print(player2.score)

            if win_variant==1:
                dx*=-1


            if win_variant==2:
                ball.rect.x = 400
                ball.rect.y = 250





        if ball.rect.colliderect(player1):
            dx *= -1
            ball.rect.left = player1.rect.right


        if ball.rect.colliderect(player2):
            dx *= -1
            ball.rect.right = player2.rect.left

        ball.rect.x += dx
        ball.rect.y += dy



    pygame.display.update()
    clock.tick(60)
