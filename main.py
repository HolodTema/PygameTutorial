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
# sound_background.play()

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
player_speed = 8
player_x = 150
player_y = 600
is_jump = False
jump_count = 10

background_x = 0

running = True
while running:
    keys = pg.key.get_pressed()

    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 1440, 0))
    background_x = background_x - 2 if background_x - 2 >= -1440 else 0

    if keys[pg.K_a]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))
    player_anim_count = player_anim_count + 1 if player_anim_count + 1 < len(walk_left) else 0

    if keys[pg.K_d] and player_x < 400:
        player_x += player_speed
    elif keys[pg.K_a] and player_x > 20:
        player_x -= player_speed

    if not is_jump:
        if keys[pg.K_w]:
            is_jump = True
    else:
        if jump_count >= -10:
            if jump_count > 0:
                player_y -= (jump_count**2)/2
            else:
                player_y += (jump_count**2)/2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    pg.display.update()
    # proper handling of quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()

    clock.tick(30)
