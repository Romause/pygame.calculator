import pygame
import button
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
    colorHover = '#F9F06F'
    color = '#F9F01F'
    button.Button(color, colorHover, '=', 360, 648, bounds, 360 - 90, 640 - 82)
    pygame.draw.rect(screen, '#000000', (360 - 180, 640 - 82, 90, 90))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()

    clock.tick(60)

    pygame.display.flip()
pygame.quit()
