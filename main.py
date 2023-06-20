import pygame
import random
pygame.init()
Rate = 500
Speed = 1
Score = 0
Color = ""
end = 0
Blop_SFX = pygame.mixer.Sound("Assets/Blop.mp3")
BloonsType = ["Assets/red.png", "Assets/red.png", "Assets/red.png", "Assets/red.png", "Assets/red.png", "Assets/red.png", "Assets/blue.png", "Assets/blue.png", "Assets/blue.png", "Assets/green.png", "Assets/green.png", "Assets/yellow.png", "Assets/lightning.png", "Assets/lightning.png", "Assets/lightning.png", "Assets/lightning.png"]
DISPLAY = pygame.display.set_mode((800, 600))
Player = pygame.image.load("Assets/hk2GhR.png")
icon = pygame.image.load("Assets/icon.png")
pygame.display.set_icon(Player)
Caught = 10
class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        global Score
        if Score > 25:
            self.sprite = random.randint(0, 15)
        else:
            self.sprite = random.randint(0, 11)
        super().__init__()
        global BloonsType
        if Difficulty == 1:
            y = random.randint(100, 550)
        else:
            y = random.randint(30, 550)
        self.image = pygame.image.load(BloonsType[self.sprite])
        self.rect = self.image.get_rect(center=(10, y))
    def collision(self):
        if self.rect.colliderect(Player_rect):
            Blop_SFX.play()
            global Color
            global Score
            global Enemy_group
            global Caught
            global Score 
            if self.sprite in range(6):
                Caught += 1
                Score += 1
                Color = "Assets/red.png"
            if self.sprite in range(6, 9):
                Caught += 1
                Score += 3
                Color = "Assets/blue.png"
            if self.sprite in range(9, 11):
                Caught += 1
                Score += 5
                Color = "Assets/green.png"
            if self.sprite == 11:
                Caught += 1
                Score += 10
                Color = "Assets/yellow.png"
            if self.sprite in range(12, 13) and len(Group.sprites()) > 0 and Difficulty == 1:
                Caught -= 1
                Group.remove(Group.sprites()[0])
                Score -= 10
            if self.sprite in range(12, 16) and len(Group.sprites()) > 0 and Difficulty == 2:
                Caught -= 1
                Group.remove(Group.sprites()[0])
                Score -= 10
            self.kill()
    def update(self):
        global Speed
        self.rect.x += Speed * Difficulty
        self.collision()
class Bloons(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global Color
        self.image = pygame.image.load(Color)
        self.rect = self.image.get_rect(center=(random.randint(730,760), Player_rect.centery))
    def start(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE] and game:
            self.kill()
    def movement(self):
        self.rect.centery = Player_rect.y - 20
    def update(self):
        self.movement()
Balloons = []
velocity = 1
Red = pygame.image.load("Assets/red.png")
Blue = pygame.image.load("Assets/blue.png")
Green = pygame.image.load("Assets/green.png")
Yellow = pygame.image.load("Assets/yellow.png")
FONT1 = pygame.font.Font("Assets/font.otf", 50)
FONT2 = pygame.font.Font("Assets/font.otf", 100)
Main_menu = FONT1.render("Press ONE to start flopping!", False, "Aqua")
Main_menu_rect = Main_menu.get_rect(center=(400, 500))
Balloons_count = FONT2.render(f"", False, "Gray")
Balloons_count_rect = Balloons_count.get_rect(center=(380, 300))
pygame.display.set_caption("Flop-n-pop")
Player = pygame.transform.scale(Player, (90, 80))
Player_rect = Player.get_rect(center=(750, 300))
Easy_sign = FONT1.render("EASY MODE", False, "Green")
Easy_sign_rect = Easy_sign.get_rect(center=(400, 200))
Medium_sign = FONT1.render("NORMAL MODE", False, "Orange")
Medium_sign_rect = Medium_sign.get_rect(center=(400, 300))
Hard_sign = FONT1.render("HARD MODE", False, "Red")
Hard_sign_rect = Hard_sign.get_rect(center=(400, 400))
Timer = pygame.USEREVENT + 2
pygame.time.set_timer(Timer, 500)
FPS = pygame.time.Clock()
straped = 0
Group = pygame.sprite.Group()
Enemy_group = pygame.sprite.Group()
menu = True
game = False
difficulty_chooser = False
played = False
animation = 0
up = True
down = False
Done = 0
Difficulty = 0
Handicap = 0
while True:
    if Score > 50 and Score < 100 and Done == 0 and Difficulty == 1:
        Speed = 7
        pygame.time.set_timer(Timer, 450)
        Done += 1
    elif Score > 100 and Score < 150 and Done == 1 and Difficulty == 1:
        Speed = 13
        pygame.time.set_timer(Timer, 400)
        Done += 1
    elif Score > 150 and Score < 200 and Done == 2 and Difficulty == 1:
        Speed = 19
        pygame.time.set_timer(Timer, 350)
        Done += 1
    elif Score > 200 and Score < 250 and Done == 3 and Difficulty == 1:
        Speed = 24
        pygame.time.set_timer(Timer, 300)
        Done += 1
    if Score > 50 and Score < 100 and Done == 0 and Difficulty == 2:
        Speed = 7
        pygame.time.set_timer(Timer, 400)
        Done += 1
    elif Score > 100 and Score < 150 and Done == 1 and Difficulty == 2:
        Speed = 13
        pygame.time.set_timer(Timer, 370)
        Done += 1
    elif Score > 150 and Score < 200 and Done == 2 and Difficulty == 2:
        Speed = 19
        pygame.time.set_timer(Timer, 340)
        Done += 1
    elif Score > 200 and Score < 250 and Done == 3 and Difficulty == 2:
        Speed = 24
        pygame.time.set_timer(Timer, 300)
        Done += 1
    if game:
        if Caught != len(Group.sprites()):
            if Caught < len(Group.sprites()):
                Group.remove(Group.sprites()[0])
            if Caught > len(Group.sprites()):
                Group.add(Bloons())
        Balloons_count = FONT2.render(f"{Score}", False, "Gray")
        Player_rect.y += velocity
        velocity += 0.5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == Timer:
                Enemy_group.add(Enemies())
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_SPACE] and event.type == pygame.KEYDOWN and Caught > 0:
                velocity = 0
                velocity -= 10
                Caught -= 1
                played = True
        if Player_rect.y > 600 or Player_rect.y < -50:
            game = False
            menu = True
            played = True
        DISPLAY.fill("White")
        DISPLAY.blit(Balloons_count, Balloons_count_rect)
        DISPLAY.blit(Player, Player_rect)
        Enemy_group.draw(DISPLAY)
        Enemy_group.update()
        Group.draw(DISPLAY)
        Group.update()
        if Difficulty == 1 and Handicap == 1:
            end += 3
            pygame.draw.rect(DISPLAY, "Black", (0, 0, end, 50))
            if end > 800:
                end = 0
                Color = "Assets/red.png"
                Group.add(Bloons())
        FPS.tick(60)
        pygame.display.flip()
    elif menu:
        DISPLAY.fill((80,199,199))
        if played == False:
            DISPLAY.blit(Main_menu, Main_menu_rect)
        else:
            Main_menu = FONT1.render(f"Your score is {Score}", False, "Aqua")
            DISPLAY.blit(Main_menu, (Main_menu_rect.x + 100, Main_menu_rect.y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        animation += 1
        if animation % 60 == 0:
            up = not up
            down = not down
        if up:
            Main_menu_rect.y -= 1
        if down:
            Main_menu_rect.y += 1
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_1]:
            pygame.time.set_timer(Timer, 500)
            Done = 0
            Speed = 5
            Color = "Assets/red.png"
            for x in range(10):
                Group.add(Bloons())
            Previous_Frame = 10
            Enemy_group.empty()
            Player_rect.y = 200
            Balloons_count = FONT1.render(f"{len(Group.sprites())}", False, "Gray")
            Caught = 10
            menu = False
            difficulty_chooser = True
            velocity = 1
            Score = 0
            end = 0
        DISPLAY.blit(icon, (200, 50))
        FPS.tick(60)
        pygame.display.flip()
    elif difficulty_chooser:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if Easy_sign_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                Handicap = 1
                end = 0
                Difficulty = 1
                game = True
                difficulty_chooser = False
            if Medium_sign_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                Handicap = 0
                end = 0
                Difficulty = 1
                game = True
                difficulty_chooser = False
            if Hard_sign_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                Handicap = 0
                Difficulty = 2
                game = True
                difficulty_chooser = False
        DISPLAY.fill((80,199,199))
        DISPLAY.blit(Easy_sign, Easy_sign_rect)
        DISPLAY.blit(Medium_sign, Medium_sign_rect)
        DISPLAY.blit(Hard_sign, Hard_sign_rect)
        FPS.tick(60)
        pygame.display.update()