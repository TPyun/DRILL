import random
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024 #사진 크기

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT) #사진 크기의 캔버스

hand = load_image('hand_arrow.png')
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2 #xy좌표를 가운데로 정렬
frame = 0

handx = random.randint(1, KPU_WIDTH)
handy = random.randint(1, KPU_HEIGHT)

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw(handx, handy)
    if x > handx:
        character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
        x -= 1
    elif x < handx:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        x += 1
    if y > handy:
        y -= 1
    elif y < handy:
        y += 1
    elif x == handx and y == handy:
        handx = random.randint(1, KPU_WIDTH)
        handy = random.randint(1, KPU_HEIGHT)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




