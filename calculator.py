import pygame

pygame.init()

bounds = (360, 648)
screen = pygame.display.set_mode(bounds)

pygame.display.set_caption('Calculator')


def draw_text(screen, text, size, x, y, color):
    font_name = pygame.font.match_font("Arial")
    font = pygame.font.Font(font_name, size)
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect()
    text_rect = center = (x, y)
    screen.blit(text_image, text_rect)


run = True
clock = pygame.time.Clock()
while run:
    screen.fill('#FFFFFF')
    mousePos = pygame.mouse.get_pos()
    color = '#F9F01F'
    if 360 > mousePos[0] > 360 - 90 and 640 > mousePos[1] > 640 - 82:
        color = '#F9F06F'
    pygame.draw.rect(screen, color, (360 - 90, 640 - 82, 90, 90))
    draw_text(screen, '=', 50, 360 - 55, 640 - 65, '#FFFFFF')
    pygame.draw.rect(screen, '#000000', (360 - 180, 640 - 82, 90, 90))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()

    clock.tick(60)

    pygame.display.flip()
pygame.quit()
