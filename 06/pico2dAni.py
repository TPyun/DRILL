from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while 1:
    x = 400
    while x < 770:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 2
        delay(0.01)

    y = 90
    while y < 550:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(770, y)
        y += 2
        delay(0.01)

    x = 770
    while x > 30:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 550)
        x -= 2
        delay(0.01)

    y = 550
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(30, y)
        y -= 2
        delay(0.01)

    x = 30
    while x < 400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 2
        delay(0.01)
