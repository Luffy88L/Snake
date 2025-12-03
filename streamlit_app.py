import pygame
import time
import random

# กำหนดสีที่ใช้ในเกม
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# ขนาดหน้าจอ
dis_width = 600
dis_height = 400

# เริ่มต้น Pygame
pygame.init()

# กำหนดขนาดหน้าจอ
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# กำหนดฟอนต์
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# ฟังก์ชันแสดงคะแนน
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

# ฟังก์ชันแสดงข้อความในเกม
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# ฟังก์ชันหลักของเกม
def gameLoop():
    game_over = False
    game_close = False

    # กำหนดตำแหน่งเริ่มต้นของงู
    x1 = dis_width / 2
    y1 = dis_height / 2

    # กำหนดการเคลื่อนที่ของงู
    x1_change = 0
    y1_change = 0

    # กำหนดความยาวของงู
    snake_block = 10
    snake_speed = 15

    # งู
    snake_List = []
    Length_of_snake = 1

    # กำหนดตำแหน่งอาหาร
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # การเล่นเกม
    clock = pygame.time.Clock()

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                    if event.key == pygame.K_c:
                        gameLoop()

        # กราฟิกในเกม
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # เช็คถ้างูชนขอบจอ
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # วาดอาหาร
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # วาดงู
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for block in snake_List:
            pygame.draw.rect(dis, yellow, [block[0], block[1], snake_block, snake_block])

        # แสดงคะแนน
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # เช็คว่าอาหารถูกกินไหม
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
