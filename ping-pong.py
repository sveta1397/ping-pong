from pygame import *

win_width = 700
win_height = 500
display.set_caption("PING_PONG")
window = display.set_mode((win_width, win_height))

back = (200, 255, 255) 
window.fill(back)
game = True #флаг сбрасывается кнопкой закрытия окна
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)
        display.update()
    time.delay(50)
