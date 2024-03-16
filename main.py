import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 300))
pg.display.set_caption('Pygame tutorial')
icon = pg.image.load('images/icon.png')
pg.display.set_icon(icon)

player = pg.image.load('images/icon.png')


running = True
while running:
    screen.blit(player, (100, 50))

    pg.display.update()
    # proper handling of quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
       


