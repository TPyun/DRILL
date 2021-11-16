import game_framework
from pico2d import *
import random
import game_world

PIXEL_PER_METER = (10.0 / 0.3) # 10pixel 30cm
RUN_SPEED_KMPH = 50.0  # 50Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 1500), random.randint(100, 500)
        self.velocity = 0
        self.frame = 0
        self.ima = load_image('bird100x100x14.png')
        self.velocity += RUN_SPEED_PPS
        self.dir = clamp(-1, self.velocity, 1)

    def update(self):
        if self.x > 1500:
            self.velocity = -1 * RUN_SPEED_PPS
        elif self.x < 100:
            self.velocity = RUN_SPEED_PPS
        self.x += self.velocity * game_framework.frame_time
        self.dir = clamp(-1, self.velocity, 1)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

    def draw(self):
        if self.dir == 1:
            self.ima.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y, 100, 100)
            # (left, bottom, width, height, x, y, w=None, h=None)
        else:
            self.ima.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0, 'h', self.x, self.y, 100, 100)
            # (left, bottom, width, height, rad, flip, x, y, w = None, h = None)