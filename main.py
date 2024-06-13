from pygame import *
init()

W = 800
H = 500

window = display.set_mode((W, H))
bg = transform.scale(image.load('sto.png'), (W, H))# Трансформуємо картинку в розміри вікна

clock = time.Clock()# Лічильник кадрів

font.init()
font1 = font.SysFont('Arial', 30, bold=True)
font2 = font.SysFont('Arial', 50, italic=True)

class GameSprite(sprite.Sprite): # Базовий клас для всіх спрайтів
    def __init__(self, img, x, y, width, height, speed_x, speed_y):# Конструктор класу
        super().__init__()
        self.image = transform.scale(image.load(img), (width, height))#
        self.rect = self.image.get_rect()# Автоматичне створення хіт боксу
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.width = width
        self.height = height
    
    def draw(self): # Малювання картинки
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite): # Класс для гравців
    def update_l(self): # Управління лівого гравця
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_s] and self.rect.y < H - self.height:
            self.rect.y += self.speed_y

    def update_r(self):# управління правого гравця
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_DOWN] and self.rect.y < H - self.height:
            self.rect.y += self.speed_y


class Ball(GameSprite):
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y -= self.speed_y

player1 = Player('батут2.png', 5, 5, 110, 100, 10, 10)
player2 = Player('батут1.png', 700, 250, 110, 100, 10, 10)
ball = Ball('koleso.png', W / 2, H / 2, 70, 70, 4, 4)

player1_points = 0
player2_points = 0

game = True
while game:
    window.blit(bg, (0, 0))
    player1.draw()
    player2.draw()
    ball.draw()

    player1.update_l()
    player2.update_r()

    player1_txt = font2.render(str(player1_points), 1, (0, 0, 0))
    player2_txt = font2.render(str(player2_points), 1, (0, 0, 0))
    window.blit(player1_txt, (100, 10))
    window.blit(player2_txt, (700, 10))

    ball.move()
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if sprite.collide_rect(player1, ball) or sprite.collide_circle(player2, ball):
        ball.speed_x *= -1
    
    if ball.rect.y < 0 or ball.rect.y > H - ball.height:
        ball.speed_y *= -1

    if ball.rect.x <  0:
        player2_points += 1
        ball.rect.x = W / 2
        ball.rect.y = H / 2

    if ball.rect.x > W:
        player1_points += 1
        ball.rect.x = W / 2
        ball.rect.y = H / 2


    clock.tick(100)
    display.update()
    