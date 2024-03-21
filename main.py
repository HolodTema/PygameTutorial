import pygame as pg
import pygame.image

clock = pg.time.Clock()

pg.init()
screen = pg.display.set_mode((1440, 800))
pg.display.set_caption('Pygame tutorial')
icon = pg.image.load('images/icon.png').convert()
pg.display.set_icon(icon)

background = pg.image.load('images/background.png').convert()
player = pg.image.load('images/hero1_r.png').convert_alpha()

sound_background = pg.mixer.Sound('sounds/background.mp3')
# sound_background.play()

walk_right = [
    pg.image.load('images/hero1_r.png').convert_alpha(),
    pg.image.load('images/hero2_r.png').convert_alpha(),
    pg.image.load('images/hero3_r.png').convert_alpha(),
    pg.image.load('images/hero4_r.png').convert_alpha()
]

walk_left = [
    pg.image.load('images/hero1_l.png').convert_alpha(),
    pg.image.load('images/hero2_l.png').convert_alpha(),
    pg.image.load('images/hero3_l.png').convert_alpha(),
    pg.image.load('images/hero4_l.png').convert_alpha()
]
player_anim_count = 0
player_speed = 8
player_x = 150
player_y = 600
is_jump = False
jump_count = 10

background_x = 0

ghost = pygame.image.load('images/ghost.png').convert_alpha()
ghost_list = []

timer_ghost = pg.USEREVENT + 1
pg.time.set_timer(timer_ghost, 2500)

label = pg.font.Font('fonts/myfont_bold.ttf', 40)
label_lose = label.render('You lose!', False, (193, 196, 199))
label_play_again = label.render('Play again', False, (115, 132, 148))
rect_label_play_again = label_play_again.get_rect(topleft=(500, 400))
gameplay = True

running = True
while running:

    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 1440, 0))

    if gameplay:
        background_x = background_x - 2 if background_x - 2 >= -1440 else 0

        keys = pg.key.get_pressed()
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
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 10

        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
        if ghost_list:
            # if len>0
            for i, el in enumerate(ghost_list):
                # for every rect we draw image of ghost in coordinates of el (rect)
                screen.blit(ghost, el)
                el.x -= 10
                if el.x < -100:
                    ghost_list.pop(i)
                if player_rect.colliderect(el):
                    gameplay = False
    else:
        screen.fill((87, 88, 89))
        screen.blit(label_lose, (500, 300))
        screen.blit(label_play_again, rect_label_play_again)

        mouse = pg.mouse.get_pos()
        if rect_label_play_again.collidepoint(mouse) and pg.mouse.get_pressed()[0]:
            player_x = 150
            ghost_list.clear()
            gameplay = True



    pg.display.update()
    # proper handling of quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
        if event.type == timer_ghost:
            ghost_list += [ghost.get_rect(topleft=(1440, 600))]

    clock.tick(30)
