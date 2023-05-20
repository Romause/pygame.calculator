import pygame
import button
import operands

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

pygame.display.set_caption('Calculator')
clock = pygame.time.Clock()

buttons = ['0', ',', '=', '1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '×', 'AC', '+/-', '%', '÷']
buttonsObject = []
mainText = ''
operatorA = 0
operatorB = 0
operand = ''
result = 0

i = 1
height = 90
width = 360
for btn in buttons:
    if i % 4 == 0:
        height += 90
        width = 360
    buttonsObject.append(button.Button('#000000' if i == 3 else '#000000', '#6A5ACD' if i == 3 else '#696969', btn,
                                       179 if i == 1 else 89, 89, bounds, bounds[0] - width, bounds[1] - height))
    width -= 180 if i == 1 else 90
    i += 1

fps = 60
run = True

while run:
    clock.tick(fps)
    IsClicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            IsClicked = False
        if event.type == pygame.MOUSEBUTTONUP:
            IsClicked = True

    screen.fill('#FFFFFF')
    pygame.draw.rect(screen, '#000000', (0, 0, 400, 189))
    pygame.draw.rect(screen, '#FFFFFF', (0, 0, 400, 220))

    for btn in buttonsObject:
        text = btn.draw(screen, IsClicked)
        if text and text[0] == 'operand':
            if text[1] != '=':
                operand = text[1]
                if not operatorA:
                    operatorA = mainText
                    mainText = ''
                else:
                    operatorB = mainText
                    mainText = ''
            else:
                if not operatorB:
                    operatorB = mainText
                if operand == '+':
                    mainText = str(int(operatorA) + int(operatorB))
                elif operand == 'x':
                    mainText = str(int(operatorA) * int(operatorB))
                elif operand == '÷':
                    mainText = str(int(operatorA) / int(operatorB))
                elif operand == '%':
                    mainText = str(int(operatorA) / 100)
                operand = '='
        elif text and text[0] == 'method':
            if text[1] == 'AC':
                mainText = ''
                operatorA = 0
                operatorB = 0
                result = 0
            elif text[1] == '+/=':
                if len(mainText) != 0:
                    if mainText[0] != '-':
                        mainText = '-' + mainText
                    else:
                        mainText = mainText.replace('-', '')
                else:
                    mainText = '-'
        elif text:
            if operand == '=':
                mainText = ''
                operatorA = 0
                operatorB = 0
                operand = ''
                result = 0
            mainText += text
    draw_text(screen, bounds, mainText)

    pygame.display.flip()

pygame.quit()
