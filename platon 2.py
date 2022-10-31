import sys
import  pygame



class Ship():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("D:/Program Files/ПРОЭКТЫ ПИТОНА/8.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right:
            self.rect.x += 4
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            self.rect.x = self.x
    def update2(self):
        if self.moving_left:
            self.rect.x -= 4
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            self.rect.x = self.x
    def light(self):
        self.screen.blit(self.image, self.rect)








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
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.ship.moving_right = False
                elif event.key == pygame.K_a:
                    self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.light()
        pygame.display.flip()



class Settings():
    def __init__(self):
        self.settings = Settings
        self.bg_color = (100, 50, 200)
        self.ship_speed = 1.5
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width =  self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height


if __name__ == '__main__':
    tg = Testgame()
    tg.rungame()
