back = (200, 255, 255)
window = display.set_mode((600, 500))
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400 - 80: 
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 700 - 80: 
            self.rect.y += self.speed     
        
racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = GameSprite("tennis_ball.png", 200, 200, 4, 50, 50)

while game:
  for e in event.get():
    if e.type == QUIT:
      game = False
      
      if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect_x += speed_x
        ball.rect_y += speed_y
  
  
game = True
finish = False
clock = time.Clock()
FPS = 60            
  
          
        
