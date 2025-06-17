import os
import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1100, 650
DELTA={pg.K_UP:(0,-5),pg.K_DOWN:(0,+5),pg.K_LEFT:(-5,0),pg.K_RIGHT:(+5,0),}#移動量辞書
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def check_bound(obj_rct: pg.Rect) -> tuple[bool, bool]:
    """
    引数：こうかとんRectかばくだんRect
    戻り値：タプル（横方向判定結果，縦方向判定結果）
    画面内ならTrue，画面外ならFalse
    """
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right: # 横方向判定
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom: # 縦方向判定
        tate = False
    return yoko, tate



def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    clock = pg.time.Clock()
    tmr = 0
    bb_img=pg.Surface((20,20))
    pg.draw.circle(bb_img,(255,0,0),(10,10),10)
    bb_img.set_colorkey((0,0,0))
    bb_rct=bb_img.get_rect()
    bb_rct.centerx=random.randint(0,WIDTH)
    bb_rct.centery=random.randint(0,HEIGHT)
    vx=+5
    vy=+5    
    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for key,mv in DELTA.items():
            if key_lst[key]:
                sum_mv[1]+=mv[1]
                sum_mv[0]+=mv[0]
        kk_bound=check_bound(kk_rct)
        if not kk_bound[0] or not kk_bound[1]:
            sum_mv=[0,0]
        # if key_lst[pg.K_UP]:
        #     sum_mv[1] -= 5
        # if key_lst[pg.K_DOWN]:
        #     sum_mv[1] += 5
        # if key_lst[pg.K_LEFT]:
        #     sum_mv[0] -= 5
        # if key_lst[pg.K_RIGHT]:
        #     sum_mv[0] += 5
        kk_rct.move_ip(sum_mv)
        screen.blit(kk_img, kk_rct)
        bb_bound=check_bound(bb_rct)
        if not bb_bound[0]:
            vx=-vx
        if not bb_bound[1]:
            vy=-vy
        bb_rct.move_ip(vx,vy)
        screen.blit(bb_img,bb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)
        if kk_rct.colliderect(bb_rct):
            return



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
