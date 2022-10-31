import sys

import  pygame
from pygame.sprite import Sprite


class Enemy(Sprite ):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("D:/Program Files/ПРОЭКТЫ ПИТОНА/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

def light(self):
        self.screen.blit(self.image, self.rect)

def __init__(self):
    self.enemies = pygame.sprite.Group()
    self._create_fleet()






class Ship():
    def _create_fleet(self):
        enemy = Enemy(self)
        self.enemies.add(enemy)

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("D:/Program Files/ПРОЭКТЫ ПИТОНА/8.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        def update_screen(self):
            self.enemies.draw(self.screen)
            pygame.display.flip()

    def update(self):
        if self.moving_right:
            self.rect.x += 4
    def update2(self):
        if self.moving_left:
            self.rect.x -= 4
    def light(self):
        self.screen.blit(self.image, self.rect)


class Settings():
    def __init__(self):
        self.screen_width = 1850
        self.screen_height = 1000
        self.bg_color = (100, 50, 200)

class Testgame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        pygame.display.set_caption('Никита')
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)

    def rungame(self):
        while True:
            self._update_screen()
            self.ship.update()
            self.ship.update2()
            self._check_events()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:

                    self.ship.moving_right = True
                elif event.key == pygame.K_a:
                        self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.ship.moving_right = False
                elif event.key == pygame.K_a:
                    self.ship.moving_left = False


    def _update_screen(self):

        self.screen.fill(self.settings.bg_color)
        self.ship.light()
        pygame.display.flip()




if __name__ == '__main__':
    tg = Testgame()
    tg.rungame()


