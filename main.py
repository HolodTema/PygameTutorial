import pygame as pg

clock = pg.time.Clock()

pg.init()
screen = pg.display.set_mode((1440, 800))
pg.display.set_caption('Pygame tutorial')
icon = pg.image.load('images/icon.png')
pg.display.set_icon(icon)

background = pg.image.load('images/background.png')
player = pg.image.load('images/hero1_r.png')

sound_background = pg.mixer.Sound('sounds/background.mp3')
sound_background.play()

walk_right = [
    pg.image.load('images/hero1_r.png'),
    pg.image.load('images/hero2_r.png'),
    pg.image.load('images/hero3_r.png'),
    pg.image.load('images/hero4_r.png')
]

walk_left = [
    pg.image.load('images/hero1_l.png'),
    pg.image.load('images/hero2_l.png'),
    pg.image.load('images/hero3_l.png'),
    pg.image.load('images/hero4_l.png')
]
player_anim_count = 0
background_x = 0


running = True
while running:
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x+1440, 0))
    background_x = background_x-2 if background_x-2>=-1440 else 0

    screen.blit(walk_right[player_anim_count], (300, 300))
    player_anim_count = player_anim_count+1 if player_anim_count+1<len(walk_left) else 0



    pg.display.update()
    # proper handling of quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()


    clock.tick(30)


