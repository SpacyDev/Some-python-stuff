import pygame
import time
import random

pygame.init() #начало всего процесса для pygame 
 
white = (255, 255, 255)
yellow = (255,255,102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0,255, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height  = 400

dis = pygame.display.set_mode((dis_width, dis_height))  #задаётся ширина и высота окна  
pygame.display.set_caption('Snake Game') #Название окна
 
clock = pygame.time.Clock() #обьект для отсчета времени

snake_block=10 #размер змейки
snake_speed=10 #скорость змейки

font_style = pygame.font.SysFont("bahnschrift", 25) #стиль шрифта меню
score_font = pygame.font.SysFont("staatliches", 25) #стиль шрифта кол-во очков

def Your_score(score): #функция для отображения количества очков
    value = score_font.render("Your Score: "+ str(score), True, yellow)
    dis.blit(value,[0, 0])

def our_snake(snake_block, snake_list): #функция для отрисовывания блока змейки
    for x in snake_list:
        pygame.draw.rect(dis, black,[x[0],x[1],snake_block,snake_block])

def message(msg,color): #функция отображения какого-либо сообщения в окне
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

def gameLoop(): #функция для самой игры, игра идет пока змейка не удариться 
    game_over = False 
    game_close = False 
    #декартова система координат
    x1 = dis_width/2 #ось абсцисс 
    y1 = dis_height/2 #ось ординат
    # местонахождение змейки
    x1_change = 0 
    y1_change = 0

    snake_List = [] #змейка
    Length_of_snake = 1 #длина змейки
    acceleration = 0 #ускорение змейки
    #спавн еды
    foodx = round(random.randrange(0,dis_width - snake_block)/10)*10
    foody = round(random.randrange(0,dis_height - snake_block)/10)*10
  
    while not game_over:
        #функционал меню
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit ir C-Play Again",red)
            Your_score(Length_of_snake-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key ==pygame.K_c:
                        gameLoop()
        #тут клавиша Escape значит выйти из игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN: #тут движение змейки 
                if event.key == pygame.K_LEFT: #налево
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT: #направо
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP: #вверх
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN: #вниз
                    y1_change = snake_block
                    x1_change = 0
    
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #тут удар об стенку описывается 
            game_close = True    
        x1 += x1_change #тут движение змейки по оси OX
        y1 += y1_change  #тут движение змейки по оси OY
        dis.fill(blue) #голубой фон
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) #отрисовка еды
        snake_Head = [] 
        snake_Head.append(x1) #движение змейки у именно перемещение с точки на точку в системе координат
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List)>Length_of_snake: #перемещение путём удаление последнего местоположения змеи 
            del snake_List[0] 

        for x in snake_List[:-1]: #удар змейки об саму себя конец
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List) #отрисовывает змейку снова и снова
        Your_score(Length_of_snake - 1) #отрисовывает счет снова и снова

        pygame.display.update()#функция pygame которая должна вызваться после отрисовки обьектов на экране
    
        if x1 == foodx and y1 == foody: #покушает удлиниться и ускориться
            foodx = round(random.randrange(0,dis_width - snake_block)/10)*10
            foody = round(random.randrange(0,dis_height - snake_block)/10)*10
            Length_of_snake+=1
            acceleration+=1
        clock.tick(snake_speed+acceleration)#увеличения кадров в секунду насчет чего увеличивается и скорость
    
    
    pygame.quit() #конец всего процесса для pygame
    quit()

gameLoop() #вызов функции игры

