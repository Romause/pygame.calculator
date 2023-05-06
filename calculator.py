import pygame
import button
pygame.init()

bounds = (360, 648)
screen = pygame.display.set_mode(bounds)
buttons = []

pygame.display.set_caption('Calculator')


def draw_text(screen, text, size, x, y, color):
    font_name = pygame.font.match_font("Arial")
    font = pygame.font.Font(font_name, size)
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect()
    text_rect = center = (x, y)
    screen.blit(text_image, text_rect)


buttonsObject = []
i = 1
height = 90
width = 360
run = True
clock = pygame.time.Clock()

for btn in buttons:
    if i % 4 == 0:
        height += 90
        width = 360
    buttonsObject.append(button.Button('#000000', '#696969', btn, 180 if i == 1 else 90, 90, bounds, bounds[0] - width, bounds[1] - height))



while run:
    screen.fill('#FFFFFF')
    mousePos = pygame.mouse.get_pos()
    colorHover = '#F9F06F'
    color = '#F9F01F'

    pygame.draw.rect(screen, '#000000', (360 - 180, 640 - 82, 90, 90))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()

    clock.tick(60)
    for btn in buttonsObject:
        btn.draw(screen)

    pygame.display.flip()
pygame.quit()
