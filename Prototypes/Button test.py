import pygame, Button_Class_01
pygame.init()

Window_Width, Window_Height = 360, 360
Screen = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption("Button test")
Screen.fill((255, 255, 255))

Butt_On_Img = pygame.image.load('Images/Butt On_Btn.png').convert_alpha()
Butt_On_Btn = Button_Class.Button(96, 152, Butt_On_Img, 0.5)

Amount_Of_Butts = 0

def Screen_Text():
    global Amount_Of_Butts

    Font = pygame.font.SysFont('NeueBit', 24)
    Text = Font.render('Amount of butts: ', True, ('black'))

    Butts_Indicator = Font.render(f'{Amount_Of_Butts}', True, ('black'))

    Paddle_Width = 160
    Paddle_Height = 48
    Text_Paddle = pygame.Surface((Paddle_Width, Paddle_Height))
    Text_Paddle.fill(('white'))
    pygame.draw.rect(Text_Paddle, "black", [0, 0, Paddle_Width, Paddle_Height], 2)

    Text_Paddle.blit(Text, (8, 16))
    Text_Paddle.blit(Butts_Indicator, (130, 16))
    Screen.blit(Text_Paddle, (32, 24))

Run = True
while Run:
    Amount_Of_Butts

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False

    Screen_Text()

    if Butt_On_Btn.draw(Screen):
        Amount_Of_Butts += 1
        print ('Working')

    pygame.display.update()
    fps = 60

pygame.quit()