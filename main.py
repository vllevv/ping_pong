from pygame import *
'''Необходимые классы'''

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_sprite):
        super().__init__()
        self.image - transform.scale(image.load(player_image)
        self.speed - player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.x = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_widgth - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_widgth - 80:
            self.rect.y += self.speed
        


