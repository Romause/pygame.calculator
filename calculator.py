import pygame
import button
pygame.init()


def draw_text(screen, text, size, x, y, color):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_image, text_rect)


bounds = (360, 640)
screen = pygame.display.set_mode(bounds)
i = 1

height = 90
width = 360
buttons = ['0',',','=','1','2','3','+','4','5','6','-','7','8','9','x','AC','+/-','%','÷']
buttonsObject = []

pygame.display.set_caption('Calculator')
clock = pygame.time.Clock()

for btn in buttons:
    if i % 4 == 0:
        height += 90
        width = 360
    buttonsObject.append(button.Button('#000000', '#696969', btn, 180 if i == 1 else 90, 90, bounds, bounds[0] - width,bounds[1] - height))
    width -= 180 if i == 1 else 90
    i += 1


run = True
while run:
    clock.tick(60)

    isClicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            isClicked = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            isClicked = True

    screen.fill('#FFFFFF')




    mousePos = pygame.mouse.get_pos()

    color = '#000000'
    if 360 > mousePos[0] > 360 - 90 and 640 > mousePos[1] > 640 - 90:
        color = '#353535'
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor()
    pygame.draw.rect(screen, color, (360 - 90, 640 - 90, 90, 90))
    draw_text(screen, '=', 45, 360 - 45, 640 - 45, '#FFFFFF')

    pygame.draw.rect(screen, '#678392', (360 - 180, 640 - 90, 90, 90))

    pygame.display.flip()

pygame.quit()
