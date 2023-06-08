# lib
import sys
import math
import pygame
#from pygame.locals import *
# src
import game

# 変数・定数
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WINDOW_WIDTH = SCREEN_WIDTH * 2
WINDOW_HEIGHT = SCREEN_HEIGHT * 2
FRAME_RATE = 60
clock = pygame.time.Clock()

# 初期化
#pygame.mixer.pre_init(44100,-16,2,512,None,AUDIO_ALLOW_FREQUENCY_CHANGE | AUDIO_ALLOW_CHANNELS_CHANGE)
pygame.mixer.pre_init(44100,-16,2,512,None)
#pygame.init()

try:
    pygame.init()
    print("pygameはインストールされています。")
    print("pygameバージョン:", pygame.version.ver)
except ImportError:
    print("pygameはインストールされていません。")


# RenderTargetView
rtv = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# RenderBuffer
rb = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
game = game.Game()

# メインループ
frame = 0
exit_game = False
while not exit_game:
    for event in pygame.event.get():
        # ゲーム終了イベントハンドラ.
        if event.type == pygame.QUIT:
            exit_game = True
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or (event.mod & pygame.KMOD_META and event.key == pygame.K_q):
                exit_game = True        
    # セーフティ
    if frame > 100:
      break
    frame = frame + 1

    # 処理更新
    game.update()

    # 描画更新
    rb.fill((255,255,0)) # 画面クリア
    #game.draw() # ゲームオブジェクト描画
    rtv.blit(pygame.transform.scale(rb, (WINDOW_WIDTH, WINDOW_HEIGHT)), (0, 0))  # 拡大コピー
    pygame.display.flip()
    clock.tick(FRAME_RATE) # フレーム待機

# 終了
print("END game")
pygame.quit()
sys.exit(0)         